import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://jqueryui.com/datepicker/")

frameWin = driver.find_element(By.XPATH, "//*[@id='content']/iframe")

driver.switch_to.frame(frameWin)

time.sleep(1)

#driver.find_element(By.ID,"datepicker").send_keys("10/18/1982")

driver.find_element(By.ID,"datepicker").click()

time.sleep(2)
month = "October"
year = "2023"
date = "18"



while True:
    monthText = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yearText = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if monthText==month and yearText==year:
        allDates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
        for d in allDates:
            if d.text==date:
                d.click()
                break
    else:
        driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[1]/span").click()

time.sleep(20)
