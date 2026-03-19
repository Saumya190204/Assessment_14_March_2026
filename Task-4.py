from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = Chrome(options=options)
driver.get("https://www.myntra.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.CLASS_NAME,'desktop-searchBar').send_keys("shoes")