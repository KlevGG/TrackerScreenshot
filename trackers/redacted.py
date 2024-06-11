from selenium.webdriver.common.by import By
from .base_tracker import BaseTracker

class RedactedTracker(BaseTracker):
    def __init__(self, driver, config):
        self.tracker_name = "redacted"
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
        twofa_field = self.driver.find_element(By.NAME, "qrcode_confirm")

        # Send username and password
        username_field.send_keys(username)
        password_field.send_keys(password)

        # 2FA, ask for the code
        code = input(
            "Please enter the 2FA code: (If you don't have 2FA, just press enter.) "
        )
        twofa_field.send_keys(code)

        login_button = self.driver.find_element(By.CLASS_NAME, "submit")
        # Click on the login button
        login_button.click()

    def take_screenshot(self, tracker_name, is_load_at_runtime=False):
        super().take_screenshot(self.tracker_name)

    def run(self):
        super().run()