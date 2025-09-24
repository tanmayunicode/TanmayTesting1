from selenium.webdriver.common.by import By


class LoginPage:

    txt_email_name="email_address"
    txt_password_name="password"
    btn_signin_id="tdb1"

    def __init__(self,driver):
        self.drive=driver

    def setEmailAddress(self,email):
        self.driver.find_element(By.NAME,self.txt_email_name).send_keys(email)

    def setPassword(self, pwd):
        self.driver.find_element(By.NAME, self.txt_password_name).send_keys(pwd)

    def clickSignIn(self):
        self.driver.find_element(By.ID, self.btn_signin_id).click()
