import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(executable_path="C:/Users/AnkitPal/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://phptravels.org/register.php")


#driver.find_element(By.XPATH,"//input[@class='gLFyf gsfi']").send_keys("python")
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='selected-flag']").click()
optionsList = driver.find_elements(By.CSS_SELECTOR, 'ul.country-list li span')

print(len(optionsList))

for i in optionsList:
    print(i.text)
    time.sleep(0)
    if i == 'United Kingdom':
        i.click()


