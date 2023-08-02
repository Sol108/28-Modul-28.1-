import pytest
from pages.reset_page import ResetPage
from pages.locators import ResetLocators
from tests.config import Config


# @pytest.mark.skip
@pytest.mark.reg
def test_go_to_reset_password_page_from_auth_page(chrome_browser):
    """Проверяем возможность перехода со страницы "Авторизация" на страницу "Восстановление пароля" """
    page = ResetPage(chrome_browser)
    page.go_to_reset_password_page()
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/reset-credentials'


# @pytest.mark.skip
@pytest.mark.reg
def test_check_elem_reg_form(chrome_browser):
    """Проверяем что в правой части страницы "Восстановление пароля" присутствуют основные табы"""
    page = ResetPage(chrome_browser)
    page.go_to_reset_password_page()
    assert page.get_right_elem_reset_page() == Config.REQ_ELEMENTS_RESET


# @pytest.mark.skip
@pytest.mark.auth
def test_default_login_tab(chrome_browser):
    """Проверяем, что поумолчанию выбран вариант авторизации по номеру телефона
    (в поле ввода логина есть текст "Мобильный телефон")"""
    page = ResetPage(chrome_browser)
    assert page.get_text_from_login() == Config.DEFAULT_LOGIN_TEXT


# @pytest.mark.skip
@pytest.mark.res
def test_check_captcha(chrome_browser):
    """Проверяем, что есть капча"""
    page = ResetPage(chrome_browser)
    page.go_to_reset_password_page()
    assert page.find_element(ResetLocators.CAPTCHA)


# @pytest.mark.skip
@pytest.mark.res
def test_back_button(chrome_browser):
    """Проверка работы кнопки "Вернуться назад" """
    page = ResetPage(chrome_browser)
    page.go_to_reset_password_page()
    page.go_back_to_auth()
    assert page.get_relative_link() == "/auth/realms/b2c/login-actions/authenticate"


# @pytest.mark.skip
@pytest.mark.res
def test_login_text(chrome_browser):
    page = ResetPage(chrome_browser)
    page.go_to_reset_password_page()
    page.find_element(ResetLocators.TAB_TEL).click()
    assert page.get_text_from_login() == Config.DEFAULT_LOGIN_TEXT
    page.find_element(ResetLocators.TAB_EMAIL).click()
    assert page.get_text_from_login() == "Электронная почта"
    page.find_element(ResetLocators.TAB_LOGIN).click()
    assert page.get_text_from_login() == "Логин"
    page.find_element(ResetLocators.TAB_LS).click()
    assert page.get_text_from_login() == "Лицевой счёт"
