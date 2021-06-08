from helpers import properties

from drivers import chrome

class BasePage():
    drivers = None

    def get_driver(self):
        default_driver = properties.get_settings()['DEFAULT_DRIVER']

