#Required Libraries - You can change the browser driver if you would like to.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import datetime
import time

# Headless or with Header. Some websites do not work as headless so it's recommended to keep it False.
options = Options()
options.headless = False
 
#Start the driver 
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
#driver.maximize_window()  #Uncomment for full-screen screenshots

#The list of supported trackers. Please remove unwanted trackers from the array.
trackers = ["ATH", "RF", "LST", "BLU", "HUNO", "SP", "FL", "GPW", "ANT", "RED", "STC", "STT", "AB"]

#AITHER
if "ATH" in trackers:
    print("Entering Aither.")
    driver.get('https://aither.cc/users/XXX') #Add your profile link here. 
    time.sleep(3) #wait 3 seconds to make sure the page loads
    #Navigation - DO NOT CHANGE
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    #Add your username and password
    username.send_keys("YOUR USERNAME")
    password.send_keys("YOUR PASSWORD")
    #Login and save screenshot
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("Aither_"+ datastring +".png")
    print("Aither Screenshoted")

#ReelFlix   
if "RF" in trackers:
    print("Entering Reelflix.")
    driver.get('https://reelflix.xyz/users/XXX') #Add your profile link here. 
    time.sleep(3) #wait 3 seconds to make sure the page loads
    #Navigation
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    #Add your username and password
    username.send_keys("YOUR USERNAME")
    password.send_keys("YOUR PASSWORD")
    #Login and save screenshot
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("RF_"+ datastring +".png")
    print("Reelflix Screenshoted")

#LST    
if "LST" in trackers:
    print("Entering LST.")
    driver.get('https://lst.gg/users/XXX') #Add your profile link here. 
    time.sleep(3)
    #Navigation
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    #Add your username and password
    username.send_keys("YOUR USERNAME")
    password.send_keys("YOUR PASSWORD")
    #Login and save screenshot
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("LST_"+ datastring +".png")
    print("LST Screenshoted")

#Bluetopia
if "BLU" in trackers:
    print("Entering BLU.")
    driver.get('https://blutopia.xyz/users/XXX') #Add your profile link here. 
    time.sleep(3)
    #Navigation
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    #Add your username and password
    username.send_keys("YOUR USERNAME")
    password.send_keys("YOUR PASSWORD")
    #Login and save screenshot
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("BLU_"+ datastring +".png")
    print("BLU Screenshoted")

#Hawke-Uno
if "HUNO" in trackers:
    print("Entering HUNO")
    driver.get('https://hawke.uno/users/XXX') #Add your profile link here. 
    time.sleep(3)
    #Navigation - Login
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    #Add your username and password
    username.send_keys("YOUR USERNAME")
    password.send_keys("YOUR PASSWORD")
    #Login and save screenshot
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("HUNO_"+ datastring +".png")
    print("HUNO Screenshoted")

#Speedapp
if "SP" in trackers:
    print("Entering Speedapp.")
    driver.get('https://speedapp.io/profile/') #Keep the link as it is, DO NOT CHANGE.
    time.sleep(3)
    #Navigation - Login
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    #Add your username and password
    username.send_keys("YOUR USERNAME")
    password.send_keys("YOUR PASSWORD")
    #Login and save screenshot
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(3)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("SP_"+ datastring +".png")
    print("SP Screenshoted")

#Filelist
if "FL" in trackers:
    print("Entering Filelist")
    driver.get('https://filelist.io/') #Add your profile link
    time.sleep(3)
    #Navigation - Login
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    #Add your username and password
    username.send_keys("YOUR USERNAME")
    password.send_keys("YOUR PASSWORD")
    #Login and save screenshot
    driver.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(3)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("FL_"+ datastring +".png")
    print("FL Screenshoted")

 #GreatPosterWall
if "GPW" in trackers:
    print("Entering GreatPosterWall")
    driver.get('https://greatposterwall.com/user.php?id=XXXX') #Add your profile link
    time.sleep(3)
    #Navigation - Login
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    #Add your username and password
    username.send_keys("YOUR USERNAME")
    password.send_keys("YOUR PASSWORD")
    #Login and save screenshot
    driver.find_element(By.CLASS_NAME, "Button").click()
    time.sleep(3)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("GPW_"+ datastring +".png")
    print("GPW Screenshoted")    
 
###THE FOLLOWING ARE ADDED AND TESTED BY THE GREAT COMMUNITY### 

#AnimeTorrents
if "ANT" in trackers:
    print("Entering AnimeTorrents")
    driver.get('https://animetorrents.me/login.php')
    time.sleep(3)
    #Navigation - Login
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    #Add your username and password
    username.send_keys("YOUR USERNAME")
    password.send_keys("YOUR PASSWORD")
    #Login
    driver.find_element(By.ID, "login-element-6").click()
    time.sleep(2)
    #Load profile and screenshot
    driver.get('https://animetorrents.me/user-profile.php?uid=XXXXXX') #Add your profile link
    time.sleep(2)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("ANT_"+ datastring +".png")
    print("ANT Screenshoted") 
    
#Redacted
if "RED" in trackers:
    print("Entering Redacted.")
    driver.get('https://redacted.ch/login.php') #Keep the link as it is, DO NOT CHANGE.
    time.sleep(3)
    #Navigation - Login
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    #Add your username and password
    username.send_keys("YOUR USERNAME")
    password.send_keys("YOUR PASSWORD")
    #Login
    driver.find_element(By.CLASS_NAME, "submit").click()
    time.sleep(2)
    #Load profile and screenshot
    driver.get('https://redacted.ch/user.php?id=XXXX') #Add your profile link
    time.sleep(2)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("RED_"+ datastring +".png")
    print("RED Screenshoted")

#SkipTheCommericals
if "STC" in trackers:
    print("Entering SkipTheCommericals.")
    driver.get('https://skipthecommericals.xyz/users/XXXX') #Add your profile link here.
    time.sleep(3) #wait 3 seconds to make sure the page loads
    #Navigation - DO NOT CHANGE
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    #Add your username and password
    username.send_keys("YOUR USERNAME")
    password.send_keys("YOUR PASSWORD")
    #Login and save screenshot
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("STC_"+ datastring +".png")
    print("SkipTheCommericals Screenshoted")
    
#SkipTheTrailers
if "STT" in trackers:
    print("Entering SkipTheTrailers.")
    driver.get('https://skipthetrailers.xyz/users/XXXXX') #Add your profile link here.
    time.sleep(3) #wait 3 seconds to make sure the page loads
    #Navigation - DO NOT CHANGE
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    #Add your username and password
    username.send_keys("YOUR USERNAME")
    password.send_keys("YOUR PASSWORD")
    #Login and save screenshot
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("STT_"+ datastring +".png")
    print("SkipTheTrailers Screenshoted")
    
#AnimeBytes
if "AB" in trackers:
    print("Entering AnimeBytes")
    driver.get('https://animebytes.tv/user.php') #Keep the link as it is, DO NOT CHANGE.
    time.sleep(3)
    #Navigation - Login
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    #Add your username and password
    username.send_keys("YOUR USERNAME")
    password.send_keys("YOUR PASSWORD")
    #Login
    driver.find_element(By.CLASS_NAME, "submit").click()
    time.sleep(2)
    #Load profile and screenshot
    driver.get('https://animebytes.tv/user.php?id=XXXX') #Add your profile link
    time.sleep(3)
    datastring = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    driver.save_screenshot("AB_"+ datastring +".png")
    print("AnimeBytes Screenshoted") 
 
 
else:
    driver.quit()
    
driver.quit()


#Script on GitHub: https://github.com/KlevGG/TrackerScreenshot
