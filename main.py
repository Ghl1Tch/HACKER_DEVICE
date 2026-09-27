import os
import sys
import socket
import subprocess
import time
class Colors:
    """ ANSI color codes for clean and professional terminal output """
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
class PwnTerminal:
    def __init__(self):
        self.hostname = socket.gethostname()

    def clear_screen(self):
        """ Clears the terminal screen screen buffer """
        os.system('clear')
    def print_banner(self):
        """ Displays the main interactive retro-hacker CLI welcome interface """
        print(f"{Colors.BLUE}=================================================={Colors.RESET}")
        print(f"{Colors.GREEN}       PWN-TERMINAL OS CORE ENGINE v1.0          {Colors.RESET}")
        print(f"{Colors.BLUE}=================================================={Colors.RESET}")
        print(f"[+] System status: {Colors.GREEN}ONLINE{Colors.RESET}")
        print(f"[+] Device architecture: {os.uname().machine}")
        print(f"[+] Type 'help' to review available framework utilities.\n")
    def run_netscan(self):
        """ Parses local area network active ARP bindings tables """
        print(f"\n{Colors.YELLOW}[*] Initializing local network topology discovery...{Colors.RESET}")
        try:
            # Reads the native Linux virtual network routing table directly in Termux
            with open("/proc/net/arp", "r") as f:
                arp_lines = f.readlines()
            
            print(f"\n{Colors.GREEN}IP Address      HW Type     Flags       MAC Address         Interface{Colors.RESET}")
            for line in arp_lines[1:]:
                print(line.strip())
        except Exception as e:
            print(f"{Colors.RED}[!] Network discovery failed: {str(e)}{Colors.RESET}")
        input(f"\n{Colors.BLUE}Press Enter to return to shell...{Colors.RESET}")
    def run_sysinfo(self):
        """ Pulls detailed operational variables from the underlying OS kernel """
        print(f"\n{Colors.GREEN}=== SYSTEM DIAGNOSTICS ==={Colors.RESET}")
        print(f"Node Name     : {self.hostname}")
        print(f"Kernel Release: {os.uname().release}")
        print(f"OS Version    : Android Linux environment")
        input(f"\n{Colors.BLUE}Press Enter to return to shell...{Colors.RESET}")
    def run_system_command(self, cmd_args):
        """ Forwards execution strings directly to the underlying Linux subsystem """
        sys_cmd = " ".join(cmd_args)
        print(f"{Colors.YELLOW}[*] Executing system process: {sys_cmd}{Colors.RESET}\n")
        try:
            # Executes standard terminal commands (like ls, top, pwd) inside Termux
            subprocess.run(sys_cmd, shell=True)
        except Exception as e:
            print(f"{Colors.RED}[!] Runtime execution fault: {str(e)}{Colors.RESET}")
        input(f"\n{Colors.BLUE}Press Enter to return to shell...{Colors.RESET}")
    def start_shell(self):
        """ Main interactive input evaluation loop router """
        while True:
            self.clear_screen()
            self.print_banner()
            
            try:
                # Custom terminal prompt layout string
                user_input = input(f"{Colors.GREEN}pwn_sh# {Colors.RESET}").strip()
                if not user_input:
                    continue
                # Tokenize string input array elements
                tokens = user_input.split()
                command = tokens[0].lower()
                if command == "help":
                    print(f"\n{Colors.YELLOW}Available Commands:{Colors.RESET}")
                    print("  help          - Display this utility manual lookup table")
                    print("  netscan       - Discover active network nodes via ARP scanning")
                    print("  sysinfo       - Print detailed hardware system configurations")
                    print("  shell <cmd>   - Execute low-level system binaries natively")
                    print("  exit          - Shutdown active terminal core environment")
                    input(f"\n{Colors.BLUE}Press Enter to return to shell...{Colors.RESET}")
                elif command == "netscan":
                    self.run_netscan()
                elif command == "sysinfo":
                    self.run_sysinfo()
                elif command == "shell":
                    if len(tokens) < 2:
                        print(f"{Colors.RED}[!] Error: usage 'shell <arguments>'{Colors.RESET}")
                        time.sleep(1.5)
                        continue
                    self.run_system_command(tokens[1:])
                elif command == "exit":
                    print(f"\n{Colors.RED}[!] Shutting down terminal pipeline...{Colors.RESET}")
                    sys.exit(0)
                else:
                    print(f"{Colors.RED}[!] Command directive token '{command}' not recognized.{Colors.RESET}")
                    time.sleep(1.5)
            except (KeyboardInterrupt, EOFError):
                # Intercepts standard terminal break inputs to prevent premature script crash
                print(f"\n\n{Colors.RED}[!] Termination signal caught. Type 'exit' to quit safely.{Colors.RESET}")
                time.sleep(2)
if __name__ == "__main__":
    terminal = PwnTerminal()
    terminal.start_shell()
