# TrackerScreenshot
Automatically create screenshots of your stats and save it as PNG, as who got the time to take screenshots manually? Currently it supports over 20 trackers and takes minutes to setup!


## Supported Trackers:
    - Aither (ATH)
    - Bluetopia (BLU)
    - Reelflix (RF)
    - Speedapp (SP)
    - Filelist (FL)
    - Hawke-Uno (HUNO)
    - LST (LST)
    - GreatPosterWall (GPW)
    - AnimeTorrents (ANT)
    - Redacted (RED)
    - SkipTheCommericals (STC)
    - SkipTheTrailers (STT)
    - AnimeBytes (AB)
    - JME-ReUnit3D (JME)
    - TheDarkCommunity (TDC)
    - Cathode-Ray.tube (CRT)
    - MyAnonaMouse (MAM)
    - Nebulance (NBL)
    - TorrentLeech (TL)
    - Orpheus (OPS)
    - Swarmazon (SZN)
    - MoreThanTV (MTV)
    - HD-Torrents (HDT)
    - BroadcasTheNet (BTN)
    - GazelleGames (GGN)
    - PassThePopcorn (PTP)
    - BeyondHD (BHD)


It's easy to add new trackers. You can request it here or add it yourself.

##  Setup

**To use the script, you need to have Python and PIP. Latest versions are recommended.**

The script runs on Chrome Webdriver, therefore, you need to have Chrome installed. If you prefer Edge, refer to the end of the readme to do changes.

- Create a folder with a name of your choice. Example: "screenshots-bot".
- Clone or download the library into the folder.
- Run `pip install -r requirements.txt` to install required libraries.
- Copy `config.ini.example` to `config.ini` and edit with your details as instructed below. It's recommended to edit with [Notepad++](https://notepad-plus-plus.org/).
- Run `python screenshots.py` in the terminal.
- Screenshots will be generated for each tracker with the date and time.


## Editing The Script

### Steps
- You only need to edit `config.ini`.
- Remove unwanted trackers by renaming or deleting them from the trackers array.
- Add your username, password, and profile link.
- Make sure to repeat the steps above for each tracker you would like to screenshot.
- If you want to take full-page screenshots, change the `full_page_screenshot` option to `true`. This will make use of [Selenium_Screenshot](https://github.com/PyWizards/Selenium_Screenshot) which scrolls the page and takes a screenshot of the entire page.


## Use a different browser

Before editing, we recommend using Chrome. To change simply update browser in the `config.ini` file.
Options are: `chrome`, `firefox`, `edge`, `safari`

`[settings]
browser = chrome`

*This script was tested on Windows and Debian.*


<sub>Special thanks to FluxVelocorapotor and allegedlyundead for adding new trackers!</sub>
