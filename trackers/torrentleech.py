import time
import pyotp
from selenium.webdriver.common.by import By

from utils import get_decrypted_secrets

from .base_tracker import BaseTracker


class TorrentleechTracker(BaseTracker):
    def __init__(self, driver, config):
        self.tracker_name = "torrentleech"
        super().__init__(driver, config, self.tracker_name)

    def login(self):
        super().login()

    def click_login_button(self):
        login_button = self.driver.find_element(By.CLASS_NAME, "btn")
        login_button.click()

        prefcode = self.driver.find_element(By.ID, "prefcode")

        if prefcode:
            # if auto_2fa is enabled, use the 2fa secret from decrypted_secrets
            if self.config["settings"]["auto_2fa"] == "true":
                decrypted_secrets = get_decrypted_secrets()
                totp = pyotp.TOTP(decrypted_secrets[self.tracker_name])
                code = totp.now()
            else:
                code = input("Please enter the 2FA code: ")

            code_fields = self.driver.find_elements(By.CLASS_NAME, "prefcode_otp")
            for i in range(6):
                code_fields[i].send_keys(code[i])

            continue_button = self.driver.find_element(
                By.CLASS_NAME, "button2facontinue"
            )

            time.sleep(5)

            continue_button.click()

            profile_url = self.config[self.tracker_name]["profile_url"]
            self.driver.get(profile_url)

    def take_screenshot(self, tracker_name, is_load_at_runtime=False):
        super().take_screenshot(self.tracker_name)

    def run(self):
        super().run()
