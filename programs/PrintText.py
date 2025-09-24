import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://localhost/uth/gadgetsgallery/catalog/")
"""
1. How many rows are there in the Table?
2. Total number of columns
3. Get the data from the specific row and column
4. Print data of all rows and columns
"""


print("Total Rows->", len(driver.find_elements(By.XPATH,"//*[@class='contentContainer']/div[2]/table/tbody/tr")))
print("Total Columns->", len(driver.find_elements(By.XPATH,"//*[@class='contentContainer']/div[2]/table/tbody/tr[1]/td")))
print(driver.find_element(By.XPATH,"//*[@class='contentContainer']/div[2]/table/tbody/tr[1]/td[1]").text)

prodTable=driver.find_element(By.XPATH,"//*[@class='contentContainer']/div[2]/table")

tableRows = prodTable.find_elements(By.XPATH,"//*[@class='contentContainer']/div[2]/table/tbody/tr[2]/td")
print("-----------------------------------------")
for row in tableRows:
    row.click()
    time.sleep(2)
    print(driver.title)
    driver.back()