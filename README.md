# TrackerScreenshot
Automatically create screenshots of your stats and save it as PNG, as who got the time to take screenshots manually? 


## Supported Trackers:
    - Aither (ATH)
    - Bluetopia (BLU)
    - Reelflix (RF)
    - Speedapp (SP)
    - Filelist (FL)
    - Hawke-Uno (HUNO)
    - LST (LST)

It's easy to add new trackers. You can request it here or add it yourself. 
    

##  Setup

**To use the script, you need to have Python and PIP. Latest versions are recommended.**

The script uses Chrome Webdriver, therefore, you need to have Chrome installed. 

- Install `pip install selenium` and `pip install webdriver-manager`
- Create a folder with a name of your choice. Example: "screenshots-bot". 
- Download "screenshots.py" into the folder by cloning or downloading manually. 
- Edit `screenshots.py` with your details as instructed below. It's recommended to edit with Notepad++. 
- run `python screenshots.py` in the terminal.
- Screenshots will be generated for each tracker with the date and time.


## Editing The Script 

### Steps
- Remove unwanted trackers by renaming or deleting them from the trackers array. 
- Add your profile link to the tracker you would like to use in `driver.get()`. 
- Add your username on `username.name_keys()` and your password on `password.name_keys()`. 
- Make sure to repeat the steps above for each tracker you would like to screenshot. 


This script was tested on two Windows 10 machines. 
