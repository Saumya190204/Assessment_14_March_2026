from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = Chrome(options=options)
driver.get("https://www.youtube.com/")
driver.maximize_window()
driver.find_element(By.NAME,"search_query").send_keys("melody hits")
driver.find_element(By.CSS_SELECTOR,"button[aria-label='Search']").click()