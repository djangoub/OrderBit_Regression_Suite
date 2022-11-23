# selenium 4
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# Open page
url_locator = driver.get("https://practicetestautomation.com/practice-test-login/")

# Type username student into Username field
username_locator = driver.find_element(By.XPATH, "//input[@id='username']")
username_locator.send_keys("student")

# Type password Password123 into Password field
password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
password_locator.send_keys("Password123")

# Puch Submit button
submit_locator = driver.find_element(By.XPATH, "//button[@id='submit']")
submit_locator.click()
time.sleep(2)

# Verify new page URL contains practicetestautomation.com/logged-in-successfully/
actual_url = driver.current_url
assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
text_locator = driver.find_element(By.XPATH, "//h1[@class='post-title']")
actual_text = text_locator.text
assert actual_text == "Logged In Successfully"

# Verify button Log out is displayed on the new page
logout_locator = driver.find_element(By.LINK_TEXT, "Log out")
assert logout_locator.is_displayed()
print("test is completed without any errors")
time.sleep(2)

