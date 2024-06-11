from selenium.webdriver.common.by import By
from .base_tracker import BaseTracker

class PassthepopcornTracker(BaseTracker):
    def __init__(self, driver, config):
        self.tracker_name = "passthepopcorn"
        super().__init__(driver, config, self.tracker_name)

    def login(self):
        username = self.config[self.tracker_name]["username"]
        password = self.config[self.tracker_name]["password"]
        profile_url = self.config[self.tracker_name]["profile_url"]

        # Open the profile URL
        self.driver.get(profile_url)

        # Find the usernam, password and login button elements
        username_field = self.driver.find_element(By.NAME, "username")
        password_field = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        # Send username and password
        username_field.send_keys(username)
        password_field.send_keys(password)

        captcha_container = self.driver.find_element(By.ID, "captcha_container")

        if captcha_container.get_attribute("class") == "hidden":
            login_button.click()

        print("Manually solve the captcha. Press enter when done.")
        code = input()

        # Click on the login button
        login_button.click()

        # 2FA is enabled, ask for the code
        code_field = self.driver.find_element(By.ID, "tfa-code")
        if code_field:
            code = input("Please enter the 2FA code: ")
            code_field.send_keys(code)
            verify_button = self.driver.find_element(By.CSS_SELECTOR, "input[value='Verify']")
            verify_button.click()

    def take_screenshot(self, tracker_name, is_load_at_runtime=False):
        super().take_screenshot(self.tracker_name, is_load_at_runtime=True)

    def run(self):
        super().run()