from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_oage import BasePage


class Exception_Page(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._driver = driver

