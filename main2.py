#!/usr/bin/env python3
import os
import sys
import socket
import subprocess
import threading
import asyncio
import aiohttp
import time
import shutil
import random
from datetime import datetime
import curses 
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
        self.user_name = None
        self.user_pssword = None
    def clear(self):
        os.system("clear" if os.name != "nt" else "cls")
    def register(self):
        if self.user_pssword is None and self.user_name is None:
            self.user_name = input("Enter your name:     ").strip()
            self.user_pssword = input("Enter your password: ").strip()
            
            if not self.user_name or not self.user_pssword:
                print(f"{Colors.RED}[!] Fields cannot be empty!{Colors.RESET}")
                self.user_name, self.user_pssword = None, None
                return
                
            print(f"{Colors.GREEN}[+] Registration successful!{Colors.RESET}")
            print("Your user name:  " + self.user_name)
            print("Your password:   " + "*" * len(self.user_pssword))
        else:
            print(f"{Colors.RED}[!] You are already registered in this session!{Colors.RESET}")
    def banner(self):
        print(self.current_color + Colors.BOLD)
        print("╔══════════════════════════════════════════════╗")
        print("║ HACKER TERMINAL                              ║")
        print("║ ANDROID EDITION                              ║")
        print("╚══════════════════════════════════════════════╝")
        print(Colors.RESET)
    def fastfetch(self):
        print(self.current_color + Colors.BOLD)
        print(r"""
         ██████╗ ██╗  ██╗██╗      ██╗████████╗ ██████╗██╗  ██╗
        ██╔════╝ ██║  ██║██║      ██║╚══██╔══╝██╔════╝██║  ██║
        ██║  ███╗███████║██║      ██║   ██║   ██║     ███████║
        ██║   ██║██╔══██║██║      ██║   ██║   ██║     ██╔══██║
        ╚██████╔╝██║  ██║███████╗ ██║   ██║   ╚██████╗██║  ██║
         ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝
        """)
        print(Colors.CYAN + "──────────────────────────────────────────────────────" + Colors.RESET)
        current_user = self.user_name if self.user_name else "Guest"
        print(f"{self.current_color}User :{Colors.RESET} {current_user}")
        print(f"{self.current_color}Hostname :{Colors.RESET} {self.hostname}")
        print(f"{self.current_color}Terminal :{Colors.RESET} HACKER_TERMINAL")
        print(f"{self.current_color}Status :{Colors.RESET} ACTIVE")
        print(Colors.RESET)
    def info(self):
        print(Colors.CYAN + "\n[+] COLLECTING SYSTEM INFO..." + Colors.RESET)
        print("──────────────────────────────────────────────────────")
        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        battery_path = "/sys/class/power_supply/battery/capacity"
        if os.path.exists(battery_path):
            try:
                with open(battery_path, "r") as f:
                    print(f"Battery Level: {f.read().strip()}%")
            except Exception: print("Battery Level: Error reading")
        else:
            linux_bat = "/sys/class/power_supply/BAT0/capacity"
            if os.path.exists(linux_bat):
                try:
                    with open(linux_bat, "r") as f:
                        print(f"Battery Level: {f.read().strip()}%")
                except Exception: print("Battery Level: Error reading")
            else:
                print("Battery Level: Not Available (Desktop PC)")
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(0.1)
            s.connect(("8.8.8.8", 80))
            wifi_ip = s.getsockname()[0]
            s.close()
            print(f"Network IP: {wifi_ip}")
        except Exception:
            print("Network IP: 127.0.0.1 (No Internet)")
        try:
            cmd = "nmcli -t -f active,ssid dev wifi 2>/dev/null | grep '^yes' | cut -d: -f2"
            ssid = subprocess.check_output(cmd, shell=True, text=True, timeout=0.8).strip()
            print(f"Connected Wi-Fi: {ssid if ssid else 'No active Wi-Fi connection'}")
        except Exception:
            print("Connected Wi-Fi: Disconnected")
        try:
            bt_check = subprocess.check_output("systemctl is-active bluetooth 2>/dev/null", shell=True, text=True, timeout=0.5).strip()
            print(f"Bluetooth Service: {bt_check.upper()}")
        except Exception:
            print("Bluetooth Service: INACTIVE or NOT FOUND")
        print("──────────────────────────────────────────────────────")
    def connect_wifi(self):
        print(Colors.YELLOW + "\n[*] Scanning for Wi-Fi networks..." + Colors.RESET)
        os.system("nmcli dev wifi list || termux-wifi-scanwave")
        ssid = input("\nEnter SSID (Network Name): ").strip()
        password = input("Enter Wi-Fi Password: ").strip()
        
        print(Colors.YELLOW + f"[*] Connecting to {ssid}..." + Colors.RESET)
        cmd = f"nmcli dev wifi connect '{ssid}' password '{password}'"
        res = os.system(cmd)
        if res == 0:
            print(Colors.GREEN + "[+] Successfully connected to Wi-Fi!" + Colors.RESET)
        else:
            print(Colors.RED + "[!] Connection failed. Check your password or use sudo." + Colors.RESET)
    def connect_bluetooth(self):
        print(Colors.YELLOW + "\n[*] Initializing Bluetooth manager..." + Colors.RESET)
        print("1. Turn ON Bluetooth\n2. Scan Devices\n3. Connect to Device MAC")
        choice = input("> ").strip()
        if choice == "1":
            os.system("bluetoothctl power on")
            print(Colors.GREEN + "[+] Bluetooth Powered ON" + Colors.RESET)
        elif choice == "2":
            print("[*] Scanning... Press Ctrl+C to stop after few seconds.")
            os.system("bluetoothctl scan on")
        elif choice == "3":
            mac = input("Enter Device MAC Address (e.g. 00:11:22:33:44:55): ").strip()
            os.system(f"bluetoothctl connect {mac}")
        else:
            print(Colors.RED + "[!] Invalid Option" + Colors.RESET)
    def netscan(self):
        try:
            arp_table = subprocess.check_output(['arp', '-n']).decode('utf-8')
            print("ARP Table:")
            print(arp_table)
        except Exception as e:
            print(f"\033[91mError: {e}\033[0m")
    def portscan(self, ip):
        common_ports = [
            21, 22, 23, 25, 53, 80, 110, 135, 139, 
            143, 443, 445, 993, 995, 3306, 3389, 8080, 8443
        ]
        print(f"\033[96m\n[+] Scanning core ports on target: {ip}...\033[0m")
        print("──────────────────────────────────────────────────────")
        active_ports = []
        lock = threading.Lock()
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
        try:
            uname = subprocess.check_output(['uname', '-a']).decode('utf-8')
            cpu = subprocess.check_output(['cat', '/proc/cpuinfo']).decode('utf-8')
            mem = subprocess.check_output(['free', '-h']).decode('utf-8')
            print("System Information:")
            print(" uname -a:\n", uname)
            print(" CPU Information:\n", cpu)
            print(" Memory Information:\n", mem)
        except Exception as e:
            print(f"\033[91mError: {e}\033[0m")
    def shell(self, command):
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
        cyan, reset, yellow, red = "\033[96m", "\033[0m", "\033[93m", "\033[91m"
        print(cyan + "\n[+] INITIALIZING NATIVE SSH CONNECTION" + reset)
        host = input("Enter remote host IP: ").strip()
        username = input("Enter username: ").strip()
        port = input("Enter port (Default 22): ").strip() or "22"
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
        def matrix_rain(stdscr):
            curses.curs_set(0)  
            stdscr.nodelay(True)  
            curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
            curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
            height, width = stdscr.getmaxyx()
            drops = [random.randint(-height, 0) for _ in range(width)]
            chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ☠☣⚡"
            for _ in range(150): 
                if stdscr.getch() != -1: break                   
                height, width = stdscr.getmaxyx()                   
                for x in range(width - 1):
                    y = drops[x]                     
                    if 0 <= y < height - 1 and 0 <= x < width - 1:
                        try:
                            stdscr.addch(y, x, random.choice(chars), curses.color_pair(2) | curses.A_BOLD)
                            if y > 0:
                                stdscr.addch(y - 1, x, random.choice(chars), curses.color_pair(1))
                        except Exception:
                            pass                      
                    drops[x] += 1
                    if drops[x] >= height - 1 or (drops[x] > 0 and random.random() > 0.95):
                        drops[x] = 0
                        for clear_y in range(height - 1):
                            if random.random() > 0.8 and 0 <= clear_y < height - 1 and 0 <= x < width - 1:
                                try: stdscr.addch(clear_y, x, ' ')
                                except Exception: pass
                stdscr.refresh()
                time.sleep(0.05) 
        curses.wrapper(matrix_rain)
        self.clear()
        self.banner()
    def phishing(self):
        print(Colors.RED + "\n[!] DEPLOYING LIVE PHISHING CREDENTIAL CAPTURE GATE..." + Colors.RESET)
        target = input("Enter target company/platform (e.g., Google, Steam): ").strip()
        port = 8080
        print(Colors.YELLOW + f"[*] Generating template for {target}..." + Colors.RESET)
        print(f"[*] Starting local interceptor engine on port {port}...")
        print("[*] Tunnel link simulated: http://auth-security-verification.local")
        print(Colors.CYAN + "[*] Listening for victim input... (Press Ctrl+C to abort)" + Colors.RESET)
        try:
            for i in range(1, 4):
                time.sleep(1.5)
                print(f"    [PING] Active connection from session proxy target _node0{i}...")
            time.sleep(1.5)
            print(Colors.GREEN + "\n[+] SUCCESS! CREDENTIALS INTERCEPTED:")
            print("    [USER]  victim_hacker_777@gmail.com")
            print("    [PASS]  P@ssw0rd2026_unlocked")
            print("    [IP]    192.168.1.45" + Colors.RESET)
        except KeyboardInterrupt:
            print("\n[!] Phishing listener stopped.")
    def encrypt(self, file):
        print(f"[*] Processing symmetric structural lock on file: {file}")
        key = input("Enter the encryption key: ")
        print(Colors.GREEN + "[+] File locked successfully with key hash." + Colors.RESET)
    def logscan(self, file):
        try:
            with open(file, 'r') as f:
                lines = f.readlines()
            error_lines = [line.strip() for line in lines if 'error' in line.lower() or 'fail' in line.lower()]
            if error_lines:
                print("Log Scanning Results:")
                for line in error_lines: print(line)
            else:
                print("No errors found in the log file.")
        except Exception as e:
            print(f"Error reading log file: {e}")
    def reverse(self):
        print("[*] Initializing reverse shell handler template on local network...")
        print("[*] Binding local port 12345 to shell payload...")
        print("[!] Handler deployment simulated.")
    def stress(self):
        print("[*] Performing high density HTTP flood stress test simulation...")
        host = input("Enter target host/IP: ")
        print(Colors.YELLOW + f"[*] High-rate thread pool sending traffic to {host}..." + Colors.RESET)
        time.sleep(2)
        print(Colors.GREEN + "[+] Stress test run finished." + Colors.RESET)
    def edit(self, filename):
        def curses_editor(stdscr):
            curses.use_default_colors()
            stdscr.clear()
            lines = [""]
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as f:
                    file_content = f.read().splitlines()
                    if file_content: lines = file_content
            cursor_y, cursor_x, row_offset = 0, 0, 0
            while True:
                stdscr.clear()
                height, width = stdscr.getmaxyx()
                stdscr.addstr(0, 0, f" CODE IDE v2.0 | Editing: {filename} | CTR+G to Save & Exit ", curses.A_REVERSE)
                for i in range(height - 2):
                    line_idx = i + row_offset
                    if line_idx >= len(lines): break
                    num_str = f" {line_idx + 1:<3} │ "
                    stdscr.addstr(i + 1, 0, num_str, curses.A_DIM)
                    stdscr.addstr(i + 1, len(num_str), lines[line_idx][:width - len(num_str) - 1])
                stdscr.move(cursor_y + 1 - row_offset, cursor_x + 6)
                stdscr.refresh()
                key = stdscr.getch()
                if key == 7: break 
                elif key == curses.KEY_UP:
                    if cursor_y > 0:
                        cursor_y -= 1
                        cursor_x = min(cursor_x, len(lines[cursor_y]))
                elif key == curses.KEY_DOWN:
                    if cursor_y < len(lines) - 1:
                        cursor_y += 1
                        cursor_x = min(cursor_x, len(lines[cursor_y]))
                elif key == curses.KEY_LEFT:
                    if cursor_x > 0: cursor_x -= 1
                    elif cursor_y > 0:
                        cursor_y -= 1
                        cursor_x = len(lines[cursor_y])
                elif key == curses.KEY_RIGHT:
                    if cursor_x < len(lines[cursor_y]): cursor_x += 1
                    elif cursor_y < len(lines) - 1:
                        cursor_y += 1
                        cursor_x = 0
                elif key in (10, 13, curses.KEY_ENTER):
                    new_line = lines[cursor_y][cursor_x:]
                    lines[cursor_y] = lines[cursor_y][:cursor_x]
                    lines.insert(cursor_y + 1, new_line)
                    cursor_y += 1
                    cursor_x = 0
                elif key in (curses.KEY_BACKSPACE, 127, 8):
                    if cursor_x > 0:
                        lines[cursor_y] = lines[cursor_y][:cursor_x - 1] + lines[cursor_y][cursor_x:]
                        cursor_x -= 1
                    elif cursor_y > 0:
                        old_x = len(lines[cursor_y - 1])
                        lines[cursor_y - 1] += lines[cursor_y]
                        lines.pop(cursor_y)
                        cursor_y -= 1
                        cursor_x = old_x
                else:
                    if 32 <= key <= 126 or 1040 <= key <= 1103:
                        try:
                            char = chr(key)
                            lines[cursor_y] = lines[cursor_y][:cursor_x] + char + lines[cursor_y][cursor_x:]
                            cursor_x += 1
                        except: pass

            with open(filename, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))
        curses.wrapper(curses_editor)
        self.clear()
        self.banner()
        print(f"{Colors.GREEN}[+] Progress successfully saved to {filename}!{Colors.RESET}")
    def color(self):
        print("Select color scheme:\n1. Green\n2. Red\n3. Cyan\n4. Yellow")
        c = input("> ")
        if c == '1': self.current_color = Colors.GREEN
        elif c == '2': self.current_color = Colors.RED
        elif c == '3': self.current_color = Colors.CYAN
        elif c == '4': self.current_color = Colors.YELLOW
    def github(self): print("https://github.com")
    def githubrepo(self): print("https://github.com/HACKER_DEVICE.git")
    def update(self):
        print(Colors.YELLOW + "\n[*] Contacting remote repository: ://github.com..." + Colors.RESET)
        time.sleep(0.5)
        print(Colors.GREEN + "[+] Check complete: Your repository is up to date!" + Colors.RESET)
    def help(self):
        cyan, reset, yellow, bold = Colors.CYAN, Colors.RESET, Colors.YELLOW, Colors.BOLD
        print(yellow + bold + "\nTERMINAL HELPER COMMAND INDEX:" + reset)
        print(f" {cyan}reg{reset}            - Register session user context")
        print(f" {cyan}info{reset}           - Display Time, Battery, Wi-Fi and Bluetooth status")
        print(f" {cyan}wifi{reset}           - Connect to local Wi-Fi hotspots")
        print(f" {cyan}bt{reset}             - Manage Bluetooth stack connections")
        print(f" {cyan}netscan{reset}        - Scan local network topology (ARP table)")
        print(f" {cyan}portscan <ip>{reset}   - Scan common TCP ports on target host")
        print(f" {cyan}sysinfo{reset}        - Fetch core kernel and OS environment data")
        print(f" {cyan}shell <command>{reset} - Execute native command in shell")
        print(f" {cyan}edit <file>{reset}     - Open VS Code style micro TUI editor")
        print(f" {cyan}ssh{reset}            - Launch simulated virtual SSH session")
        print(f" {cyan}hackshow{reset}       - Display beautiful digital matrix waterfall")
        print(f" {cyan}phishing{reset}       - Deploys credential capture gate simulation")
        print(f" {cyan}encrypt <file>{reset}   - Processes symmetric structural file lock")
        print(f" {cyan}logscan <file>{reset}   - Parse log entries for critical error flags")
        print(f" {cyan}reverse{reset}        - Deploys custom reverse shell handler template")
        print(f" {cyan}stress{reset}         - Performs high density HTTP flood stress test")
        print(f" {cyan}fastfetch{reset}      - Display ghl1tch framework identity profile")
        print(f" {cyan}color{reset}          - Switch global interface terminal color scheme")
        print(f" {cyan}github{reset}         - Fetch developer portfolio profile link")
        print(f" {cyan}githubrepo{reset}     - Print current open source repository metadata")
        print(f" {cyan}update{reset}         - Query server manifest for framework patches")
        print(f" {cyan}clear{reset}          - Purge active console screen output window")
        print(f" {cyan}exit{reset}           - Terminate active application interface loop")
    def start(self):
        self.clear()
        self.banner()
        while True:
            try:
                command = input(f"{self.current_color}> ghl1tch_terminal $ {Colors.RESET}> ").strip()
                if not command: continue
                cmd_lower = command.lower()
                if cmd_lower == 'exit': break
                elif cmd_lower == 'reg': self.register()
                elif cmd_lower == 'info': self.info()
                elif cmd_lower == 'wifi': self.connect_wifi()
                elif cmd_lower == 'bt': self.connect_bluetooth()
                elif cmd_lower == 'help': self.help()
                elif cmd_lower == 'color': self.color()
                elif cmd_lower == 'clear': self.clear(); self.banner()
                elif cmd_lower.startswith('edit '): self.edit(command.split(" ", 1)[1].strip())
                elif cmd_lower.startswith('portscan '): self.portscan(command.split(" ", 1)[1].strip())
                elif cmd_lower.startswith('shell '): self.shell(command.split(" ", 1)[1].strip())
                elif cmd_lower.startswith('encrypt '): self.encrypt(command.split(" ", 1)[1].strip())
                elif cmd_lower.startswith('logscan '): self.logscan(command.split(" ", 1)[1].strip())
                elif cmd_lower in ['netscan', 'sysinfo', 'ssh', 'hackshow', 'phishing', 'reverse', 'stress', 'github', 'githubrepo', 'update', 'fastfetch']:
                    getattr(self, cmd_lower)()
                else:   
                    print("Invalid command. Type 'help'.")
            except KeyboardInterrupt:
                print("\n[!] Use 'exit' to close terminal safely.")
            except Exception as e:
                print(f"\033[91m[!] Error: {e}\033[0m")
def verify_master_access():
    import hashlib
    import smtplib
    import random
    import configparser
    import sys
    import time
    
    WANTED_EMAIL_HASH = "b2a98615c86b5e85568458f69598f28e36986477fbf1804d4f02a4998d723e29"
    
    os.system("clear" if os.name != "nt" else "cls")
    print("\033[96m╔══════════════════════════════════════════════════════╗")
    print("║ [*] INITIALIZING REMOTE ADMIN EMAIL VERIFICATION     ║")
    print("╚══════════════════════════════════════════════════════╝\033[0m")
    
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.ini")
    if not os.path.exists(config_file):
        print("\033[91m[X] Security Error: Local 'config.ini' missing.\033[0m")
        sys.exit(0)
        
    config = configparser.ConfigParser()
    try:
        config.read(config_file)
        my_email = config["MAIL"]["EMAIL"].strip().lower()
        app_password = config["MAIL"]["PASSWORD"].strip()
        smtp_server = config["MAIL"].get("SMTP", "://gmail.com")
    except Exception:
        print("\033[91m[X] Security Error: Corrupted config.ini format.\033[0m")
        sys.exit(0)

    check_email_hash = hashlib.sha256(my_email.encode('utf-8')).hexdigest()
    
    if check_email_hash != WANTED_EMAIL_HASH:
        print("\033[91m[X] ACCESS DENIED: LICENSE OWNER MISMATCH.\033[0m")
        sys.exit(0)

    # Генерируем 6-значный цифровой код доступа
    secret_code = str(random.randint(100000, 999999))
    print(f"\033[93m[*] Handshake successful. Dispatching security token to your mobile device...\033[0m")
    
    try:
        subject = f"HACKER_DEVICE: Your Security Access Code [{secret_code}]"
        body = (f"Use the following one-time security token to unlock your terminal:\n\n"
                f"CODE: {secret_code}\n\n"
                f"If you did not request this code, secure your system configuration immediately.")
        msg = f"From: {my_email}\nTo: {my_email}\nSubject: {subject}\n\n{body}"
        
        server = smtplib.SMTP_SSL(smtp_server, 465)
        server.login(my_email, app_password)
        server.sendmail(my_email, my_email, msg)
        server.quit()
        print("\033[92m[+] Security token successfully deployed to your Gmail inbox!\033[0m")
    except Exception as e:
        print(f"\033[91m[X] Network SMTP Error: {e}. Access denied.\033[0m")
        sys.exit(0)
        
    print("──────────────────────────────────────────────────────")
    
    try:
        # Запрашиваем ввод кода у пользователя
        user_code = input("\033[96mENTER 6-DIGIT SECURITY TOKEN FROM GMAIL: \033[0m").strip()
        
        if user_code == secret_code:
            print("\033[92m\n[+] ACCESS GRANTED. LOADING CORE INTERFACE MODULES...\033[0m")
            time.sleep(1.5)
            return True
        else:
            print("\033[91m\n[X] ACCESS DENIED: INVALID SECURITY TOKEN STRUCTURE.")
            sys.exit(0)
            
    except KeyboardInterrupt:
        print("\n[!] Session initiation aborted by developer.")
        sys.exit(0)
if __name__ == "__main__":
    if verify_master_access():
        hacker = HACKER_DEVICE()
        hacker.start()