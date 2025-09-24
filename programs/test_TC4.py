import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def test_DatePicker():
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    """
    service = Service("D:\\Software\\Selenium\\msedgedriver.exe")  # Path to downloaded driver
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://jqueryui.com/datepicker/")

    frameWin = driver.find_element(By.XPATH, "//*[@id='content']/iframe")

    driver.switch_to.frame(frameWin)

    time.sleep(1)

    # driver.find_element(By.ID,"datepicker").send_keys("10/18/1982")

    driver.find_element(By.ID, "datepicker").click()