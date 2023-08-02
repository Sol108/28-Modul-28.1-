from urllib.parse import urlparse
from tests.config import Config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.locators import AuthLocators
from selenium.common.exceptions import NoSuchElementException



class BasePage:

    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = Config.BASE_URL
        self.driver.implicitly_wait(timeout)

    def get_all_link(self):
        url = urlparse(self.driver.current_url)
        return url

    def get_relative_link(self):  # нужно установить библиотеку urlib
        url = urlparse(self.driver.current_url)
        return url.path


    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator),
                                                         message=f"Поиск {locator} длился больше 10 секунд, операция прервана...")

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator),
                                                         message=f"Поиск {locator} длился больше 10 секунд, операция прервана...")

    def find_captcha(self):
        try:
            if self.driver.find_element(By.ID, "captcha"):
                raise Exception('На странице есть капча, автотест не может пройти ее')
        except NoSuchElementException:
            pass

    def go_to_reg_page(self):
        """Перейти на страницу "Зарегистрироваться" со страницы "Авторизация" """
        reg_button = self.find_element(AuthLocators.REG_BTN)
        reg_button.click()

    def go_to_reset_password_page(self):
        """Перейти на страницу "Забыл пароль" со страницы "Авторизация" """
        reset_password_button = self.find_element(AuthLocators.FORGOT_PASSWORD)
        reset_password_button.click()