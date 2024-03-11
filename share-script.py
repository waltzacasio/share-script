from selenium import webdriver

# driver = webdriver.Chrome()

# Create a global WebDriver instance
driver = None

def get_or_create_driver():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
    return driver

# Use the driver in your test cases or interactions
driver = get_or_create_driver()

driver.get("https://www.facebook.com/")