# Required Libraries - You can change the browser driver if you would like to. More details on GitHub.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import datetime
import time
import configparser

# Read config file
config = configparser.ConfigParser(interpolation=None)
config.read('config.ini')

# Headless or with Header. Some websites do not work as headless so it's recommended to keep it commented.
options = Options()
# options.add_argument("--headless=new")

# Install the driver
ChromeDriverManager().install()

# Start the driver
driver = webdriver.Chrome(options=options)
#driver.maximize_window()  #Uncomment for full-screen screenshots

if "ATH" in config['wanted-trackers']['trackers']:
    print("Entering Aither.")
    #Get the details from the config file
    username = config['aither']['username']
    password = config['aither']['password']
    profile_url = config['aither']['profile_url']

    driver.get(profile_url)
    time.sleep(3) #wait 3 seconds to make sure the page loads

    #Navigation - DO NOT CHANGE
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    #Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    #Login and save screenshot
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("screenshots/Aither_"+ datastring +".png")
    print("Aither Screenshoted")


if "RF" in config['wanted-trackers']['trackers']:
    print("Entering Reelflix.")
    #Get the details from the config file
    username = config['reelflix']['username']
    password = config['reelflix']['password']
    profile_url = config['reelflix']['profile_url']

    driver.get(profile_url)
    time.sleep(3) #wait 3 seconds to make sure the page loads

    #Navigation
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    #Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    #Login and save screenshot
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("screenshots/RF_"+ datastring +".png")
    print("Reelflix Screenshoted")


if "LST" in config['wanted-trackers']['trackers']:
    print("Entering LST.")
    username = config['lst']['username']
    password = config['lst']['password']
    profile_url = config['lst']['profile_url']

    driver.get(profile_url)
    time.sleep(3) #wait 3 seconds to make sure the page loads

    #Navigation
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    #Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    #Login and save screenshot
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("screenshots/LST_"+ datastring +".png")
    print("LST Screenshoted")

if "BLU" in config['wanted-trackers']['trackers']:
    print("Entering BLU.")
    username = config['blutopia']['username']
    password = config['blutopia']['password']
    profile_url = config['blutopia']['profile_url']

    driver.get(profile_url)
    time.sleep(3) #wait 3 seconds to make sure the page loads

    #Navigation
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    #Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    #Login and save screenshot
    driver.find_element(By.CLASS_NAME, "auth-form__primary-button").click()

    #2FA is enabled, ask for the code
    if driver.find_elements(By.ID, "code"):
        code = input("Please enter the 2FA code: ")
        code_field = driver.find_element(By.ID, "code")
        code_field.send_keys(code)

    time.sleep(3)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("screenshots/BLU_"+ datastring +".png")
    print("Blu Screenshoted")

if "HUNO" in config['wanted-trackers']['trackers']:
    print("Entering BLU.")
    username = config['huno']['username']
    password = config['huno']['password']
    profile_url = config['huno']['profile_url']
    skip = False

    driver.get(profile_url)
    time.sleep(3) #wait 3 seconds to make sure the page loads

    if driver.find_elements(By.ID, "challenge-running"):
        print("Please solve the challenge and press enter to continue or type 'n' and press enter to skip.")
        response = input()
        if response == "n":
            skip = True

    if not skip:
        #Navigation
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")

        #Send username and password
        username_field.send_keys(username)
        password_field.send_keys(password)

        #Login and save screenshot
        driver.find_element(By.ID, "login-button").click()
        time.sleep(3)

        #2FA is enabled, ask for the code
        if driver.find_elements(By.ID, "v_input"):
            code = input("Please enter the 2FA code: ")
            code_field = driver.find_element(By.ID, "v_input")
            code_field.send_keys(code)
            driver.find_element(By.ID, "submit_verification").click()
            time.sleep(3)
        datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        driver.save_screenshot("screenshots/HUNO_"+ datastring +".png")
        print("HUNO Screenshoted")

if "SP" in config['wanted-trackers']['trackers']:
    print("Entering Speedapp.")
    username = config['speedapp']['username']
    password = config['speedapp']['password']
    profile_url = config['speedapp']['profile_url']

    driver.get(profile_url)
    time.sleep(3)

    #Navigation - Login
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    #Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    #Login and screenshot
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(3)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("screenshots/SP_"+ datastring +".png")
    print("Speedapp Screenshoted")

if "FL" in config['wanted-trackers']['trackers']:
    print("Entering Filelist.")
    username = config['filelist']['username']
    password = config['filelist']['password']
    profile_url = config['filelist']['profile_url']

    driver.get(profile_url)
    time.sleep(3)

    #Navigation - Login
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    #Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    #Login and screenshot
    driver.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(3)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("screenshots/FL_"+ datastring +".png")
    print("Filelist Screenshoted")


if "GPW" in config['wanted-trackers']['trackers']:
    print("Entering GreatPosterWall.")
    username = config['greatposterwall']['username']
    password = config['greatposterwall']['password']
    profile_url = config['greatposterwall']['profile_url']

    driver.get(profile_url)
    time.sleep(3)

    #Navigation - Login
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    #Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    #Login and save screenshot
    driver.find_element(By.CLASS_NAME, "Button").click()
    time.sleep(3)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("screenshots/GPW_"+ datastring +".png")
    print("GPW Screenshoted")


###THE FOLLOWING ARE TESTED BY THE COMMUNITY###

if "JME" in config['wanted-trackers']['trackers']:
    print("Entering JME.")
    username = config['jme']['username']
    password = config['jme']['password']
    profile_url = config['jme']['profile_url']

    driver.get('https://jme-reunit3d.de/login') #DO NOT CHANGE THIS, JME requires an extra step for login
    time.sleep(3) #wait 3 seconds to make sure the page loads

    #Navigation - DO NOT CHANGE
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    #Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    #Login and save screenshot
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    driver.get(profile_url)
    time.sleep(2)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("screenshots/JME_"+ datastring +".png")
    print("JME-REUNIT3D Screenshoted")


if "ANT" in config['wanted-trackers']['trackers']:
    print("Entering AnimeTorrents.")
    username = config['animetorrents']['username']
    password = config['animetorrents']['password']
    profile_url = config['animetorrents']['profile_url']

    driver.get('https://animetorrents.me/login.php') #DO NOT CHANGE
    time.sleep(3)

    #Navigation - Login
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    #Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    #Login
    driver.find_element(By.ID, "login-element-6").click()
    time.sleep(2)

    #Load profile and screenshot
    driver.get(profile_url)
    time.sleep(2)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("screenshots/ANT_"+ datastring +".png")
    print("ANT Screenshoted")


if "RED" in config['wanted-trackers']['trackers']:
    print("Entering Redacted.")
    username = config['redacted']['username']
    password = config['redacted']['password']
    profile_url = config['redacted']['profile_url']
    driver.get('https://redacted.ch/login.php') #Keep the link as it is, DO NOT CHANGE.
    time.sleep(3)

    #Navigation - Login
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    #Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    #Login
    driver.find_element(By.CLASS_NAME, "submit").click()
    time.sleep(2)

    #Load profile and screenshot
    driver.get(profile_url)
    time.sleep(2)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("screenshots/RED_"+ datastring +".png")
    print("RED Screenshoted")


if "STC" in config['wanted-trackers']['trackers']:
    print("Entering SkipTheCommericals.")
    username = config['skipthecommercials']['username']
    password = config['skipthecommercials']['password']
    profile_url = config['skipthecommercials']['profile_url']

    driver.get(profile_url)
    time.sleep(3) #wait 3 seconds to make sure the page loads

    #Navigation - DO NOT CHANGE
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    #Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    #Login and save screenshot
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("screenshots/STC_"+ datastring +".png")
    print("SkipTheCommericals Screenshoted")


if "STT" in config['wanted-trackers']['trackers']:
    print("Entering SkipTheTrailers.")
    username = config['skipthetrailers']['username']
    password = config['skipthetrailers']['password']
    profile_url = config['skipthetrailers']['profile_url']

    driver.get(profile_url)
    time.sleep(3) #wait 3 seconds to make sure the page loads

    #Navigation - DO NOT CHANGE
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    #Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    #Login and save screenshot
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("screenshots/STT_"+ datastring +".png")
    print("SkipTheTrailers Screenshoted")

if "AB" in config['wanted-trackers']['trackers']:
    print("Entering AnimeBytes")
    username = config['animebytes']['username']
    password = config['animebytes']['password']
    profile_url = config['animebytes']['profile_url']

    driver.get('https://animebytes.tv/user.php') #Keep the link as it is, DO NOT CHANGE.
    time.sleep(3)

    #Navigation - Login
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    #Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    #Login
    driver.find_element(By.CLASS_NAME, "submit").click()
    time.sleep(2)

    #Load profile and screenshot
    driver.get(profile_url) #Add your profile link
    time.sleep(3)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("screenshots/AB_"+ datastring +".png")
    print("AnimeBytes Screenshoted")

if "TDC" in config['wanted-trackers']['trackers']:
    print("Entering TheDarkCommunity")
    username = config['thedarkcommunity']['username']
    password = config['thedarkcommunity']['password']
    profile_url = config['thedarkcommunity']['profile_url']

    driver.get(profile_url)
    time.sleep(3)

    #Navigation
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    #Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    #Login and save screenshot
    driver.find_element(By.ID, "login-button").click()
    time.sleep(4)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("screenshots/TDC_"+ datastring +".png")
    print("TDC Screenshoted")


if "CRT" in config['wanted-trackers']['trackers']:
    print("Entering Cathode-Ray.tube")
    username = config['cathode-raytube']['username']
    password = config['cathode-raytube']['password']
    profile_url = config['cathode-raytube']['profile_url']

    driver.get('https://www.cathode-ray.tube/login') #Keep the link as it is, DO NOT CHANGE.
    time.sleep(3)

    #Navigation - Login
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    #Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    #Login
    driver.find_element(By.ID, "login_button").click()
    time.sleep(2)

    #Load profile and screenshot
    driver.get(profile_url)
    time.sleep(2)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("screenshots/CRT_"+ datastring +".png")
    print("CRT Screenshoted")

if "MAM" in config['wanted-trackers']['trackers']:
    print("Entering myanonamouse")
    username = config['myanonamouse']['username']
    password = config['myanonamouse']['password']
    profile_url = config['myanonamouse']['profile_url']

    driver.get(profile_url)
    time.sleep(3)

    #Navigation
    username_field = driver.find_element(By.NAME, "email")
    password_field = driver.find_element(By.NAME, "password")

    #Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    #Login and save screenshot
    driver.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(4)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("screenshots/MAM_"+ datastring +".png")
    print("myanonamouse Screenshoted")

if "NBL" in config['wanted-trackers']['trackers']:
    print("Entering Nebulance")
    username = config['nebulance']['username']
    password = config['nebulance']['password']
    profile_url = config['nebulance']['profile_url']

    driver.get(profile_url)
    time.sleep(3)

    #Navigation
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    #Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    #Login and save screenshot
    driver.find_element(By.NAME, "login").click()
    time.sleep(4)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("screenshots/NBL_"+ datastring +".png")
    print("Nebulance Screenshoted")

if "TL" in config['wanted-trackers']['trackers']:
    print("Entering TorrentLeech")
    username = config['torrentleech']['username']
    password = config['torrentleech']['password']
    profile_url = config['torrentleech']['profile_url']

    driver.get(profile_url)
    time.sleep(3)

    #Navigation - Login
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    #Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    #Login and save screenshot
    driver.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(4)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("screenshots/TL_"+ datastring +".png")
    print("TorrentLeech Screenshoted")

if "OPS" in config['wanted-trackers']['trackers']:
    print("Entering Orpheus")
    username = config['orpheus']['username']
    password = config['orpheus']['password']
    profile_url = config['orpheus']['profile_url']
    driver.get('https://orpheus.network/login.php') #Keep the link as it is, DO NOT CHANGE.
    time.sleep(3)

    #Navigation - Login
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    twofa_field = driver.find_element(By.NAME, "twofa")

    #Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    #2FA, ask for the code
    code = input("Please enter the 2FA code: (If you don't have 2FA, just press enter.) ")
    twofa_field.send_keys(code)

    #Login
    driver.find_element(By.CLASS_NAME, "submit").click()
    time.sleep(2)

    #Load profile and screenshot
    driver.get(profile_url) #Add your profile link
    time.sleep(2)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("screenshots/OPS_"+ datastring +".png")
    print("OPS Screenshoted")

if "SZN" in config['wanted-trackers']['trackers']:
    print("Entering Swarmazon")
    username = config['swarmazon']['username']
    password = config['swarmazon']['password']
    profile_url = config['swarmazon']['profile_url']

    driver.get('https://swarmazon.club/en/account/login.php')
    time.sleep(3)

    #Navigation - Login
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    #Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    #Login
    driver.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(2)

    #Load profile and screenshot
    driver.get(profile_url) #Keep as-is
    time.sleep(2)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("screenshots/Swarmazon_"+ datastring +".png")
    print("Swarmazon Screenshoted")

if "MTV" in config['wanted-trackers']['trackers']:
    print("Entering MoreThanTV")
    username = config['morethantv']['username']
    password = config['morethantv']['password']
    profile_url = config['morethantv']['profile_url']

    driver.get(profile_url)
    time.sleep(3) #wait 3 seconds to make sure the page loads

    #Navigation - DO NOT CHANGE
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    #Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    #Login and save screenshot
    driver.find_element(By.ID, "login_button").click()
    time.sleep(4)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("screenshots/MoreThanTV_"+ datastring +".png")
    print("MoreThanTV Screenshoted")

if "HDT" in config['wanted-trackers']['trackers']:
    print("Entering HD-Torrents")
    username = config['hdtorrents']['username']
    password = config['hdtorrents']['password']
    profile_url = config['hdtorrents']['profile_url']

    driver.get('https://hd-torrents.org') #Keep the link as it is, DO NOT CHANGE.
    time.sleep(3)

    #Navigation - Login
    username_field = driver.find_element(By.NAME, "uid")
    password_field = driver.find_element(By.NAME, "pwd")

    #Send username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    #Login
    driver.find_element(By.XPATH, "/html/body/div[3]/table/tbody/tr/td/form/table/tbody/tr/td[1]/table/tbody/tr/td[5]/input").click()
    time.sleep(2)

    #Load profile and screenshot
    driver.get(profile_url) #Add your profile link
    time.sleep(2)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("screenshots/HDT_"+ datastring +".png")
    print("HDT Screenshoted")

else:
    driver.quit()

driver.quit()


#GitHub: https://github.com/KlevGG/TrackerScreenshot
