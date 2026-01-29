import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os
import zipfile
import time
import sys

# -----------------------------
# Check/install requests
# -----------------------------
try:
    import requests
except ImportError:
    # Show info popup about admin
    root = tk.Tk()
    root.withdraw()  # hide main window
    messagebox.showinfo(
        "Info",
        "Admin rights are only needed if pip requires them to install the 'requests' module.\n\nThe program will attempt to install it now."
    )
    # Try installing requests
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests  # import again after install
    root.destroy()

# -----------------------------
# SteamCMD setup
# -----------------------------
STEAMCMD_URL = "https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip"
STEAMCMD_FOLDER = "steamcmd"
STEAMCMD_EXE = os.path.join(STEAMCMD_FOLDER, "steamcmd.exe")


def download_steamcmd(progress):
    if os.path.exists(STEAMCMD_EXE):
        return

    os.makedirs(STEAMCMD_FOLDER, exist_ok=True)

    zip_path = "steamcmd.zip"

    r = requests.get(STEAMCMD_URL, stream=True)
    total = int(r.headers.get("content-length", 0))
    downloaded = 0

    with open(zip_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
                downloaded += len(chunk)
                percent = int((downloaded / total) * 100)
                progress["value"] = percent
                root.update_idletasks()

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(STEAMCMD_FOLDER)

    os.remove(zip_path)


def run():
    game_id = game_entry.get().strip()
    workshop_ids = workshop_entry.get("1.0", tk.END).strip().split()

    if not game_id or not workshop_ids:
        messagebox.showerror("Error", "Enter Game ID and Workshop IDs")
        return

    status_label.config(text="Downloading SteamCMD...")
    download_steamcmd(progress)

    status_label.config(text="Starting workshop downloads...")

    cmd = f'"{STEAMCMD_EXE}" +login anonymous '

    for wid in workshop_ids:
        cmd += f'+workshop_download_item {game_id} {wid} '

    cmd += "+quit"

    subprocess.Popen(cmd, shell=True)

    status_label.config(text="Done! Opening download folder...")

    # Wait a few seconds to ensure folders exist
    time.sleep(2)

    # Open SteamCMD workshop folder
    download_path = os.path.join(STEAMCMD_FOLDER, "steamapps", "workshop", "content", game_id)
    os.makedirs(download_path, exist_ok=True)
    os.startfile(download_path)


# -----------------------------
#GUI
# -----------------------------
root = tk.Tk()
root.title("SteamCMD Workshop Downloader")
root.geometry("450x350")

tk.Label(root, text="Game App ID").pack()
game_entry = tk.Entry(root)
game_entry.pack(fill="x", padx=10)

tk.Label(root, text="Workshop IDs (one per line)").pack()
workshop_entry = tk.Text(root, height=10)
workshop_entry.pack(fill="both", padx=10)

progress = ttk.Progressbar(root, length=300)
progress.pack(pady=5)

status_label = tk.Label(root, text="")
status_label.pack()

tk.Button(root, text="Download Mods", command=run).pack(pady=10)

root.mainloop()
