from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ___________ Task 1 _____________
# # Keep the browser open after the script ends
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)

# # 2 step to avoid detection
# chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#   "source": """
#     Object.defineProperty(navigator, 'webdriver', {
#       get: () => undefined
#     })
#   """
# })

# # Open the Amazon page
# driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

# # Change country by clicking on the country flag
# try:
#     ukraine_option = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.ID, "nav-global-location-popover-link"))
#     )
#     ukraine_option.click()
#     ukraine_option = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.ID, "GLUXCountryListDropdown"))
#     )
#     time.sleep(5)
#     ukraine_option.click()
#     ukraine_option = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.ID, "GLUXCountryList_6"))
#     )
#     time.sleep(2)
#     ukraine_option.click()
#     ukraine_option = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.ID, "a-autoid-237-announce"))
#     )
#     time.sleep(3)
#     ukraine_option.click()
# except Exception as e:
#     print("Ukraine option not found, continuing...")
#     print(e)

# # Перезавантажити сторінку, щоб cookies подіяли
# driver.refresh()
# time.sleep(5)

# # Wait for the price element to be present
# price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction").text

# # Print the price
# print(price_dollar + "." + price_cents)

# ___________ Task 2 _____________
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument("user-agent=Mozilla/5/0 (Windows NT 10.0; Win64; x64)")
# driver = webdriver.Chrome(options=chrome_options)

# # 2 step to avoid detection
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#   "source": """
#     Object.defineProperty(navigator, 'webdriver', {
#       get: () => undefined
#     })
#   """
# })

# driver.get("https://www.python.org")
# time.sleep(5)
# piece = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul')

# pieces = piece.text.split("\n")

# formatted_pieces = {}


# for i in range(0, len(pieces), 2):
#   formatted_pieces[str(len(formatted_pieces) + 1)] = {
#     "time": pieces[i],
#     "name": pieces[i + 1]
#   }  

# print(formatted_pieces)

# ___________ Task 3 _____________
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument("user-agent=Mozilla/5/0 (Windows NT 10.0; Win64; x64)")
# driver = webdriver.Chrome(options=chrome_options)

# # 2 step to avoid detection
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#   "source": """
#     Object.defineProperty(navigator, 'webdriver', {
#       get: () => undefined
#     })
#   """
# })

# driver.get("https://secure-retreat-92358.herokuapp.com")

# driver.find_element(By.NAME, "fName").send_keys("Vlad")
# driver.find_element(By.NAME, "lName").send_keys("Kovalchuk")
# driver.find_element(By.NAME, "email").send_keys("mariannabenkalovych@gmail.com")
# driver.find_element(By.CSS_SELECTOR, "button").click()
# time.sleep(5)

# __________ Task 4 _____________
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("user-agent=Mozilla/5/0 (Windows 10.0; Win64; x64)")
driver = webdriver.Chrome(options=chrome_options)

# 2 step to avoid detection
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#   "source": """
#     Object.defineProperty(navigator, 'webdriver', {
#       get: () => undefined
#     })
#   """
# })

# Open the website
driver.get("http://orteil.dashnet.org/cookieclicker")
time.sleep(5)

driver.find_element(By.ID, "langSelect-EN").click()
time.sleep(5)

st = time.time()
while True:
  driver.find_element(By.ID, "bigCookie").click()
  

  if time.time() - st >= 5:
    i = 0
    while i != 19:
      if driver.find_element(By.ID, f"productPrice{i}").text != '':
        if int(driver.find_element(By.ID, "cookies").text.split(" ")[0].replace(",", "")) >= int(driver.find_element(By.ID, f"productPrice{i}").text.replace(",", "")):
          driver.find_element(By.ID, f"product{i}").click()
          time.sleep(0.2)
          i -= 1
      i += 1
    st = time.time()  

        