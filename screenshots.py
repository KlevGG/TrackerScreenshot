# Required Libraries - You can change the browser driver if you would like to. More details on GitHub.
from seleniumbase import Driver, SB  # type: ignore
from selenium.webdriver.common.by import By
from Screenshot import Screenshot  # type: ignore
import datetime
import configparser

# Read config file
config = configparser.ConfigParser(interpolation=None)
config.read("config.ini")

browser = config["settings"]["browser"]

# Start the driver
if browser == "brave" or browser == "opera":
    driver = Driver(
        uc=True, browser="chrome", binary_location=config["settings"]["binary_location"]
    )
else:
    driver = Driver(uc=True, browser=browser)
driver.implicitly_wait(6)

ob = Screenshot.Screenshot()


def take_screenshot(tracker_name, driver=driver, is_load_at_runtime=False):
    date_string = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    image_name = tracker_name + "_" + date_string + ".png"

    if config["settings"]["full_page_screenshot"] == "true":
        ob.full_screenshot(
            driver,
            save_path="screenshots",
            image_name=image_name,
            is_load_at_runtime=is_load_at_runtime,
        )
    else:
        driver.save_screenshot("screenshots/" + image_name)


if "ATH" in config["wanted-trackers"]["trackers"]:
    print("Entering Aither.")
    # Get the details from the config file
    username = config["aither"]["username"]
    password = config["aither"]["password"]
    profile_url = config["aither"]["profile_url"]

    driver.get(profile_url)

    # Navigation - DO NOT CHANGE
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Login and save screenshot
    driver.find_element(By.ID, "login-button").click()
    take_screenshot("Aither")
    print("Aither Screenshoted")


if "RF" in config["wanted-trackers"]["trackers"]:
    print("Entering Reelflix.")
    # Get the details from the config file
    username = config["reelflix"]["username"]
    password = config["reelflix"]["password"]
    profile_url = config["reelflix"]["profile_url"]

    driver.get(profile_url)

    # Navigation
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Login and save screenshot
    driver.find_element(By.ID, "login-button").click()
    take_screenshot("RF")
    print("Reelflix Screenshoted")


if "LST" in config["wanted-trackers"]["trackers"]:
    print("Entering LST.")
    username = config["lst"]["username"]
    password = config["lst"]["password"]
    profile_url = config["lst"]["profile_url"]

    driver.get(profile_url)

    # Navigation
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Login and save screenshot
    driver.find_element(By.ID, "login-button").click()
    take_screenshot("LST")
    print("LST Screenshoted")

if "BLU" in config["wanted-trackers"]["trackers"]:
    print("Entering BLU.")
    username = config["blutopia"]["username"]
    password = config["blutopia"]["password"]
    profile_url = config["blutopia"]["profile_url"]

    driver.get(profile_url)

    # Navigation
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Login and save screenshot
    driver.find_element(By.CLASS_NAME, "auth-form__primary-button").click()

    # 2FA is enabled, ask for the code
    if driver.find_elements(By.ID, "code"):
        code = input("Please enter the 2FA code: ")
        code_field = driver.find_element(By.ID, "code")
        code_field.send_keys(code)

    take_screenshot("BLU")
    print("Blu Screenshoted")

if "HUNO" in config["wanted-trackers"]["trackers"]:
    print("Entering HUNO.")
    username = config["huno"]["username"]
    password = config["huno"]["password"]
    profile_url = config["huno"]["profile_url"]
    skip = False

    driver.get(profile_url)

    if driver.find_elements(By.ID, "challenge-running"):
        print(
            "Please solve the challenge and press enter to continue or type 'n' and press enter to skip."
        )
        response = input()
        if response == "n":
            skip = True

    if not skip:
        # Navigation
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")

        # Send username and password
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Login and save screenshot
        driver.find_element(By.ID, "login-button").click()

        # 2FA is enabled, ask for the code
        if driver.find_elements(By.ID, "v_input"):
            code = input("Please enter the 2FA code: ")
            code_field = driver.find_element(By.ID, "v_input")
            code_field.send_keys(code)
            driver.find_element(By.ID, "submit_verification").click()

        # is_load_at_runtime is set to ensure the full page screenshot is taken correctly
        if config["settings"]["full_page_screenshot"] == "true":
            take_screenshot("HUNO", is_load_at_runtime=True)
        else:
            take_screenshot("HUNO")
        print("HUNO Screenshoted")

if "SP" in config["wanted-trackers"]["trackers"]:
    print("Entering Speedapp.")
    username = config["speedapp"]["username"]
    password = config["speedapp"]["password"]
    profile_url = config["speedapp"]["profile_url"]

    driver.get(profile_url)

    # Navigation - Login
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Login and screenshot
    driver.find_element(By.TAG_NAME, "button").click()

    take_screenshot("SP")
    print("Speedapp Screenshoted")

if "FL" in config["wanted-trackers"]["trackers"]:
    print("Entering Filelist.")
    username = config["filelist"]["username"]
    password = config["filelist"]["password"]
    profile_url = config["filelist"]["profile_url"]

    driver.get(profile_url)

    # Navigation - Login
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Login and screenshot
    driver.find_element(By.CLASS_NAME, "btn").click()

    take_screenshot("FL")
    print("Filelist Screenshoted")


if "GPW" in config["wanted-trackers"]["trackers"]:
    print("Entering GreatPosterWall.")
    username = config["greatposterwall"]["username"]
    password = config["greatposterwall"]["password"]
    profile_url = config["greatposterwall"]["profile_url"]

    driver.get(profile_url)

    # Navigation - Login
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Login and save screenshot
    driver.find_element(By.CLASS_NAME, "Button").click()

    take_screenshot("GPW")
    print("GPW Screenshoted")


###THE FOLLOWING ARE TESTED BY THE COMMUNITY###

if "JME" in config["wanted-trackers"]["trackers"]:
    print("Entering JME.")
    username = config["jme"]["username"]
    password = config["jme"]["password"]
    profile_url = config["jme"]["profile_url"]

    driver.get(
        "https://jme-reunit3d.de/login"
    )  # DO NOT CHANGE THIS, JME requires an extra step for login

    # Navigation - DO NOT CHANGE
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Login and save screenshot
    driver.find_element(By.ID, "login-button").click()

    driver.get(profile_url)

    take_screenshot("JME")
    print("JME-REUNIT3D Screenshoted")


if "ANT" in config["wanted-trackers"]["trackers"]:
    print("Entering AnimeTorrents.")
    username = config["animetorrents"]["username"]
    password = config["animetorrents"]["password"]
    profile_url = config["animetorrents"]["profile_url"]

    driver.get("https://animetorrents.me/login.php")  # DO NOT CHANGE

    # Navigation - Login
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Login
    driver.find_element(By.ID, "login-element-6").click()

    # Load profile and screenshot
    driver.get(profile_url)

    take_screenshot("ANT")
    print("ANT Screenshoted")


if "RED" in config["wanted-trackers"]["trackers"]:
    print("Entering Redacted.")
    username = config["redacted"]["username"]
    password = config["redacted"]["password"]
    profile_url = config["redacted"]["profile_url"]
    driver.get(
        "https://redacted.ch/login.php"
    )  # Keep the link as it is, DO NOT CHANGE.

    # Navigation - Login
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    twofa_field = driver.find_element(By.NAME, "qrcode_confirm")

    # Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # 2FA, ask for the code
    code = input(
        "Please enter the 2FA code: (If you don't have 2FA, just press enter.) "
    )
    twofa_field.send_keys(code)

    # Login
    driver.find_element(By.CLASS_NAME, "submit").click()

    # Load profile and screenshot
    driver.get(profile_url)

    take_screenshot("RED")
    print("RED Screenshoted")


if "STC" in config["wanted-trackers"]["trackers"]:
    print("Entering SkipTheCommericals.")
    username = config["skipthecommercials"]["username"]
    password = config["skipthecommercials"]["password"]
    profile_url = config["skipthecommercials"]["profile_url"]

    driver.get(profile_url)

    # Navigation - DO NOT CHANGE
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Login and save screenshot
    driver.find_element(By.ID, "login-button").click()

    take_screenshot("STC")
    print("SkipTheCommericals Screenshoted")


if "STT" in config["wanted-trackers"]["trackers"]:
    print("Entering SkipTheTrailers.")
    username = config["skipthetrailers"]["username"]
    password = config["skipthetrailers"]["password"]
    profile_url = config["skipthetrailers"]["profile_url"]

    driver.get(profile_url)

    # Navigation - DO NOT CHANGE
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Login and save screenshot
    driver.find_element(By.ID, "login-button").click()

    take_screenshot("STT")
    print("SkipTheTrailers Screenshoted")

if "AB" in config["wanted-trackers"]["trackers"]:
    print("Entering AnimeBytes")
    username = config["animebytes"]["username"]
    password = config["animebytes"]["password"]
    profile_url = config["animebytes"]["profile_url"]

    driver.get(
        "https://animebytes.tv/user.php"
    )  # Keep the link as it is, DO NOT CHANGE.

    # Navigation - Login
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Login
    driver.find_element(By.CLASS_NAME, "submit").click()

    # Load profile and screenshot
    driver.get(profile_url)  # Add your profile link

    take_screenshot("AB")
    print("AnimeBytes Screenshoted")

if "TDC" in config["wanted-trackers"]["trackers"]:
    print("Entering TheDarkCommunity")
    username = config["thedarkcommunity"]["username"]
    password = config["thedarkcommunity"]["password"]
    profile_url = config["thedarkcommunity"]["profile_url"]

    driver.get(profile_url)

    # Navigation
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Login and save screenshot
    driver.find_element(By.ID, "login-button").click()

    take_screenshot("TDC")
    print("TDC Screenshoted")


if "CRT" in config["wanted-trackers"]["trackers"]:
    print("Entering Cathode-Ray.tube")
    username = config["cathode-raytube"]["username"]
    password = config["cathode-raytube"]["password"]
    profile_url = config["cathode-raytube"]["profile_url"]

    driver.get(
        "https://www.cathode-ray.tube/login"
    )  # Keep the link as it is, DO NOT CHANGE.

    # Navigation - Login
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Login
    driver.find_element(By.ID, "login_button").click()

    # 2FA is enabled, ask for the code
    if driver.find_elements(By.NAME, "code"):
        code = input("Please enter the 2FA code: ")
        code_field = driver.find_element(By.NAME, "code")
        code_field.send_keys(code)
        driver.find_element(By.ID, "login_button").click()

    # Load profile and screenshot
    driver.get(profile_url)

    # Hide passkey
    try:
        passkey_li = driver.find_element(By.XPATH, "//li[contains(text(), 'Passkey')]")
        driver.execute_script("arguments[0].style.display = 'none';", passkey_li)
    except:  # noqa: E722
        pass

    take_screenshot("CRT")
    print("CRT Screenshoted")

if "MAM" in config["wanted-trackers"]["trackers"]:
    print("Entering myanonamouse")
    username = config["myanonamouse"]["username"]
    password = config["myanonamouse"]["password"]
    profile_url = config["myanonamouse"]["profile_url"]

    driver.get(profile_url)

    # Navigation
    username_field = driver.find_element(By.NAME, "email")
    password_field = driver.find_element(By.NAME, "password")

    # Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Login and save screenshot
    driver.find_element(By.CLASS_NAME, "btn").click()

    take_screenshot("MAM")
    print("myanonamouse Screenshoted")

if "NBL" in config["wanted-trackers"]["trackers"]:
    print("Entering Nebulance")
    username = config["nebulance"]["username"]
    password = config["nebulance"]["password"]
    profile_url = config["nebulance"]["profile_url"]

    driver.get(profile_url)

    # Navigation
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Login and save screenshot
    driver.find_element(By.NAME, "login").click()

    take_screenshot("NBL")
    print("Nebulance Screenshoted")

if "TL" in config["wanted-trackers"]["trackers"]:
    print("Entering TorrentLeech")
    username = config["torrentleech"]["username"]
    password = config["torrentleech"]["password"]
    profile_url = config["torrentleech"]["profile_url"]

    driver.get(profile_url)

    # Navigation - Login
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Login and save screenshot
    driver.find_element(By.CLASS_NAME, "btn").click()

    take_screenshot("TL")
    print("TorrentLeech Screenshoted")

if "OPS" in config["wanted-trackers"]["trackers"]:
    print("Entering Orpheus")
    username = config["orpheus"]["username"]
    password = config["orpheus"]["password"]
    profile_url = config["orpheus"]["profile_url"]
    driver.get(
        "https://orpheus.network/login.php"
    )  # Keep the link as it is, DO NOT CHANGE.

    # Navigation - Login
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    twofa_field = driver.find_element(By.NAME, "twofa")

    # Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # 2FA, ask for the code
    code = input(
        "Please enter the 2FA code: (If you don't have 2FA, just press enter.) "
    )
    twofa_field.send_keys(code)

    # Login
    driver.find_element(By.CLASS_NAME, "submit").click()

    # Load profile and screenshot
    driver.get(profile_url)  # Add your profile link

    take_screenshot("OPS")
    print("OPS Screenshoted")

if "SZN" in config["wanted-trackers"]["trackers"]:
    print("Entering Swarmazon")
    username = config["swarmazon"]["username"]
    password = config["swarmazon"]["password"]
    profile_url = config["swarmazon"]["profile_url"]

    driver.get("https://swarmazon.club/en/account/login.php")

    # Navigation - Login
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Login
    driver.find_element(By.CLASS_NAME, "btn").click()

    # Load profile and screenshot
    driver.get(profile_url)  # Keep as-is

    take_screenshot("Swarmazon")
    print("Swarmazon Screenshoted")

if "MTV" in config["wanted-trackers"]["trackers"]:
    print("Entering MoreThanTV")
    username = config["morethantv"]["username"]
    password = config["morethantv"]["password"]
    profile_url = config["morethantv"]["profile_url"]

    driver.get(profile_url)

    # Navigation - DO NOT CHANGE
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)
    driver.find_element(By.ID, "login_button").click()

    # 2FA is enabled, ask for the code
    if driver.find_elements(By.NAME, "code"):
        code = input("Please enter the 2FA code: ")
        code_field = driver.find_element(By.NAME, "code")
        code_field.send_keys(code)
        driver.find_element(By.ID, "login_button").click()

    # Hide passkey
    try:
        passkey_li = driver.find_element(By.XPATH, "//li[contains(text(), 'Passkey')]")
        driver.execute_script("arguments[0].style.display = 'none';", passkey_li)
    except:  # noqa: E722
        pass

    # Login and save screenshot
    take_screenshot("MoreThanTV")
    print("MoreThanTV Screenshoted")

if "HDT" in config["wanted-trackers"]["trackers"]:
    print("Entering HD-Torrents")
    username = config["hdtorrents"]["username"]
    password = config["hdtorrents"]["password"]
    profile_url = config["hdtorrents"]["profile_url"]

    driver.get("https://hd-torrents.org")  # Keep the link as it is, DO NOT CHANGE.

    # Navigation - Login
    username_field = driver.find_element(By.NAME, "uid")
    password_field = driver.find_element(By.NAME, "pwd")

    # Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Login
    driver.find_element(
        By.XPATH,
        "/html/body/div[3]/table/tbody/tr/td/form/table/tbody/tr/td[1]/table/tbody/tr/td[5]/input",
    ).click()

    # Load profile and screenshot
    driver.get(profile_url)  # Add your profile link

    take_screenshot("HDT")
    print("HDT Screenshoted")

if "BTN" in config["wanted-trackers"]["trackers"]:
    with SB(uc=True, locale_code="en") as sb:
        print("Entering BroadcasTheNet")
        username = config["broadcasthenet"]["username"]
        password = config["broadcasthenet"]["password"]
        profile_url = config["broadcasthenet"]["profile_url"]

        sb.driver.uc_open_with_reconnect(profile_url, 1)

        # Navigation - DO NOT CHANGE
        username_field = "input[id='username']"
        password_field = "input[id='password']"
        login_button = "input[name='login']"

        # Send username and password
        sb.type(username_field, username)
        sb.type(password_field, password)
        sb.driver.reconnect(0.1)
        sb.driver.uc_click(login_button, reconnect_time=4)
        sb.wait_for_text_not_visible("Checking", timeout=10)

        # 2FA is enabled, ask for the code
        if sb.driver.find_elements(By.ID, "code"):
            code = input("Please enter the 2FA code: ")
            code_field = "input[id='code']"
            sb.type(code_field, code)
            submit_button = "input[type='submit']"
            sb.driver.uc_click(submit_button, reconnect_time=4)

        sb.driver.get(profile_url)

        info_button = "a[href='#section2']"
        sb.driver.uc_click(info_button, reconnect_time=4)
        # Login and save screenshot
        take_screenshot("BroadcasTheNet", sb.driver)
        print("BroadcasTheNet Screenshoted")

if "GGN" in config["wanted-trackers"]["trackers"]:
    print("Entering GazelleGames")
    username = config["gazellegames"]["username"]
    password = config["gazellegames"]["password"]
    profile_url = config["gazellegames"]["profile_url"]

    driver.get(profile_url)

    # Navigation - DO NOT CHANGE
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    twofa_field = driver.find_element(By.NAME, "authkey")

    print(
        "Manually solve the captcha image. Press enter when done. (If you use 2FA then press enter after you type the code below)"
    )
    code = input()

    # Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)
    twofa_field.send_keys(code)

    driver.find_element(By.CLASS_NAME, "submit").click()

    # Login and save screenshot
    take_screenshot("GazelleGames")
    print("GazelleGames Screenshoted")

if "PTP" in config["wanted-trackers"]["trackers"]:
    print("Entering PassThePopcorn")
    username = config["passthepopcorn"]["username"]
    password = config["passthepopcorn"]["password"]
    profile_url = config["passthepopcorn"]["profile_url"]

    driver.get(profile_url)

    # Navigation - DO NOT CHANGE
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    driver.find_element(By.ID, "login-button").click()
    print("Manually solve the captcha image. Press enter when done.")
    code = input()
    driver.find_element(By.ID, "login-button").click()

    # 2FA is enabled, ask for the code
    if driver.find_elements(By.ID, "tfa-code"):
        code = input("Please enter the 2FA code: ")
        code_field = driver.find_element(By.ID, "tfa-code")
        code_field.send_keys(code)
        verify_button = driver.find_element(By.CSS_SELECTOR, "input[value='Verify']")
        verify_button.click()

    # is_load_at_runtime is set to ensure the full page screenshot is taken correctly
    if config["settings"]["full_page_screenshot"] == "true":
        take_screenshot("PassThePopcorn", is_load_at_runtime=True)
    else:
        take_screenshot("PassThePopcorn")
    print("PassThePopcorn Screenshoted")

if "BHD" in config["wanted-trackers"]["trackers"]:
    print("Entering BeyondHD")
    username = config["beyond-hd"]["username"]
    password = config["beyond-hd"]["password"]
    profile_url = config["beyond-hd"]["profile_url"]

    driver.get(profile_url)

    # Navigation - DO NOT CHANGE
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    print("Manually solve the captcha. Press enter when done.")
    code = input()
    # Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    driver.find_element(By.ID, "login-button").click()

    # 2FA is enabled, ask for the code
    if driver.find_elements(By.ID, "code"):
        code = input("Please enter the 2FA code: ")
        code_field = driver.find_element(By.ID, "code")
        code_field.send_keys(code)
        driver.find_element(By.ID, "login-button").click()

    driver.get(profile_url)
    # Login and save screenshot
    take_screenshot("BeyondHD")
    print("BeyondHD Screenshoted")

else:
    driver.quit()

driver.quit()


# GitHub: https://github.com/KlevGG/TrackerScreenshot
