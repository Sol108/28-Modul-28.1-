from base_page import BasePage
from locators import RegLocators, GlobalLocators
from tests.config import Config


class RegPage(BasePage):
    """Создаем класс страницы "Регистрация" """
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = Config.BASE_URL or "https://b2c.passport.rt.ru/auth/"
        driver.get(url)

    def enter_name(self, value):
        """Ввести данные в поле "Имя" """
        name = self.find_element(RegLocators.REG_NAME).send_keys(value)
        return name

    def enter_surname(self, value):
        """Ввести данные в поле "Фамилия" """
        surname = self.find_element(RegLocators.REG_SURNAME)
        surname.send_keys(value)
        return surname

    def enter_region(self, value): #ТУТ ТОЖЕ ПОД ВОПРОСОМ
        """Ввести данные в поле "Регион" """
        region = self.find_element(RegLocators.REG_REGION)
        region.clear()
        region.send_keys(value)
        return region

    def enter_login(self, value):
        """Ввести данные в поле "E-mail или мобильный телефон" """
        login = self.find_element(RegLocators.REG_LOGIN)
        login.send_keys(value)
        return login

    def enter_pass(self, value):
        """Ввести данные в поле "Пароль" """
        password = self.find_element(RegLocators.REG_PASS)
        password.send_keys(value)
        return password

    def confirm_pass(self, value):
        """Ввести данные в поле "Подтверждение пароля" """
        confirm_password = self.find_element(RegLocators.REG_PASS_CONFIRM)
        confirm_password.send_keys(value)
        return confirm_password

    def btn_click_registration_btn(self):
        """Подтвердить и отправить заполненные данные кнопкой "Зарегистрироваться" """
        btn_submit_reg = self.find_element(RegLocators.REG_BTN_SUBMIT)
        btn_submit_reg.click()

    def go_to_user_agreement(self):
        """Открыть пользовательское соглашение"""
        agreement_btn = self.find_element(RegLocators.REG_USER_AGREEMENT)
        agreement_btn.click()

    def get_right_elem_reg(self):
        """ Получаем названия основных элементов блока страницы регистрации"""
        # Получаем названия полей
        right_block_reg = self.find_elements(RegLocators.REG_RIGHT_ELEMENTS)
        fields = "".join([x.text for x in right_block_reg])
        return fields

    def get_errors_of_fields(self):
        """ Получаем названия основных элементов блока страницы регистрации"""
        # Получаем названия полей
        errors = self.find_elements(RegLocators.ERROR_NAME)
        errors_text = "".join([x.text for x in errors])
        return errors_text

    def check_info_left_block(self):
        """Получить слоган с левого блока страницы "Регистрация" """
        tagline = self.find_element(GlobalLocators.TAGLINE)
        return tagline.text

    def get_text_from_region(self):
        """Получить название региона из поля "Регион" """
        region_name = self.find_element(RegLocators.REG_REGION_TEXT)
        return region_name.text
