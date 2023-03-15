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

The script runs on Chrome Webdriver, therefore, you need to have Chrome installed. If you prefer Edge, refer to the end of the readme to do changes.  

- Create a folder with a name of your choice. Example: "screenshots-bot". 
- Clone or download the library into the folder.
- Run `pip install -r requirements.txt` to install required libraries. 
- Edit `screenshots.py` with your details as instructed below. It's recommended to edit with Notepad++. 
- Run `python screenshots.py` in the terminal.
- Screenshots will be generated for each tracker with the date and time.


## Editing The Script 

### Steps
- Remove unwanted trackers by renaming or deleting them from the trackers array. 
- Add your profile link to the tracker you would like to use in `driver.get()`. 
- Add your username on `username.name_keys()` and your password on `password.name_keys()`. 
- Make sure to repeat the steps above for each tracker you would like to screenshot. 
- (Optional) If you want to take full-screen screeshots, uncomment line 15: `driver.maximize_window()`


## Use Edge Instead of Chrome

If you like to run it using Edge, you need to do the following changes. Before editing, we recommend using Chrome. 
- Remove line 3 and 4: `from selenium.webdriver.chrome.options import Options` - `from webdriver_manager.chrome import ChromeDriverManager`. 
- Add the following instead: `from selenium.webdriver.edge.service import Service as EdgeService` and `from webdriver_manager.microsoft import EdgeChromiumDriverManager`
- Remove line 10 and 11: `options = Options()` - `options.headless = False`. 
- Remove line 14: `driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)`
- Replace it with `driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))`.

This script was tested on two Windows 10 machines. 
