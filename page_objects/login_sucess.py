import self as self
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_oage import BasePage


class Login_Success(BasePage):
    __url = "https://practicetestautomation.com/logged-in-successfully/"
    __header_locator = (By.XPATH, "//h1[@class='post-title']")
    __logout_locator = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self.__url

    @property
    def header(self) -> str:
        return super().get_text(self.__header_locator)

    def is_logout_locator(self) -> bool:
        return super()._is_displayed(self.__logout_locator)



