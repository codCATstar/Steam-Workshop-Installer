SteamCMD Workshop Downloader

A fully-featu<img width="1917" height="1006" alt="Screenshot 2026-01-30 123354" src="https://github.com/user-attachments/assets/99935010-efa1-4bd9-ad3a-2effd24f550c" />
<img width="697" height="849" alt="Screenshot 2026-01-30 121413" src="https://github.com/user-attachments/assets/f31d4b39-9177-4d91-b34f-0c050b161f5e" />
red GUI tool for downloading Steam Workshop mods using SteamCMD.

This app allows you to easily download mods for any game using its Steam App ID and Workshop IDs, with support for dependencies, drag & drop, mod naming, and live terminal output.

Features

Dark Mode UI – easy on the eyes for long download sessions.

Drag & Drop Workshop IDs – quickly add multiple Workshop items.

Mod Naming – downloaded mods are automatically renamed to their Steam Workshop name.

Dependency Detection – optional checkbox to download required dependencies.

Game Presets – save Game IDs for quick access later.

Embedded Terminal Output – see SteamCMD logs live inside the program.

Overall Progress Bar – shows total download progress across all mods.

Download Button Above Terminal – clean layout for easy access.

Auto-Tiles to Left Half of Screen – convenient multitasking layout.

Installation

Download or clone this repository:

git clone https://github.com/yourusername/steamcmd-workshop-downloader.git


Ensure you have Python 3.10+ installed.

Install required dependencies:

pip install requests tkinterdnd2


The program will also automatically download SteamCMD if not present.

Usage

Open the program:

python steamcmd_workshop_gui.py


Enter your Game App ID.

Add one or more Workshop IDs (one per line, or drag & drop from browser).

Check Download Dependencies if needed.

Click Download Mods.

The mods will be downloaded to:

steamcmd/steamapps/workshop/content/<GameID>/


Each mod folder is automatically renamed to the Steam Workshop name.

Saving Game IDs

When you download a game for the first time, you’ll be prompted to save the Game ID with a custom name. Saved games appear in the dropdown for future use.

Building an Executable

To create a Windows .exe:

python -m PyInstaller --onefile --windowed --icon=steamcmd_icon.ico steamcmd_workshop_gui.py


--onefile → single executable

--windowed → GUI only, no console

--icon → path to your .ico file

The compiled executable will be in the dist/ folder.

License

This project is released under the MIT License.
You may use, modify, and distribute freely.
