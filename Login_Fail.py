import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# Open page
driver.get("https://practicetestautomation.com/practice-test-login/")

# Type username student into Username field
username_locator = driver.find_element(By.XPATH, "//input[@id='username']")
username_locator.send_keys("incorrectUser")

# Type password Password123 into Password field
password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
password_locator.send_keys("Password123")

# Puch Submit button
submit_locator = driver.find_element(By.XPATH, "//button[@id='submit']")
submit_locator.click()
time.sleep(2)

# Verify error message is displayed
error_msg = driver.find_element(By.XPATH, "//div[@id='error']")
error_msg.text
assert error_msg.text == "Your username is invalid!"


