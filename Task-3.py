from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = Chrome(options=options)
driver.get("https://www.naukri.com/")
driver.maximize_window()
driver.find_element(By.ID,"register_Layer").click()
sleep(2)
driver.find_element(By.ID,"name").send_keys("Saumya")
driver.find_element(By.ID,"email").send_keys("saumya123@gmail.com")
driver.find_element(By.ID,"password").send_keys("Saumya@4567")