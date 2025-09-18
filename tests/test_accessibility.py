from selenium.webdriver.common.by import By

def test_basic_accessibility_labels(driver):
    # Register page
    driver.get("http://127.0.0.1:5000/register")
    labels = driver.find_elements(By.TAG_NAME, "label")
    inputs = driver.find_elements(By.TAG_NAME, "input")
    # Ensure at least one label and inputs have matching 'for' and 'id'
    label_for_ids = {l.get_attribute("for") for l in labels if l.get_attribute("for")}
    input_ids = {i.get_attribute("id") for i in inputs if i.get_attribute("id")}
    assert label_for_ids.issubset(input_ids)

def test_images_have_alt(driver):
    driver.get("http://127.0.0.1:5000/")
    imgs = driver.find_elements(By.TAG_NAME, "img")
    for img in imgs:
        alt = img.get_attribute("alt")
        assert alt is not None and alt.strip() != ""
