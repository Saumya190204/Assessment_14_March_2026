from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

options = ChromeOptions()
options.add_experimental_option("detach", True)

driver = Chrome(options=options)
driver.get("https://www.facebook.com")
driver.maximize_window()

sleep(3)

email = driver.find_element(By.CSS_SELECTOR,"input[name='email']" )
email.send_keys("saumya19@gmail.com")

sleep(2)

password = driver.find_element(By.CSS_SELECTOR,"input[name='pass']")
password.send_keys("saumya@123")

sleep(2)

driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Log in"').click()