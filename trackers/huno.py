from selenium.webdriver.common.by import By
from .base_tracker import BaseTracker


class HunoTracker(BaseTracker):
    def __init__(self, driver, config):
        self.tracker_name = "huno"
        super().__init__(driver, config, self.tracker_name)

    def login(self):
        username = self.config["huno"]["username"]
        password = self.config["huno"]["password"]
        profile_url = self.config["huno"]["profile_url"]
        skip = False

        # Open the profile URL
        self.driver.get(profile_url)

        if self.driver.find_elements(By.ID, "challenge-running"):
            print(
                "Please solve the challenge and press enter to continue or type 'n' and press enter to skip."
            )
            response = input()
            if response == "n":
                skip = True
        if not skip:
            # Find the username, password and login button elements
            username_field = self.driver.find_element(By.NAME, "username")
            password_field = self.driver.find_element(By.NAME, "password")
            login_button = self.driver.find_element(By.ID, "login-button")

            # Type username and password
            username_field.send_keys(username)
            password_field.send_keys(password)

            # Click on the login button
            login_button.click()

            # 2FA is enabled, ask for the code
            code_field = self.driver.find_element(By.ID, "v_input")
            if code_field:
                code = input("Please enter the 2FA code: ")
                code_field.send_keys(code)

                verify_button = self.driver.find_element(By.ID, "submit_verification")
                verify_button.click()

    def take_screenshot(self, tracker_name, is_load_at_runtime=False):
        # super().take_screenshot(self.tracker_name)
        if self.config["settings"]["full_page_screenshot"] == "true":
            super().take_screenshot(self.tracker_name, is_load_at_runtime=True)
        else:
            super().take_screenshot(self.tracker_name)

    def run(self):
        super().run()
