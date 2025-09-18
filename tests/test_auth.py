from selenium.webdriver.common.by import By
from tests.pages.register_page import RegisterPage
from tests.pages.login_page import LoginPage

def test_register_and_login_flow(driver, test_user):
    reg = RegisterPage(driver)
    reg.register(test_user["name"], test_user["email"], test_user["password"])
    # After registration, should land on login
    assert "/login" in driver.current_url

    login = LoginPage(driver)
    login.login(test_user["email"], test_user["password"])
    # After login, should land on dashboard
    assert "/dashboard" in driver.current_url

def test_login_invalid_credentials(driver):
    login = LoginPage(driver)
    login.login("nope@example.com", "wrong")
    # should stay on login page with flash error
    body = driver.find_element(By.TAG_NAME, "body").text
    assert "Invalid credentials" in body
