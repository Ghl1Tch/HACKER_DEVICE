#!/usr/bin/env python3

import os
import socket
import subprocess
import threading
import asyncio
import aiohttp
import time
import shutil




class Colors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"




class HACKER_DEVICE:
    # Initialize terminal variables
    def __init__(self):
        self.hostname = socket.gethostname()
        self.history = []
        self.last_scan = []
    # Clear the terminal screen
    def clear(self):
        os.system("clear")
    # Display the main HACKER-OS banner
    def banner(self):
        print(Colors.GREEN + Colors.BOLD)
        print("╔══════════════════════════════════════════════╗")
        print("║             HACKER-OS TERMINAL               ║")
        print("║                 ANDROID EDITION              ║")
        print("╠══════════════════════════════════════════════╣")
        print(f"║    HOST   : {self.hostname:<33}║")
        print("║    STATUS : ONLINE                           ║")
        print("╚══════════════════════════════════════════════╝")
        print(Colors.RESET)
    # Display a Fastfetch-style system profile
    def fastfetch(self):
        print(Colors.GREEN + Colors.BOLD)

        print("        ██████╗ ██╗  ██╗██╗     ")
        print("       ██╔════╝ ██║  ██║██║     ")
        print("       ██║  ███╗███████║██║     ")
        print("       ██║   ██║██╔══██║██║     ")
        print("       ╚██████╔╝██║  ██║███████╗")
        print("        ╚═════╝ ╚═╝  ╚═╝╚══════╝")

        print(Colors.RESET)

        print(Colors.CYAN + "────────────────────────────────────" + Colors.RESET)
        print(f"{Colors.GREEN}User      :{Colors.RESET} ghl1tch")
        print(f"{Colors.GREEN}Hostname  :{Colors.RESET} {self.hostname}")
        print(f"{Colors.GREEN}OS        :{Colors.RESET} Hacker OS")
        print(f"{Colors.GREEN}Terminal  :{Colors.RESET} HACKER-OS TERMINAL")
        print(f"{Colors.GREEN}Status    :{Colors.RESET} ONLINE")
        print(Colors.CYAN + "────────────────────────────────────" + Colors.RESET)
    # Scan the local ARP network table
    def netscan(self):
        print(Colors.CYAN + "\n[+] NETWORK SCAN" + Colors.RESET)
        try:
            with open("/proc/net/arp") as file:
                lines = file.readlines()[1:]
            self.last_scan = []
            for line in lines:
                parts = line.split()
                if len(parts) >= 6 and parts[3] != "00:00:00:00:00:00":
                    ip, mac, interface = parts[0], parts[3], parts[5]
                    self.last_scan.append(
                        (ip, mac, interface)
                    )
                    print(
                        f"[+] {ip:<16} "
                        f"{mac:<18} "
                        f"{interface}"
                    )
            print(
                f"\n[+] Devices: "
                f"{len(self.last_scan)}"
            )
        except Exception as e:
            print(
                f"{Colors.RED}"
                f"[!] {e}"
                f"{Colors.RESET}"
            )
    # Scan common TCP ports on a target
    def portscan(self, target):
        ports = [
            21, 22, 23, 25, 53,
            80, 110, 139, 143,
            443, 445, 3306, 3389, 8080
        ]
        print(
            Colors.CYAN +
            f"\n[+] PORT SCAN: {target}" +
            Colors.RESET
        )
        def scan(port):
            try:
                sock = socket.socket(
                    socket.AF_INET,
                    socket.SOCK_STREAM
                )
                sock.settimeout(0.5)
                if sock.connect_ex(
                    (target, port)
                ) == 0:
                    print(
                        f"{Colors.GREEN}"
                        f"[OPEN] {port}"
                        f"{Colors.RESET}"
                    )
                sock.close()
            except Exception:
                pass
        threads = [
            threading.Thread(
                target=scan,
                args=(port,)
            )
            for port in ports
        ]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        print(
            Colors.GREEN +
            "[+] Scan complete" +
            Colors.RESET
        )
    # Display basic system information
    def sysinfo(self):
        print(
            Colors.CYAN +
            "\n[+] SYSTEM INFORMATION" +
            Colors.RESET
        )
        try:
            system = subprocess.check_output(
                ["uname", "-a"],
                text=True
            ).strip()
            print(f"System   : {system}")
            print(f"Hostname : {self.hostname}")
            print(f"CPU      : {os.cpu_count()} cores")
        except Exception as e:
            print(
                f"{Colors.RED}"
                f"[!] {e}"
                f"{Colors.RESET}"
            )
    # Execute a local shell command
    def shell(self, command):
        subprocess.run(command, shell=True)
    # Start the SSH service and display the local address
    def ssh(self):
        print(
            Colors.CYAN +
            "\n[+] SSH SERVICE" +
            Colors.RESET
        )
        if subprocess.run(
            "pgrep sshd",
            shell=True
        ).returncode != 0:
            subprocess.run(
                "sshd",
                shell=True
            )
        try:
            ip = subprocess.check_output(
                "ip route get 1.1.1.1 | awk '{print $7; exit}'",
                shell=True,
                text=True
            ).strip()
            user = os.getenv(
                "USER",
                "user"
            )
            print(
                f"{Colors.GREEN}"
                f"[+] SSH: ssh {user}@{ip}"
                f"{Colors.RESET}"
            )
        except Exception as e:
            print(
                f"{Colors.RED}"
                f"[!] {e}"
                f"{Colors.RESET}"
            )
    # Display a system activity animation
    def hackshow(self):
        print(
            Colors.GREEN +
            "\n[+] SYSTEM ACCESS" +
            Colors.RESET
        )
        for name in [
            "Initializing modules",
            "Scanning interfaces",
            "Analyzing network",
            "Processing packets",
            "Loading system data",
            "Finalizing operation"
        ]:
            print(f"[*] {name}")

            for i in range(20):
                print(
                    f"\r[{('#' * (i + 1)).ljust(20)}]"
                    f" {(i + 1) * 5}%",
                    end=""
                )

                time.sleep(0.03)
            print()
        print(
            Colors.GREEN +
            "[+] Operation complete" +
            Colors.RESET
        )
    # Display a local login demonstration
    def phishing(self):
        print(
            Colors.CYAN +
            "\n[+] LOGIN INTERFACE" +
            Colors.RESET
        )
        username = input("Login: ")
        input("Password: ")
        print(
            Colors.GREEN +
            f"\n[+] Account: {username}" +
            Colors.RESET
        )
        print("[+] Request processed")
    # Create an altered copy of a local file
    def encrypt(self, filename):
        if not os.path.isfile(filename):
            print(
                f"{Colors.RED}"
                "[!] File not found"
                f"{Colors.RESET}"
            )
            return
        output = filename + ".encrypted"
        try:
            shutil.copy2(
                filename,
                output
            )

            with open(
                output,
                "rb"
            ) as file:
                data = file.read()

            data = bytes(
                byte ^ 0xAA
                for byte in data
            )

            with open(
                output,
                "wb"
            ) as file:
                file.write(data)

            print(
                Colors.GREEN +
                f"[+] Created: {output}" +
                Colors.RESET
            )
        except Exception as e:
            print(
                f"{Colors.RED}"
                f"[!] {e}"
                f"{Colors.RESET}"
            )
    # Search a text file for selected keywords
    def logscan(self, filename):
        if not os.path.isfile(filename):
            print(
                f"{Colors.RED}"
                "[!] File not found"
                f"{Colors.RESET}"
            )
            return
        try:
            with open(
                filename,
                "r",
                errors="ignore"
            ) as file:
                lines = file.readlines()
            keywords = [
                "password",
                "login",
                "username",
                "admin"
            ]
            matches = 0
            for line in lines:
                if any(
                    word in line.lower()
                    for word in keywords
                ):
                    print(
                        "[MATCH] Sensitive keyword detected"
                    )

                    matches += 1
            print(
                f"\n[+] Matches: {matches}"
            )
        except Exception as e:
            print(
                f"{Colors.RED}"
                f"[!] {e}"
                f"{Colors.RESET}"
            )
    # Display reverse-link architecture information
    def reverse(self):
        print(
            Colors.CYAN +
            "\n[+] REVERSE LINK" +
            Colors.RESET
        )
        print("[+] Connection architecture")
        print("[+] Client -> Server")
        print("[+] Authentication required")
        print("[+] Command channel disabled")
    # Send one local HTTP request
    async def stress_worker(self, session):
        try:
            async with session.get(
                "http://127.0.0.1:8080",
                timeout=3
            ):
                return True
        except Exception:
            return False
    # Run the local HTTP load demonstration
    async def stress_async(self):
        print(
            Colors.CYAN +
            "\n[+] STRESS" +
            Colors.RESET
        )
        print("[+] Target: 127.0.0.1:8080")
        async with aiohttp.ClientSession() as session:
            tasks = [
                self.stress_worker(session)
                for _ in range(20)]
            results = await asyncio.gather(
                *tasks
            )
        print(
            Colors.GREEN +
            f"[+] Requests completed: "
            f"{sum(results)}/20" +
            Colors.RESET
        )
    # Start the local HTTP load demonstration
    def stress(self):
        asyncio.run(
            self.stress_async()
        )
    # Open the GitHub profile
    def github(self):
        url = "https://github.com/Ghl1Tch"
        print(
            Colors.CYAN +
            "\n[+] GITHUB" +
            Colors.RESET
        )
        print(f"[+] {url}")
        subprocess.run(
            ["xdg-open", url]
        )
    # Open the GitHub repository
    def githubrepo(self):
        url = "https://github.com/Ghl1Tch/JeremyAI_betaversion"
        print(
            Colors.CYAN +
            "\n[+] GITHUB REPOSITORY" +
            Colors.RESET
        )
        print(f"[+] {url}")
        subprocess.run(
            ["xdg-open", url]
        )
    # Update the current Git repository
    def update(self):
        print(
            Colors.CYAN +
            "\n[+] REPOSITORY UPDATE" +
            Colors.RESET
        )
        print(
            "[*] Pulling latest commit..."
        )
        subprocess.run(
            ["git", "pull"]
        )
    # Display the available commands
    def help(self):
        print(
            Colors.CYAN +
            "\nCOMMANDS" +
            Colors.RESET
        )
        print("netscan              — Scan network")
        print("portscan <ip>        — Scan TCP ports")
        print("sysinfo              — Show system information")
        print("shell <command>      — Run shell command")
        print("ssh                  — Start SSH service")
        print("hackshow             — Show system activity")
        print("phishing             — Show login demo")
        print("encrypt <file>       — Encrypt file copy")
        print("logscan <file>       — Scan log file")
        print("reverse              — Show reverse-link info")
        print("stress               — Localhost stress test")
        print("fastfetch            — Show system profile")
        print("github               — Open GitHub profile")
        print("githubrepo           — Open GitHub repository")
        print("update               — Update repository")
        print("clear                — Clear terminal")
        print("help                 — Show command list")
        print("exit                 — Close terminal")
    # Start the main terminal loop
    def start(self):
        self.clear()
        self.banner()
        while True:
            try:
                command = input(
                    Colors.GREEN +
                    "\npwn@android:~$ " +
                    Colors.RESET
                ).strip()
                if not command:
                    continue
                self.history.append(command)
                parts = command.split(
                    " ",
                    1
                )
                action = parts[0].lower()
                argument = (
                    parts[1]
                    if len(parts) > 1
                    else ""
                )
                if action == "netscan":
                    self.netscan()
                elif action == "portscan":
                    argument and self.portscan(argument) or print("Usage: portscan <ip>")
                elif action == "sysinfo":
                    self.sysinfo()
                elif action == "shell":
                    argument and self.shell(argument) or print("Usage: shell <command>")
                elif action == "ssh":
                    self.ssh()
                elif action == "hackshow":
                    self.hackshow()
                elif action == "phishing":
                    self.phishing()
                elif action == "encrypt":
                    argument and self.encrypt(argument) or print("Usage: encrypt <file>")
                elif action == "logscan":
                    argument and self.logscan(argument) or print("Usage: logscan <file>")
                elif action == "reverse":
                    self.reverse()
                elif action == "stress":
                    self.stress()
                elif action == "fastfetch":
                    self.fastfetch()
                elif action == "github":
                    self.github()
                elif action == "githubrepo":
                    self.githubrepo()
                elif action == "update":
                    self.update()
                elif action == "clear":
                    self.clear()
                    self.banner()
                elif action == "help":
                    self.help()
                elif action == "exit":
                    print("[+] Terminal closed")
                    break
                else:
                    print("[!] Unknown command")
            except KeyboardInterrupt:
                print("\n[!] Use exit to close")
            except Exception as e:
                print(
                    f"{Colors.RED}"
                    f"[!] {e}"
                    f"{Colors.RESET}"
                )
# Start the application
def main():
    HACKER_DEVICE().start()
if __name__ == "__main__":
    main()