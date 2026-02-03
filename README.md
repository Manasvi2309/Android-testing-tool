# Android-testing-tool
This is my Android testing tool
# 🔐 Android ADB Testing Tool (Python)

A Python-based Android testing and reconnaissance tool using **ADB**.
Designed for **Android pentesting, security research, and debugging**.

> Platform: Linux  
> Language: Python 3  
> Backend: ADB (Android Debug Bridge)

---

## ✨ Features

- Check connected Android devices
- List installed applications
- View app permissions
- Get APK path
- Pull APK for reverse engineering
- List exported activities & receivers
- Check running processes
- View logcat logs
- Check open ports
- View device, battery & hardware info
- Check SELinux status
- Take screenshots
- Get app version & SDK details

---

## 🧠 Use Cases

- Android application pentesting
- Reconnaissance & information gathering
- Reverse engineering support (jadx)
- Debugging & PoC creation
- Security research

---

## 🛠 Requirements

- Linux OS
- Python 3.x
- ADB installed

### Install ADB
```bash
sudo apt install android-tools-adb

📲 Device Setup

Enable Developer Options

Enable USB Debugging

Connect device and authorize ADB

Check connection:

adb devices


▶️ Usage
chmod +x android.py
python3 android.py
