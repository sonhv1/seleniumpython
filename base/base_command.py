from helper import wait_until


class BaseCommand():

    def __init__(self, driver):
        self.driver = driver

    def type(self, locator, value):
        try:
            wait_until.presence_of_element_located(self.driver, locator).send_keys(value)
        except:
            self.driver.quit()
            raise

    def click(self, locator):
        try:
            wait_until.element_to_be_clickable(self.driver, locator).click()
        except:
            self.driver.quit()
            raise
