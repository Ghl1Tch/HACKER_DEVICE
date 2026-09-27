import os
import sys
import socket
import subprocess
import time
import threading

class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

class PwnTerminal:
    def __init__(self):
        self.hostname = socket.gethostname()
        self.history = []

    def clear_screen(self):
        os.system('clear')

    def print_banner(self):
        print(f"{Colors.CYAN}╔══════════════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.GREEN}║     PWN-TERMINAL OS v2.0 | ANDROID EDITION   ║{Colors.RESET}")
        print(f"{Colors.CYAN}╚══════════════════════════════════════════════╝{Colors.RESET}")
        print(f"[+] System: {Colors.GREEN}ONLINE{Colors.RESET} | Type 'help' for commands\n")

    def run_netscan(self):
        """Сканирование сети через ARP-таблицу"""
        print(f"\n{Colors.YELLOW}[*] Scanning local network (ARP table)...{Colors.RESET}")
        try:
            with open("/proc/net/arp", "r") as f:
                lines = f.readlines()
            
            print(f"\n{Colors.GREEN}{'IP Address':<16} {'MAC Address':<18} {'Interface':<10}{Colors.RESET}")
            print("-" * 50)
            
            devices = []
            for line in lines[1:]:
                parts = line.split()
                if len(parts) >= 4 and parts[0] != "IP":
                    ip = parts[0]
                    mac = parts[3]
                    iface = parts[5] if len(parts) > 5 else "?"
                    if mac != "00:00:00:00:00:00":
                        devices.append((ip, mac, iface))
                        print(f"{ip:<16} {mac:<18} {iface:<10}")
            
            print(f"\n{Colors.BLUE}[+] Found {len(devices)} active devices{Colors.RESET}")
            
            # Сохраняем для portscan
            self.last_scan = [d[0] for d in devices]
            
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {str(e)}{Colors.RESET}")
        input(f"\n{Colors.BLUE}Press Enter...{Colors.RESET}")

    def run_portscan(self, target):
        """Многопоточный сканер портов"""
        print(f"\n{Colors.YELLOW}[*] Scanning {target}...{Colors.RESET}")
        
        ports = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 
            53: "DNS", 80: "HTTP", 110: "POP3", 139: "NetBIOS",
            443: "HTTPS", 445: "SMB", 3306: "MySQL", 3389: "RDP", 
            8080: "HTTP-Alt", 5555: "ADB"
        }
        
        try:
            target_ip = socket.gethostbyname(target)
            print(f"{Colors.GREEN}[+] Target: {target_ip}{Colors.RESET}\n")
            print(f"{Colors.BLUE}{'PORT':<8} {'STATE':<10} {'SERVICE':<15}{Colors.RESET}")
            print("-" * 35)
            
            open_ports = []
            
            def scan_port(port, service):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                if s.connect_ex((target_ip, port)) == 0:
                    print(f"{Colors.GREEN}{port:<8} {'OPEN':<10} {service:<15}{Colors.RESET}")
                    open_ports.append(port)
                s.close()
            
            # Запускаем потоки
            threads = []
            for port, service in ports.items():
                t = threading.Thread(target=scan_port, args=(port, service))
                t.start()
                threads.append(t)
                time.sleep(0.01)  # Небольшая задержка для стабильности
            
            for t in threads:
                t.join()
            
            if not open_ports:
                print(f"{Colors.RED}[-] No open ports found{Colors.RESET}")
            else:
                print(f"\n{Colors.GREEN}[+] Total open: {len(open_ports)}{Colors.RESET}")
                
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {str(e)}{Colors.RESET}")
        input(f"\n{Colors.BLUE}Press Enter...{Colors.RESET}")

    def run_sysinfo(self):
        """Детальная информация о системе"""
        print(f"\n{Colors.GREEN}=== SYSTEM DIAGNOSTICS ==={Colors.RESET}")
        print(f"Hostname: {self.hostname}")
        print(f"Platform: Android (Termux Linux)")
        
        # Получаем инфу через uname
        try:
            uname = subprocess.check_output(['uname', '-a']).decode().strip()
            print(f"Kernel: {uname}")
        except:
            pass
        
        # Инфо о батарее (Android specific)
        try:
            with open("/sys/class/power_supply/battery/capacity", "r") as f:
                batt = f.read().strip()
            print(f"Battery: {batt}%")
        except:
            pass
        
        # CPU info
        try:
            with open("/proc/cpuinfo", "r") as f:
                cpu = f.read()
            cores = cpu.count("processor")
            model = [l for l in cpu.split('\n') if 'model name' in l]
            if model:
                print(f"CPU: {model[0].split(':')[1].strip()} ({cores} cores)")
        except:
            pass
            
        input(f"\n{Colors.BLUE}Press Enter...{Colors.RESET}")

    def run_shell(self, cmd):
        """Выполнение системных команд"""
        command = " ".join(cmd)
        print(f"{Colors.YELLOW}[*] Executing: {command}{Colors.RESET}\n")
        try:
            subprocess.run(command, shell=True)
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {str(e)}{Colors.RESET}")
        input(f"\n{Colors.BLUE}Press Enter...{Colors.RESET}")

    def start_ssh(self):
        """Запуск SSH сервера"""
        print(f"\n{Colors.YELLOW}[*] Starting SSH server...{Colors.RESET}")
        try:
            # Проверяем установлен ли openssh
            result = subprocess.run(['which', 'sshd'], capture_output=True)
            if result.returncode != 0:
                print(f"{Colors.RED}[!] OpenSSH not installed. Run: pkg install openssh{Colors.RESET}")
                input("Press Enter...")
                return
            
            subprocess.Popen(['sshd'])
            time.sleep(1)
            
            # Получаем IP
            ip = subprocess.check_output(['ifconfig', 'wlan0']).decode()
            ip = [l for l in ip.split('\n') if 'inet ' in l][0].split()[1]
            
            print(f"{Colors.GREEN}[+] SSH server started!{Colors.RESET}")
            print(f"{Colors.CYAN}[i] Connect from PC:{Colors.RESET}")
            print(f"    ssh -p 8022 $(whoami)@{ip}")
            
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {str(e)}{Colors.RESET}")
        input(f"\n{Colors.BLUE}Press Enter...{Colors.RESET}")

    def show_help(self):
        print(f"\n{Colors.YELLOW}Available Commands:{Colors.RESET}")
        print(f"  {Colors.GREEN}netscan{Colors.RESET}          - Scan local network (ARP)")
        print(f"  {Colors.GREEN}portscan <ip>{Colors.RESET}    - Scan ports on target")
        print(f"  {Colors.GREEN}sysinfo{Colors.RESET}          - System information")
        print(f"  {Colors.GREEN}shell <cmd>{Colors.RESET}      - Execute system command")
        print(f"  {Colors.GREEN}ssh{Colors.RESET}              - Start SSH server")
        print(f"  {Colors.GREEN}clear{Colors.RESET}            - Clear screen")
        print(f"  {Colors.GREEN}exit{Colors.RESET}             - Shutdown terminal")
        input(f"\n{Colors.BLUE}Press Enter...{Colors.RESET}")

    def start(self):
        while True:
            self.clear_screen()
            self.print_banner()
            
            try:
                cmd = input(f"{Colors.GREEN}pwn_sh# {Colors.RESET}").strip()
                if not cmd:
                    continue
                
                parts = cmd.split()
                command = parts[0].lower()
                args = parts[1:]
                
                if command == "help":
                    self.show_help()
                elif command == "netscan":
                    self.run_netscan()
                elif command == "portscan" and args:
                    self.run_portscan(args[0])
                elif command == "sysinfo":
                    self.run_sysinfo()
                elif command == "shell" and args:
                    self.run_shell(args)
                elif command == "ssh":
                    self.start_ssh()
                elif command == "clear":
                    continue
                elif command == "exit":
                    print(f"\n{Colors.RED}[!] Shutting down...{Colors.RESET}")
                    sys.exit(0)
                else:
                    print(f"{Colors.RED}[!] Unknown: {command}{Colors.RESET}")
                    time.sleep(1)
                    
            except KeyboardInterrupt:
                print(f"\n{Colors.YELLOW}[!] Ctrl+C detected. Type 'exit' to quit.{Colors.RESET}")
                time.sleep(1)
            except Exception as e:
                print(f"{Colors.RED}[!] Error: {str(e)}{Colors.RESET}")
                time.sleep(1)

if __name__ == "__main__":
    term = PwnTerminal()
    term.start()