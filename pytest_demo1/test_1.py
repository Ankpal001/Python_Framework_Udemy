from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:/Users/AnkitPal/Downloads/chromedriver_win32/chromedriver.exe")
driver.get('https://phptravels.org/login')
#driver.t
driver.maximize_window()
WebDriverWait(driver.find_element())
