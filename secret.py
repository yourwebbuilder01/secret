import os
import getpass
import time
import platform
import socket
import psutil
from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import webbrowser

NOTES_FOLDER = os.path.join(os.path.expanduser('~'), 'Desktop', 'MySecretNotes')
PASSWORD = "123"
ENCRYPTION_KEY = b'yourwebbu1lder12'

def hacker_print(text, delay=0.003):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def setup():
    if not os.path.exists(NOTES_FOLDER):
        os.makedirs(NOTES_FOLDER)

def check_password():
    hacker_print("\n[ACCESS] Authentication required...")
    
    attempts = 3
    while attempts > 0:
        input_pass = getpass.getpass(f"[SECURITY] Password ({attempts} attempts): ")
        
        if input_pass == PASSWORD:
            hacker_print("[SUCCESS] Access granted!")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                hacker_print(f"[ERROR] Wrong password. {attempts} attempts left.")
    
    hacker_print("[LOCKDOWN] Access denied!")
    return False

def encrypt_data(data):
    try:
        iv = get_random_bytes(16)
        cipher = AES.new(ENCRYPTION_KEY, AES.MODE_CFB, iv=iv)
        encrypted_data = cipher.encrypt(data.encode('utf-8'))
        combined = iv + encrypted_data
        return base64.b64encode(combined).decode('utf-8')
    except Exception as e:
        hacker_print(f"[ENCRYPTION ERROR] {e}")
        return None

def decrypt_data(encrypted_data_b64):
    try:
        combined = base64.b64decode(encrypted_data_b64.encode('utf-8'))
        iv = combined[:16]
        encrypted_data = combined[16:]
        cipher = AES.new(ENCRYPTION_KEY, AES.MODE_CFB, iv=iv)
        decrypted_data = cipher.decrypt(encrypted_data)
        return decrypted_data.decode('utf-8')
    except Exception:
        return None

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("┌" + "─" * 50 + "┐")
    hacker_print("│                ██████╗  ██████╗  ██████╗ ██╗  ██╗     │")
    hacker_print("│                ██╔══██╗██╔═══██╗██╔════╝ ██║  ██║     │")
    hacker_print("│                ██████╔╝██║   ██║██║  ███╗███████║     │")
    hacker_print("│                ██╔══██╗██║   ██║██║   ██║██╔══██║     │")
    hacker_print("│                ██████╔╝╚██████╔╝╚██████╔╝██║  ██║     │")
    hacker_print("│                ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝     │")
    print("├" + "─" * 50 + "┤")
    hacker_print("│               SECRET NOTES SYSTEM             │")
    print("├" + "─" * 50 + "┤")
    
    note_count = 0
    if os.path.exists(NOTES_FOLDER):
        note_count = len([f for f in os.listdir(NOTES_FOLDER) if f.endswith('.txt')])
    
    hacker_print(f"│ Total Notes: {note_count}                              │")
    print("├" + "─" * 50 + "┤")
    hacker_print("│ [1] CREATE NEW NOTE                          │")
    hacker_print("│ [2] VIEW ALL NOTES                           │")
    hacker_print("│ [3] SYSTEM ANALYSIS                          │")
    hacker_print("│ [4] ABOUT AUTHOR                             │")
    hacker_print("│ [5] EXIT                                     │")
    print("└" + "─" * 50 + "┘")
    
    choice = input("\n[INPUT] Select operation: ").strip()
    return choice

def get_user_input():
    print("\n[EDITOR] Begin transmission (type SAVE to finish):")
    print("─" * 50)
    
    lines = []
    while True:
        try:
            line = input()
            if line.upper() == "SAVE":
                break
            lines.append(line)
        except KeyboardInterrupt:
            print("\n\n[ABORT] Transmission cancelled.")
            return None
    
    return "\n".join(lines) if lines else None

def create_note():
    print("\n" + "─" * 50)
    hacker_print("[CREATE NEW NOTE]")
    
    note_name = input("[INPUT] Note title: ").strip()
    if not note_name:
        hacker_print("[ERROR] Title required!")
        input("Press Enter to continue...")
        return
    
    safe_name = "".join(c for c in note_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
    safe_name = safe_name.replace(' ', '_')
    file_path = os.path.join(NOTES_FOLDER, f"{safe_name}.txt")
    
    content = get_user_input()
    
    if content and content.strip():
        encrypted_content = encrypt_data(content)
        if encrypted_content:
            full_content = f"NOTE: {note_name}\nCreated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n─" + "─" * 40 + f"\nENCRYPTED_CONTENT_START\n{encrypted_content}\nENCRYPTED_CONTENT_END\n─" + "─" * 40
        else:
            full_content = f"NOTE: {note_name}\nCreated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n─" + "─" * 40 + f"\n{content}\n─" + "─" * 40
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        hacker_print(f"[SUCCESS] Note '{note_name}' encrypted!")
    else:
        hacker_print("[ERROR] Null data rejected!")
    
    input("Press Enter to continue...")

def view_notes():
    if not os.path.exists(NOTES_FOLDER):
        hacker_print("[INFO] No encrypted data found.")
        input("Press Enter to continue...")
        return
    
    notes = [f for f in os.listdir(NOTES_FOLDER) if f.endswith('.txt')]
    
    if not notes:
        hacker_print("[INFO] No encrypted data found.")
        input("Press Enter to continue...")
        return
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("┌" + "─" * 50 + "┐")
        hacker_print("│               ENCRYPTED DATA VAULT            │")
        print("├" + "─" * 50 + "┤")
        
        for i, note in enumerate(notes, 1):
            note_name = note[:-4].replace('_', ' ')
            print(f"│ {i:2d}. {note_name:<42} │")
        
        print("├" + "─" * 50 + "┤")
        hacker_print("│ [1-{0}] DECRYPT  [D] DELETE  [B] BACK      │".format(len(notes)))
        print("└" + "─" * 50 + "┘")
        
        choice = input("\n[INPUT] Select operation: ").strip().upper()
        
        if choice == 'B':
            break
        elif choice == 'D':
            note_num = input("[INPUT] Note number to delete: ").strip()
            if note_num.isdigit() and 1 <= int(note_num) <= len(notes):
                note_index = int(note_num) - 1
                note_name = notes[note_index][:-4].replace('_', ' ')
                confirm = input(f"[CONFIRM] Delete '{note_name}'? (y/n): ").lower()
                if confirm == 'y':
                    os.remove(os.path.join(NOTES_FOLDER, notes[note_index]))
                    hacker_print(f"[SUCCESS] '{note_name}' purged!")
                    notes = [f for f in os.listdir(NOTES_FOLDER) if f.endswith('.txt')]
                    if not notes:
                        break
            else:
                hacker_print("[ERROR] Invalid input!")
        elif choice.isdigit() and 1 <= int(choice) <= len(notes):
            note_index = int(choice) - 1
            open_note(notes[note_index])
            notes = [f for f in os.listdir(NOTES_FOLDER) if f.endswith('.txt')]
            if not notes:
                break
        else:
            hacker_print("[ERROR] Invalid command!")
        
        input("Press Enter to continue...")

def open_note(note_file):
    file_path = os.path.join(NOTES_FOLDER, note_file)
    note_name = note_file[:-4].replace('_', ' ')
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("┌" + "─" * 50 + "┐")
        hacker_print(f"│             DECRYPTED: {note_name:<25} │")
        print("├" + "─" * 50 + "┤")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if "ENCRYPTED_CONTENT_START" in content and "ENCRYPTED_CONTENT_END" in content:
                start_idx = content.find("ENCRYPTED_CONTENT_START") + len("ENCRYPTED_CONTENT_START\n")
                end_idx = content.find("ENCRYPTED_CONTENT_END")
                encrypted_content = content[start_idx:end_idx].strip()
                
                decrypted_content = decrypt_data(encrypted_content)
                if decrypted_content:
                    display_content = content[:content.find("ENCRYPTED_CONTENT_START")] + decrypted_content + content[content.find("ENCRYPTED_CONTENT_END") + len("ENCRYPTED_CONTENT_END"):]
                    print(display_content)
                else:
                    print(content)
            else:
                print(content)
                
        except Exception as e:
            hacker_print(f"[ERROR] Could not read note: {e}")
        
        print("├" + "─" * 50 + "┤")
        hacker_print("│ [1] MODIFY  [2] PURGE  [3] RETURN        │")
        print("└" + "─" * 50 + "┘")
        
        choice = input("\n[INPUT] Select operation: ").strip()
        
        if choice == '1':
            edit_note(file_path, note_name)
            break
        elif choice == '2':
            confirm = input("[CONFIRM] Purge this data? (y/n): ").lower()
            if confirm == 'y':
                os.remove(file_path)
                hacker_print("[SUCCESS] Data purged!")
                return True
        elif choice == '3':
            break
        
        input("Press Enter to continue...")

def edit_note(file_path, note_name):
    hacker_print(f"\n[MODIFYING: {note_name}]")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            current_content = f.read()
        
        if "ENCRYPTED_CONTENT_START" in current_content and "ENCRYPTED_CONTENT_END" in current_content:
            start_idx = current_content.find("ENCRYPTED_CONTENT_START") + len("ENCRYPTED_CONTENT_START\n")
            end_idx = current_content.find("ENCRYPTED_CONTENT_END")
            encrypted_content = current_content[start_idx:end_idx].strip()
            decrypted_content = decrypt_data(encrypted_content)
            if decrypted_content:
                current_display_content = decrypted_content
            else:
                current_display_content = "[ENCRYPTED CONTENT - DECRYPTION FAILED]"
        else:
            lines = current_content.split('\n')
            if '─' * 40 in lines:
                sep_index = lines.index('─' * 40)
                content_lines = lines[sep_index + 1:len(lines) - 2]
                current_display_content = '\n'.join(content_lines)
            else:
                current_display_content = current_content
        
        hacker_print("[CURRENT DATA STREAM]")
        print("─" * 50)
        print(current_display_content)
        print("─" * 50)
    except:
        pass
    
    hacker_print("[INPUT NEW DATA STREAM]")
    content = get_user_input()
    
    if content and content.strip():
        encrypted_content = encrypt_data(content)
        if encrypted_content:
            new_content = f"NOTE: {note_name}\nCreated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n─" + "─" * 40 + f"\nENCRYPTED_CONTENT_START\n{encrypted_content}\nENCRYPTED_CONTENT_END\n─" + "─" * 40
        else:
            new_content = f"NOTE: {note_name}\nCreated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n─" + "─" * 40 + f"\n{content}\n─" + "─" * 40
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        hacker_print("[SUCCESS] Data stream updated!")
    else:
        hacker_print("[ERROR] Null stream rejected!")
    
    input("Press Enter to continue...")

def get_system_info():
    try:
        system_info = {
            'os': f"{platform.system()} {platform.release()}",
            'version': platform.version(),
            'machine': platform.machine(),
            'processor': platform.processor(),
            'hostname': socket.gethostname(),
            'username': os.getlogin()
        }
        
        memory = psutil.virtual_memory()
        system_info['memory_total'] = f"{memory.total // (1024**3)} GB"
        system_info['memory_used'] = f"{memory.used // (1024**3)} GB"
        system_info['memory_percent'] = f"{memory.percent}%"
        
        disk = psutil.disk_usage('/')
        system_info['disk_total'] = f"{disk.total // (1024**3)} GB"
        system_info['disk_used'] = f"{disk.used // (1024**3)} GB"
        system_info['disk_free'] = f"{disk.free // (1024**3)} GB"
        system_info['disk_percent'] = f"{disk.percent}%"
        
        system_info['cpu_cores'] = psutil.cpu_count(logical=False)
        system_info['cpu_threads'] = psutil.cpu_count(logical=True)
        system_info['cpu_usage'] = f"{psutil.cpu_percent(interval=1)}%"
        
        boot_time = datetime.fromtimestamp(psutil.boot_time())
        system_info['boot_time'] = boot_time.strftime("%Y-%m-%d %H:%M:%S")
        
        return system_info
    except Exception as e:
        hacker_print(f"[ERROR] System analysis failed: {e}")
        return None

def system_analysis():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("┌" + "─" * 50 + "┐")
    hacker_print("│               SYSTEM ANALYSIS               │")
    print("├" + "─" * 50 + "┤")
    
    system_info = get_system_info()
    
    if system_info:
        hacker_print("│ SYSTEM INFORMATION                      │")
        hacker_print(f"│ OS: {system_info['os']:<40} │")
        hacker_print(f"│ Version: {system_info['version']:<35} │")
        hacker_print(f"│ Machine: {system_info['machine']:<36} │")
        hacker_print(f"│ Hostname: {system_info['hostname']:<35} │")
        hacker_print(f"│ User: {system_info['username']:<39} │")
        
        print("├" + "─" * 50 + "┤")
        hacker_print("│ MEMORY & STORAGE                        │")
        hacker_print(f"│ RAM: {system_info['memory_used']}/{system_info['memory_total']} ({system_info['memory_percent']}) │")
        hacker_print(f"│ Disk: {system_info['disk_used']}/{system_info['disk_total']} ({system_info['disk_percent']}) │")
        hacker_print(f"│ Free Space: {system_info['disk_free']:<33} │")
        
        print("├" + "─" * 50 + "┤")
        hacker_print("│ PROCESSOR                               │")
        hacker_print(f"│ Cores: {system_info['cpu_cores']} Threads: {system_info['cpu_threads']:<24} │")
        hacker_print(f"│ Usage: {system_info['cpu_usage']:<38} │")
        hacker_print(f"│ Boot Time: {system_info['boot_time']:<32} │")
    
    note_count = 0
    total_size = 0
    if os.path.exists(NOTES_FOLDER):
        notes = [f for f in os.listdir(NOTES_FOLDER) if f.endswith('.txt')]
        note_count = len(notes)
        for note in notes:
            file_path = os.path.join(NOTES_FOLDER, note)
            total_size += os.path.getsize(file_path)
    
    print("├" + "─" * 50 + "┤")
    hacker_print("│ SECRET NOTES STATUS                       │")
    hacker_print(f"│ Encrypted Files: {note_count:<30} │")
    hacker_print(f"│ Storage Used: {total_size} bytes{' ' * (18 - len(str(total_size)))}│")
    hacker_print(f"│ Data Vault: Desktop/MySecretNotes{' ' * 8}│")
    hacker_print(f"│ Security Level: MAXIMUM{' ' * 25}│")
    
    print("├" + "─" * 50 + "┤")
    hacker_print("│ [1] Refresh Analysis                      │")
    hacker_print("│ [2] Return to Terminal                    │")
    print("└" + "─" * 50 + "┘")
    
    choice = input("\n[INPUT] Select operation: ").strip()
    
    if choice == '1':
        system_analysis()

def about_author():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("┌" + "─" * 50 + "┐")
        hacker_print("│                 ABOUT AUTHOR                │")
        print("├" + "─" * 50 + "┤")
        hacker_print("│                                              │")
        hacker_print("│           ██████╗  ██████╗  ██████╗ ██╗  ██╗│")
        hacker_print("│           ██╔══██╗██╔═══██╗██╔════╝ ██║  ██║│")
        hacker_print("│           ██████╔╝██║   ██║██║  ███╗███████║│")
        hacker_print("│           ██╔══██╗██║   ██║██║   ██║██╔══██║│")
        hacker_print("│           ██████╔╝╚██████╔╝╚██████╔╝██║  ██║│")
        hacker_print("│           ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝│")
        hacker_print("│                                              │")
        print("├" + "─" * 50 + "┤")
        hacker_print("│           SECRET NOTES SYSTEM v2.0          │")
        hacker_print("│           Created by: yourwebbu1lder        │")
        print("├" + "─" * 50 + "┤")
        hacker_print("│ [1] GitHub: github.com/yourwebbu1lder       │")
        hacker_print("│ [2] Instagram: @yourwebbu1lder              │")
        print("├" + "─" * 50 + "┤")
        hacker_print("│ [3] Return to Main Menu                     │")
        print("└" + "─" * 50 + "┘")
        
        choice = input("\n[INPUT] Select option: ").strip()
        
        if choice == '1':
            hacker_print("[SYSTEM] Opening GitHub profile...")
            webbrowser.open("https://github.com/yourwebbu1lder")
            time.sleep(1)
        elif choice == '2':
            hacker_print("[SYSTEM] Opening Instagram profile...")
            webbrowser.open("https://instagram.com/yourwebbu1lder")
            time.sleep(1)
        elif choice == '3':
            break
        else:
            hacker_print("[ERROR] Invalid option!")
            input("Press Enter to continue...")

def main():
    setup()
    
    if not check_password():
        return
    
    while True:
        choice = main_menu()
        
        if choice == '1':
            create_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            system_analysis()
        elif choice == '4':
            about_author()
        elif choice == '5':
            hacker_print("\n[SYSTEM] Securing connection...")
            time.sleep(1)
            hacker_print("[EXIT] System shutdown complete.")
            break
        else:
            hacker_print("[ERROR] Invalid command!")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
