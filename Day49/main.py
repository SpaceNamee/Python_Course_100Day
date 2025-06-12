from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

ACCOUNT_EMAIL = "mariannabenkalovych@gmail.com"
ACCOUNT_PASSWORD = '27102006'

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://ua.linkedin.com"
)

# Click Reject Cookies Button
# time.sleep(2)
# reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
# reject_button.click()

# Click Sign in Button
time.sleep(5)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Увійти за допомогою електронної пошти")
print("TEXT____________________________=" + sign_in_button.text)
sign_in_button.click()
 
# Sign in
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(ACCOUNT_EMAIL)
time.sleep(2)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
time.sleep(2)
password_field.send_keys(Keys.ENTER)

# # You may be presented with a CAPTCHA - Solve the Puzzle Manually
# input("Press Enter when you have solved the Captcha")
