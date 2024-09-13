# Required Libraries - You can change the browser driver if you would like to. More details on GitHub.
import configparser
import json
import os
from getpass import getpass

from argon2 import PasswordHasher
from seleniumbase import Driver

from utils import encrypt_secrets, get_decrypted_secrets  # type: ignore

# Read config file
config = configparser.ConfigParser(interpolation=None)
config.read("config.ini")

if "auto_2fa" in config["settings"] and config["settings"]["auto_2fa"] == "true":
    ph = PasswordHasher()
    # Check if master password is stored in config file
    if "master_password" not in config["settings"]:
        # Prompt the user to enter the master password
        print("Master password not found in config file, please enter it.")
        master_password = getpass("")
        # Hash the master password
        master_password_hash = ph.hash(master_password)
        salt = os.urandom(16)
        # Store the master password hash in the config file
        config["settings"]["master_password"] = master_password_hash
        config["settings"]["salt"] = salt.hex()
        with open("config.ini", "w") as configfile:
            config.write(configfile)

    twofa_trackers = [
        "blutopia",
        "huno",
        "redacted",
        "broadcasthenet",
        "gazellegames",
        "passthepopcorn",
        "beyond-hd",
        "oldtoons",
        "cathode-raytube",
        "morethantv",
        "orpheus",
        "torrentleech",
    ]

    # Decrypt the secrets
    decrypted_secrets = get_decrypted_secrets()

    # Prompt for any missing 2FA secrets
    for tracker in twofa_trackers:
        if tracker not in decrypted_secrets:
            decrypted_secrets[tracker] = input(
                f"Please enter the 2FA secret for {tracker}: "
            )

    # Write the secrets to the secrets file
    secrets_config = configparser.ConfigParser()
    secrets_config.read("secrets.ini")

    # Encrypt the secrets and write them to the secrets file
    encrypted_secrets = encrypt_secrets(decrypted_secrets)
    secrets_config["secrets"] = encrypted_secrets
    with open("secrets.ini", "w") as secretsfile:
        secrets_config.write(secretsfile)


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
