# 🛠️ GHL1TCH FRAMEWORK — CLI Core Engine v1.5

A multi-functional **Command Line Interface (CLI)** Python framework optimized for desktop Linux (**Arch Linux / EndeavourOS**) and mobile environments (**Termux on Android**), designed for local network auditing and admin automation.

---

## ⚡ Core Features & Commands

*   📊 **`fastfetch` / `info`:** Displays custom branding, session statistics, real-time diagnostics, battery levels, and active parameters.
*   🖥️ **`edit <filename>`:** A full-screen TUI text editor powered by `curses` with buffer saving (`Ctrl + G`).
*   🌐 **`netscan` & `portscan <target_ip>`:** Local network topology parsing via ARP tables and high-speed multi-threaded port auditing.
*   📡 **`ssh` / `shell` / `wifi` / `bt`:** Native integrations for secure shell connections, OS execution, and hardware controls.
*   🎣 **Simulations:** Includes educational modules like `phishing` and a full-screen Matrix cascade (`hackshow`).
*   ⚙️ **Utilities:** Theme customization (`color`), screen clearing (`clear`), and session closure (`exit`).

---

## 🔒 Zero-Trust Security Architecture

Protected via a hybrid two-factor authentication (2FA) mechanism:
1.  **SHA-256 Hashing:** No plaintext credentials or developer emails are stored in the codebase.
2.  **`config.ini` Perimeter:** Local device storage only for runtime configurations and SMTP/IMAP credentials.
3.  **TLS/SSL 2FA Challenge:** Generates and dispatches a unique 6-digit session token to Gmail upon initialization; the shell unlocks only after verification.

---

## 🛠️ Installation & Setup

1.  **Dependencies (Arch/Termux):** Install standard packages (`net-tools`, `openssh`, `git`).
2.  **Clone Repo:** `git clone https://github.com`
3.  **Virtual Environment:** Initialize and activate Python virtual environment.
4.  **Configuration:** Create a local `config.ini` file with your Gmail App Password credentials.

Run the core engine using `python3 main2.py`.
