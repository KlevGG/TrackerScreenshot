import datetime
from selenium.webdriver.common.by import By
from Screenshot import Screenshot  # type: ignore


class BaseTracker:
    def __init__(self, driver, config, tracker_name):
        self.driver = driver
        self.config = config
        self.tracker_name = tracker_name
        self.ob = Screenshot.Screenshot()

    def login(self, login_url=None):
        profile_url = self.config[self.tracker_name]["profile_url"]

        # Open the profile URL or login URL
        if login_url:
            self.driver.get(login_url)
        else:
            self.driver.get(profile_url)

        self.enter_credentials()
        self.click_login_button()

        if login_url:
            self.driver.get(profile_url)

    def enter_credentials(self, username_field=None, password_field=None):
        username = self.config[self.tracker_name]["username"]
        password = self.config[self.tracker_name]["password"]

        # Find the username, password and login button elements
        if not username_field:
            username_field = self.driver.find_element(By.NAME, "username")
        if not password_field:
            password_field = self.driver.find_element(By.NAME, "password")

        # Type username and password
        username_field.send_keys(username)
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

    def hide_passkey(self):
        try:
            passkey_li = self.driver.find_element(
                By.XPATH, "//li[contains(text(), 'Passkey')]"
            )
            self.driver.execute_script(
                "arguments[0].style.display = 'none';", passkey_li
            )
        except:  # noqa: E722
            pass

    def hide_notifications(self):
        try:
            self.driver.execute_script(
                "document.querySelector('#noty_bottomRight_layout_container').style.display = 'none';"
            )
        except:  # noqa: E722
            pass

    def hide_ip(self):
        # CRT
        try:
            element = self.driver.find_element(By.ID, "statuscont0")
            self.driver.execute_script("arguments[0].style.display = 'none';", element)
        except:  # noqa: E722
            pass

        # MTV
        try:
            element = self.driver.find_element(By.ID, "statuscont1")
            self.driver.execute_script("arguments[0].style.display = 'none';", element)
        except:  # noqa: E722
            pass

        # OTW
        try:
            element = self.driver.find_element(
                By.XPATH, "//h2[contains(text(), 'Clients and IP-Addresses')]"
            )
            self.driver.execute_script(
                "arguments[0].parentNode.style.display = 'none';", element
            )
        except:  # noqa: E722
            pass

    def take_screenshot(self, tracker_name, is_load_at_runtime=False):
        date_string = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        image_name = tracker_name + "_" + date_string + ".png"

        if self.config["settings"].get("full_page_screenshot", "false") == "true":
            self.ob.full_screenshot(
                self.driver,
                save_path="screenshots",
                image_name=image_name,
                is_load_at_runtime=is_load_at_runtime,
            )
        else:
            self.driver.save_screenshot("screenshots/" + image_name)

    def run(self):
        print("Capturing " + self.tracker_name)
        self.login()
        self.hide_passkey()
        self.hide_notifications()
        self.hide_ip()
        self.take_screenshot(self.tracker_name)
        print("Captured " + self.tracker_name + "\n")
