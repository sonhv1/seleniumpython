import pytest
from base_page import BasePage
from helper import properties

class BaseTest(pytest.TestCase):
    def setUp(self):
        self.driver = BasePage.get_driver()
        self.driver.get(properties.get_setting()['DEFAULT-BASE-URL'])

    def tearDown(self):
            self.driver.quit()

if __name__ == "__main__":
        pytest.main()