import pyotp
from selenium.webdriver.common.by import By

from utils import get_decrypted_secrets

from .base_tracker import BaseTracker


class GazellegamesTracker(BaseTracker):
    def __init__(self, driver, config):
        self.tracker_name = "gazellegames"
        super().__init__(driver, config, self.tracker_name)

    def login(self):
        username = self.config[self.tracker_name]["username"]
        password = self.config[self.tracker_name]["password"]
        profile_url = self.config[self.tracker_name]["profile_url"]

        # Open the profile URL
        self.driver.get(profile_url)

        # Find the username, password and 2fa elements
        username_field = self.driver.find_element(By.NAME, "username")
        password_field = self.driver.find_element(By.NAME, "password")
        twofa_field = self.driver.find_element(By.NAME, "authkey")

        # Send username and password
        username_field.send_keys(username)
        password_field.send_keys(password)

        # 2FA, ask for the code
        if self.config["settings"]["auto_2fa"] == "true":
            decrypted_secrets = get_decrypted_secrets()
            totp = pyotp.TOTP(decrypted_secrets[self.tracker_name])
            code = totp.now()
            input("Manually solve the captcha image. Press enter when done.")
        else:
            code = input(
                "Manually solve the captcha image. Press enter when done. (If you use 2FA then press enter after you type the code below)"
            )
        twofa_field.send_keys(code)

        login_button = self.driver.find_element(By.CLASS_NAME, "submit")
        # Click on the login button
        login_button.click()

    def take_screenshot(self, tracker_name, is_load_at_runtime=False):
        super().take_screenshot(self.tracker_name)

    def run(self):
        super().run()
