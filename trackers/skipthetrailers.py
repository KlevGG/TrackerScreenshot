from .base_tracker import BaseTracker

class SkipthetrailersTracker(BaseTracker):
    def __init__(self, driver, config):
        self.tracker_name = "skipthetrailers"
        super().__init__(driver, config, self.tracker_name)

    def login(self):
        super().login()

    def take_screenshot(self, tracker_name, is_load_at_runtime=False):
        super().take_screenshot(self.tracker_name)

    def run(self):
        super().run()