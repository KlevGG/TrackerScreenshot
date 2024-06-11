from selenium.webdriver.common.by import By
from .base_tracker import BaseTracker

class HdtorrentsTracker(BaseTracker):
    def __init__(self, driver, config):
        self.tracker_name = "hdtorrents"
        super().__init__(driver, config, self.tracker_name)

    def login(self):
        super().login(login_url=self.config[self.tracker_name]["login_url"])

    def enter_credentials(self):
        username_field = self.driver.find_element(By.NAME, "uid")
        password_field = self.driver.find_element(By.NAME, "pwd")

        super().enter_credentials(username_field, password_field)

    def click_login_button(self):
        login_button = self.driver.find_element(By.XPATH, "/html/body/div[3]/table/tbody/tr/td/form/table/tbody/tr/td[1]/table/tbody/tr/td[5]/input")
        login_button.click()

    def take_screenshot(self, tracker_name, is_load_at_runtime=False):
        super().take_screenshot(self.tracker_name)

    def run(self):
        super().run()