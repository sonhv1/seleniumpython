import unittest
from pages.homepage import Homepage
from base.base_command import BaseCommand


class TestHomePage(BaseCommand):

    def __init__(self, driver):
        super().__init__(driver)
        self.drivers = None

    def testCreateAccount(self):
        test_home_page = Homepage(self.drivers)
        test_home_page.click_login_button()


if __name__ == '__main__':
    unittest.main()
