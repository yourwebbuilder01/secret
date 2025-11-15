# BOGH Secret Notepad 🔐

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![Encryption](https://img.shields.io/badge/Encryption-AES--128-green)
![Security](https://img.shields.io/badge/Security-Password%20Protected-red)

**Your personal encrypted note-taking system with military-grade security**

---

## 🚀 Quick Start

### Installation (30 seconds)
```bash
# 1. Install required package
pip install pycryptodome psutil

# 2. Download the script
# Save as 'secret_notepad.py'

# 3. Run it!
python secret_notepad.py
```

### First Use
1. **Default Password:** `123`
2. **Change it immediately** for security!
3. **Notes are encrypted** and saved to your Desktop

---

## 🎯 What is This?

BOGH Secret Notepad is a secure, encrypted note-taking system that protects your private thoughts, passwords, and sensitive information with:

- **🔒 AES-128 Encryption** - Military-grade security
- **🕵️ Hacker-Style Interface** - Cool typing effects
- **🔐 Password Protection** - Multiple login attempts
- **💾 Local Storage** - No cloud, no internet needed
- **🚫 Complete Privacy** - Your data never leaves your computer

---

## ⚙️ Easy Personalization

### Change Password (IMPORTANT!)
**Find this line in the code:**
```python
PASSWORD = "123"  # Simple password
```
**Change it to:**
```python
PASSWORD = "YourSuperSecurePassword123!"  # Your new password
```

### Change Encryption Key
**Find this line:**
```python
ENCRYPTION_KEY = b'yourwebbu1lder12'
```
**Change it to any 16-character key:**
```python
ENCRYPTION_KEY = b'MySecretKey12345!'  # Must be 16 characters
```

### Change Notes Location
**Find this line:**
```python
NOTES_FOLDER = os.path.join(os.path.expanduser('~'), 'Desktop', 'MySecretNotes')
```
**Change to:**
```python
NOTES_FOLDER = os.path.join(os.path.expanduser('~'), 'Documents', 'SecretVault')
```

---

## 🎮 How to Use

### Creating Notes
1. Select `[1] CREATE NEW NOTE`
2. Enter a title
3. Type your content (multiple lines supported)
4. Type `SAVE` on a new line to finish
5. **Auto-encrypted** and saved instantly

### Viewing Notes
1. Select `[2] VIEW ALL NOTES`
2. Choose a note number
3. **Automatically decrypted** for viewing
4. Options: Modify, Delete, or Return

### Example Session:
```
[CREATE NEW NOTE]
Title: My Secret Project
Content: This is my super secret plan...
        More confidential information...
        SAVE
[SUCCESS] Note encrypted and saved!
```

---

## 🔧 Customization Options

### Change Typing Speed
**Find this function:**
```python
def hacker_print(text, delay=0.003):
```
**Adjust the delay:**
- `0.001` = Very fast
- `0.005` = Slow and dramatic
- `0.01` = Very slow

### Modify Menu Colors
The interface uses simple text - you can easily change the ASCII art and borders to match your style.

### Add Categories
Want to organize notes by category? Add this to the note creation:
```python
# Add category selection
categories = ["Personal", "Work", "Ideas", "Passwords"]
# Let user choose or auto-detect from title
```

---

## 🛡️ Security Features

### What Makes It Secure?
- **AES-128 Encryption** - Same technology banks use
- **Local Storage** - No cloud syncing, no third parties
- **Password Protection** - 3 attempts then locks
- **File Encryption** - Notes are unreadable without the program
- **No Backdoors** - You control everything

### File Structure
```
Desktop/
└── MySecretNotes/
    ├── project_ideas.txt          # Encrypted
    ├── passwords.txt              # Encrypted  
    └── personal_thoughts.txt      # Encrypted
```

**Each file contains:**
- Plain text header (title, date)
- **ENCRYPTED_CONTENT_START** section
- Base64 encoded encrypted data
- **ENCRYPTED_CONTENT_END** section

---

## ❓ Frequently Asked Questions

### 🔒 Security Questions
**Q: Is my data really secure?**  
A: Yes! Uses AES-128 encryption - the same standard used by governments and banks.

**Q: What if I forget my password?**  
A: There's no password recovery. This is a security feature. **Change the default password but don't forget it!**

**Q: Can someone decrypt my files without the password?**  
A: Extremely unlikely without the encryption key and password.

### 🛠️ Technical Questions
**Q: Where are my notes stored?**  
A: In `Desktop/MySecretNotes/` - you can change this location.

**Q: Can I use it on multiple computers?**  
A: Yes! Copy the script and your Notes folder to any computer with Python.

**Q: How do I backup my notes?**  
A: Simply copy the `MySecretNotes` folder to a USB drive or cloud storage.

### 🎨 Customization Questions
**Q: Can I change the interface?**  
A: Absolutely! The code is well-structured and easy to modify.

**Q: Can I add more features?**  
A: Yes! The modular design makes it easy to add new functionality.

---

## 🚨 Important Security Notice

### ✅ **What You MUST Do:**
1. **Change the default password** from `123`
2. **Change the encryption key** from the default
3. **Backup your Notes folder** regularly
4. **Keep the script secure** - it contains your encryption key

### ❌ **What to Avoid:**
- Don't use simple passwords
- Don't share the script with your encryption key
- Don't store the script and notes on public computers
- Don't forget your password (no recovery option)

---

## 🔄 Import/Export Features

### Export Notes to Plain Text
Add this function to export decrypted notes:
```python
def export_notes():
    """Export all notes to a readable text file"""
    # You can easily add this feature!
    pass
```

### Import from Other Apps
The simple file structure makes it easy to import notes from other applications.

---

## 🐛 Troubleshooting

### Common Issues:
**"ModuleNotFoundError: No module named 'Crypto'"**
```bash
pip uninstall crypto pycryptodome
pip install pycryptodome
```

**"Access denied" to Notes folder**
- Run as Administrator or change NOTES_FOLDER location

**Notes not saving**
- Make sure you type `SAVE` on its own line
- Check disk space

**Forgot password**
- You'll need to modify the script to reset it
- Or restore from backup

---

## 💡 Pro Tips

### For Maximum Security:
1. Use the script on a encrypted drive
2. Change passwords monthly
3. Store backups in multiple secure locations
4. Use a password manager for your BOGH password

### For Convenience:
1. Create a desktop shortcut
2. Use consistent naming for notes
3. Export important notes to secure cloud storage
4. Use categories in note titles (e.g., "[Work] Project X")

---

## 📞 Support & Customization

**Need help? Want custom features?**
- Check the code comments - it's well-documented
- Modify the script to fit your needs
- The structure makes adding features easy

---

## 🎯 Ready to Secure Your Notes?

```bash
# 1. Install dependencies
pip install pycryptodome psutil

# 2. Run the notepad
python secret_notepad.py

# 3. Change the password immediately!
```

**Default Login:**
- 🔑 **Password:** `123`
- 📁 **Storage:** `Desktop/MySecretNotes/`

---

*Your thoughts deserve protection. Keep them secure with BOGH.* 🔐
