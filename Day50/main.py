from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys

EMAIL = "zirochkamaym@gmail.com"
PASSWORD = "27102006Marianna"
SLEEP_TIME = 2

chromea_options = webdriver.ChromeOptions()
chromea_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chromea_options)
driver.get("https://tinder.com")


time.sleep(SLEEP_TIME)
# Click Reject Cookies Button
try:
    driver.find_element(By.XPATH, '//*[@id="s-1958430230"]/div/div[2]/div/div/div[1]/div[1]/button').click()
except Exception as e:
    driver.close()
    print(f"No cookies button found or already clicked. [{e}]")    

time.sleep(SLEEP_TIME)
# Click Log In Button
try:
    driver.find_element(by=By.XPATH, value='//*[@id="s-1958430230"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a').click()
except Exception as e:
    driver.close()
    print(f"No log in button found or already clicked. [{e}]")

time.sleep(SLEEP_TIME)
# Click Log In with Facebook Button
try:
    driver.find_element(by=By.XPATH, value='//*[@id="s608155990"]/div/div/div/div[2]/div/div/div[2]/div[2]/span/div[2]/button').click()
except Exception as e:
    # driver.close()
    # print(f"No log in by facebook button found or already clicked. [{e}]")
    # sys.exit(1) 
    driver.find_element(by=By.XPATH, value='//*[@id="s608155990"]/div/div/div/div[2]/div/div/div[2]/div[2]/span/button').click()
    driver.find_element(by=By.XPATH, value='//*[@id="s608155990"]/div/div/div/div[2]/div/div/div[2]/div[2]/span/div[2]/button').click()


time.sleep(SLEEP_TIME)
# Get necessary windows
base_window = driver.window_handles[0] 
fb_login_window = driver.window_handles[1]

# Switch to Facebook login window
driver.switch_to.window(fb_login_window)

time.sleep(3)
# Fill in Facebook login form
try:
    email_input = driver.find_element(by=By.XPATH, value='//*[@id="email"]')
    email_input.send_keys(EMAIL)
    password_input = driver.find_element(by=By.ID, value='pass')
    password_input.click()
    password_input.send_keys(PASSWORD)
except Exception as e:
    print(f"Email input or paswword input not found or already filled. [{e}]")

time.sleep(2)
# Submit the form
driver.find_element(by=By.XPATH, value='//*[@id="loginbutton"]').click()

time.sleep(15)
# Confirm the login
try:
    driver.find_element(by=By.CSS_SELECTOR, value='body > div > div > div > div > div > div > div > div.x9f619.x1ja2u2z.x78zum5.x1q0g3np.x1iyjqo2.x1t2pt76.x1n2onr6.xvrxa7q.x1nhjfyr > div.x9f619.x2lah0s.x1n2onr6.x78zum5.x1iyjqo2.x1t2pt76.x1lspesw > div > div > div > div > div > div > div.x9f619.x78zum5.xdt5ytf.x2lah0s.x193iq5w.x1l90r2v.xexx8yu.x2bj2ny.x1ey2m1c.xixxii4.x80663w.xh8yej3.x1vjfegm > div > div > div.x1n2onr6.x1ja2u2z.x9f619.x78zum5.xdt5ytf.x2lah0s.x193iq5w.xyamay9 > div > div > div > div:nth-child(1) > div > div > div > div').click()
except Exception as e: 
    print(f"Confirm login button not found or already clicked. [{e}]")

# Switch back to the main window
driver.switch_to.window(base_window)

time.sleep(7)
# Click Allow Location Button
try:
    driver.find_element(by=By.XPATH, value='//*[@id="s608155990"]/div/div/div/div/div[3]/button[1]').click()
except Exception as e: 
    print(f"Button not found or already clicked. [{e}]")


time.sleep(5)
# Click Allow Notification Button
try:
    driver.find_element(by=By.XPATH, value='//*[@id="s608155990"]/div/div/div/div/div[3]/button[1]').click()
except Exception as e: 
    print(f"Button not found or already clicked. [{e}]")
