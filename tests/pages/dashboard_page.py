from selenium.webdriver.common.by import By
from .base_page import BasePage

class DashboardPage(BasePage):
    TITLE = (By.ID, "title")
    DESCRIPTION = (By.ID, "description")
    CREATE = (By.ID, "createBtn")

    def create_item(self, title, description):
        d = self.driver
        d.find_element(*self.TITLE).clear()
        d.find_element(*self.TITLE).send_keys(title)
        d.find_element(*self.DESCRIPTION).clear()
        d.find_element(*self.DESCRIPTION).send_keys(description)
        d.find_element(*self.CREATE).click()
