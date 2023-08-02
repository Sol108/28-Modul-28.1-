import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session", autouse=True)
def chrome_browser():
    s = Service('driver/chromedriver.exe')
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=s, options=chrome_options)

    yield driver
    driver.delete_all_cookies()
    driver.quit()


