from utils.locators import homepage_locators
from base.base_command import BaseCommand

class Homepage(BaseCommand):
    def __init__(self, driver):
        BaseCommand.__init__(self, driver)

    def click_login_button(self):
        self.click(homepage_locators.login_btn)
