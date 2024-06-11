# Required Libraries - You can change the browser driver if you would like to. More details on GitHub.
from seleniumbase import Driver  # type: ignore
import configparser
import json

# Read config file
config = configparser.ConfigParser(interpolation=None)
config.read("config.ini")

if "browser" not in config["settings"]:
    config["settings"]["browser"] = "chrome"
browser = config["settings"]["browser"]

# Start the driver
if browser == "brave" or browser == "opera":
    # If the binary_location is not set in the config file, warn the user
    if (
        "binary_location" not in config["settings"]
        or config["settings"]["binary_location"] == ""
    ):
        print(
            "Please set the binary_location in the config file for Brave or Opera browser."
        )
        exit()
    driver = Driver(
        uc=True, browser="chrome", binary_location=config["settings"]["binary_location"]
    )
else:
    driver = Driver(uc=True, browser=browser)
driver.implicitly_wait(6)


trackers_list = json.loads(config["wanted-trackers"]["trackers"])

# For each tracker in the config file, run the tracker class
for tracker in trackers_list:
    try:
        tracker_class_name = "trackers." + tracker.lower()
        tracker_class = getattr(
            __import__(tracker_class_name, fromlist=[tracker]),
            tracker.capitalize().replace("-", "") + "Tracker",
        )
    except ModuleNotFoundError:
        print(f"Tracker {tracker} does not exist.")
        continue

    # Create an instance of the tracker class and run it
    tracker_instance = tracker_class(driver, config)
    tracker_instance.run()

driver.quit()

# GitHub: https://github.com/KlevGG/TrackerScreenshot
