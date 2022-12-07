import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.base_oage import BasePage


class LoginPage(BasePage):
    __url = "https://iqbro.orderbit.app/"
    __signin_click = (By.XPATH, "(//button[@aria-label='Authentication'][normalize-space()='Sign In'])[1]")
    __username_field = (By.XPATH, "//input[@id='email']")
    __password_field = (By.XPATH, "//input[@id='password']")
    __submit_field = (By.XPATH, "//button[@type='submit']")
    __select_category = (By.LINK_TEXT, "Categories")
    __select_product = (By.XPATH, "// li[contains(text(), 'Fresh Vegetables')]")
    __add_product = (By.CSS_SELECTOR, "button[aria-label='Count Button']")
    __cart_click = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/header[1]/div[1]/div[1]/div[2]/button[1]/span[1]")
    __checkout_proceed = (By.XPATH, "//span[@class='py-0.5']")
    __Order_click = (By.XPATH, "//button[normalize-space()='Order Now']")
    __click_account = (By.CSS_SELECTOR, "a[href='/my-account/orders']")
    _click_logout = (By.XPATH, "//span[normalize-space()='Logout']")

    # __error_message = (By.ID, "error")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_login(self, username: str, password: str):

        super()._click(self.__signin_click)
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._click(self.__submit_field)
        super()._click(self.__select_category)
        super()._click(self.__select_product)
        super()._click(self.__add_product)
        time.sleep(5)
        super()._click(self.__cart_click)
        time.sleep(5)
        super()._click(self.__checkout_proceed)
        time.sleep(5)
        super()._click(self.__Order_click)
        time.sleep(5)
        super()._click(self.__click_account)

        super()._click(self._click_logout)


    def get_error_message(self) -> str:
        return super().get_text(self.__error_message)
