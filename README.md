# BedwarsScoreboard
## Info
BedwarsScoreboard is a Python program that reads Minecraft chat logs and outputs Hypixel bedwars kills, deaths, bed breaks, and types of the former to a Pandas dataframe. It's compatible with all versions of Minecraft and all Minecraft clients that output chat logs similar to those output by the vanilla Minecraft client.

## How to Use
1. Download and extract the included BedwarsScoreboard files.
2. Make sure you have Python 3.9.5 installed. It can be installed at https://www.python.org/downloads/release/python-395/.
3. Using pip, install the pandas module. This can be done by running `pip install pandas` in the terminal. Note that you may need to run a different command such as `py -m pip install pandas` instead.
4. Configure the main.py program. This includes entering your logpath and username.
5. Launch Minecraft and join the Hypixel network. Configure the mode and team member usernames based on what gamemode of Bedwars you want to play and who is in it.
6. Run main.py.

## Version 1.0
This version is functional, however it requires manual input of player usernames and does not output to any sort of web server or image file, so it's largely unusable at the moment, and is more of a baseline for future versions.

## TO-DO:
 • Code/find mod that allows for the exporting of player usernames to chat/other logs
 
 • Integrate exported player usernames into the program
 
 • Create and polish scoreboard design
 
 • Use either Google Slides or the Pillow library to update the scoreboard live from the program
 
 • Output finished image to file/web server in order to use it as an overlay in OBS
