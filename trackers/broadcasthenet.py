from seleniumbase import SB # type: ignore
from selenium.webdriver.common.by import By
from .base_tracker import BaseTracker

class BroadcasthenetTracker(BaseTracker):
    def __init__(self, driver, config):
        self.tracker_name = "broadcasthenet"
        super().__init__(driver, config, self.tracker_name)

    def run(self):
        with SB(uc=True, locale_code="en") as sb:
            self.driver = sb.driver
            print("Capturing " + self.tracker_name)
            username = self.config["broadcasthenet"]["username"]
            password = self.config["broadcasthenet"]["password"]
            profile_url = self.config["broadcasthenet"]["profile_url"]

            sb.driver.uc_open_with_reconnect(profile_url, 1)

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
            super().take_screenshot("broadcasthenet")
            print("Captured " + self.tracker_name)