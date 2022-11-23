import time
import pytest
from selenium.webdriver.common.by import By

from page_objects.login_page import LoginPage
from page_objects.login_sucess import Login_Success


class Test_Positive_Scenarios:

    @pytest.mark.login
    def test_positive_Login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("student", "Password123")
        logged_in_page = Login_Success(driver)
        assert logged_in_page.expected_url == login_page.current_url , "Actual page is not same as the expected page"
        assert logged_in_page.header == "Logged In Successfully", "Header is not matching"
        # assert logged_in_page.is_logout_locator(), "Logout button should visible"

