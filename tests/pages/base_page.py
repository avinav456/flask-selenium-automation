from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, base_url="http://127.0.0.1:5000"):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)

    def open(self, path: str = "/"):
        self.driver.get(self.base_url + path)

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
