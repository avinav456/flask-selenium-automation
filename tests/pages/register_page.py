from selenium.webdriver.common.by import By
from .base_page import BasePage

class RegisterPage(BasePage):
    NAME = (By.ID, "name")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "registerBtn")

    def open_register(self):
        self.open("/register")

    def register(self, name, email, password):
        self.open_register()
        d = self.driver
        d.find_element(*self.NAME).send_keys(name)
        d.find_element(*self.EMAIL).send_keys(email)
        d.find_element(*self.PASSWORD).send_keys(password)
        d.find_element(*self.SUBMIT).click()
