from .base_tracker import BaseTracker


class JmeTracker(BaseTracker):
    def __init__(self, driver, config):
        self.tracker_name = "jme"
        super().__init__(driver, config, self.tracker_name)

    def login(self):
        super().login(login_url=self.config[self.tracker_name]["login_url"])

    def take_screenshot(self, tracker_name, is_load_at_runtime=False):
        super().take_screenshot(self.tracker_name)

    def run(self):
        super().run()
