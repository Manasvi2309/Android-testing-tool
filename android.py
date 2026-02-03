#!/usr/bin/env python3
"""
Advanced Android ADB Testing Tool
Author: Security Researcher
Platform: Linux
"""

import os
import subprocess


def run_cmd(cmd):
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL)
        return output.decode()
    except subprocess.CalledProcessError:
        return "[!] Command failed or no output"


def check_device():
    result = run_cmd("adb devices")
    return "device\n" in result


# -------- BASIC OPTIONS --------

def list_apps():
    print(run_cmd("adb shell pm list packages"))


def app_permissions():
    pkg = input("Package name: ")
    print(run_cmd(f"adb shell dumpsys package {pkg} | grep permission"))


def app_path():
    pkg = input("Package name: ")
    print(run_cmd(f"adb shell pm path {pkg}"))


def running_processes():
    print(run_cmd("adb shell ps"))


def battery_device_info():
    print("\n[Device Info]")
    print(run_cmd("adb shell getprop | grep product"))
    print("\n[Battery Info]")
    print(run_cmd("adb shell dumpsys battery"))


def view_logcat():
    print("[CTRL+C to stop]")
    os.system("adb logcat")


# -------- ADVANCED SECURITY OPTIONS --------

def pull_apk():
    pkg = input("Package name: ")
    path = run_cmd(f"adb shell pm path {pkg}").strip()
    if "package:" in path:
        apk_path = path.replace("package:", "")
        os.system(f"adb pull {apk_path}")
        print("[+] APK pulled successfully")
    else:
        print("[-] Unable to find APK path")


def exported_activities():
    pkg = input("Package name: ")
    print(run_cmd(f"adb shell dumpsys package {pkg} | grep exported"))


def exported_receivers():
    pkg = input("Package name: ")
    print(run_cmd(f"adb shell dumpsys package {pkg} | grep receiver"))


def open_ports():
    print(run_cmd("adb shell netstat -tulnp"))


def selinux_status():
    print(run_cmd("adb shell getenforce"))


def hardware_info():
    print(run_cmd("adb shell cat /proc/cpuinfo"))


def screen_info():
    print(run_cmd("adb shell wm size"))
    print(run_cmd("adb shell wm density"))


def take_screenshot():
    os.system("adb shell screencap /sdcard/screen.png")
    os.system("adb pull /sdcard/screen.png")
    print("[+] Screenshot saved")


def app_version_info():
    pkg = input("Package name: ")
    print(run_cmd(f"adb shell dumpsys package {pkg} | grep version"))


# -------- MENU --------

def menu():
    print("""
=============================
 Advanced Android ADB Tool
=============================
 1. List installed apps
 2. App permissions
 3. App path
 4. Running processes
 5. Battery & device info
 6. View logcat
 7. Pull APK
 8. Exported activities
 9. Exported receivers
10. Check open ports
11. SELinux status
12. Hardware info
13. Screen info
14. Take screenshot
15. App version info
 0. Exit
""")


def main():
    if not check_device():
        print("[-] No Android device connected")
        return

    while True:
        menu()
        choice = input("Select option: ")

        actions = {
            "1": list_apps,
            "2": app_permissions,
            "3": app_path,
            "4": running_processes,
            "5": battery_device_info,
            "6": view_logcat,
            "7": pull_apk,
            "8": exported_activities,
            "9": exported_receivers,
            "10": open_ports,
            "11": selinux_status,
            "12": hardware_info,
            "13": screen_info,
            "14": take_screenshot,
            "15": app_version_info
        }

        if choice == "0":
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("[-] Invalid option")


if __name__ == "__main__":
    main()


