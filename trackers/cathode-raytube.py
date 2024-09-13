import pyotp
from selenium.webdriver.common.by import By

from utils import get_decrypted_secrets

from .base_tracker import BaseTracker


class CathoderaytubeTracker(BaseTracker):
    def __init__(self, driver, config):
        self.tracker_name = "cathode-raytube"
        super().__init__(driver, config, self.tracker_name)

    def login(self):
        username = self.config[self.tracker_name]["username"]
        password = self.config[self.tracker_name]["password"]
        profile_url = self.config[self.tracker_name]["profile_url"]
        login_url = self.config[self.tracker_name]["login_url"]

        # Open the login URL
        self.driver.get(login_url)

        # Find the username, password and login button elements
        username_field = self.driver.find_element(By.NAME, "username")
        password_field = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.ID, "login_button")

        # Send username and password
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Click on the login button
        login_button.click()

        # 2FA is enabled, ask for the code
        code_field = self.driver.find_element(By.NAME, "code")
        if code_field:
            if self.config["settings"]["auto_2fa"] == "true":
                decrypted_secrets = get_decrypted_secrets()
                totp = pyotp.TOTP(decrypted_secrets[self.tracker_name])
                code = totp.now()
            else:
                code = input("Please enter the 2FA code: ")
            code_field.send_keys(code)
            login_button = self.driver.find_element(By.ID, "login_button")
            login_button.click()

        # Open the profile URL
        self.driver.get(profile_url)

    def click_login_button(self):
        login_button = self.driver.find_element(By.ID, "login_button")
        login_button.click()

    def take_screenshot(self, tracker_name, is_load_at_runtime=False):
        super().take_screenshot(self.tracker_name)

    def run(self):
        super().run()
