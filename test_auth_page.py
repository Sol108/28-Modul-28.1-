import pytest
from pages.auth_page import AuthPage, GlobalLocators
from tests.config import Config


# @pytest.mark.skip
@pytest.mark.auth
def test_check_elem_auth_form(chrome_browser):
    """Проверяем что в форме "Авторизация присутствуют основные элементы"""
    page = AuthPage(chrome_browser)
    assert page.get_right_elem_auth() == Config.REQ_ELEMENTS_AUTH


# @pytest.mark.skip
@pytest.mark.auth
def test_default_login(chrome_browser):
    """Проверяем, что поумолчанию выбран вариант авторизации по номеру телефона
    (в поле ввода логина есть текст "Мобильный телефон")"""
    page = AuthPage(chrome_browser)
    assert page.get_text_from_login() == Config.DEFAULT_LOGIN_TEXT


# @pytest.mark.skip
@pytest.mark.auth
def test_chek_left_block_auth(chrome_browser):
    """Проверяем, что в левой части старницы авторизации имеется слоган компании"""
    page = AuthPage(chrome_browser)
    assert page.check_info_left_block() == Config.TAGLINE_TEXT


# @pytest.mark.skip
@pytest.mark.auth
def test_chek_info_for_users_leftside(chrome_browser):
    page = AuthPage(chrome_browser)
    assert "Пользовательским соглашением" in page.find_element(GlobalLocators.LEFT_BLOCK).text.split('\n'), \
        "В левой части страницы остуствует вспомогательная информация для клиентов"


@pytest.mark.auth
def test_login_with_valid_telefon(chrome_browser):
    """Проверка входа в личный кабинет по номеру телефона с валидным значениями """
    page = AuthPage(chrome_browser)
    page.find_captcha()
    page.enter_login(Config.VALID_PHONE)
    page.enter_pass(Config.VALID_PASSWORD)
    page.btn_click()
    page.find_logout_btn()
    assert page.get_relative_link() == '/account_b2c/page', "Пользователь не авторизован"
    page.logout_btn_click()

@pytest.mark.auth
def test_login_with_valid_mail(chrome_browser):
    """Проверка входа в личный кабинет по номеру телефона с валидным значениями """
    page = AuthPage(chrome_browser)
    page.find_captcha()
    page.click_email_tab()
    page.enter_login(Config.VALID_EMAIL)
    page.enter_pass(Config.VALID_PASSWORD)
    page.btn_click()
    page.find_logout_btn()
    assert page.get_relative_link() == '/account_b2c/page', "Пользователь не авторизован"
    page.logout_btn_click()

@pytest.mark.auth
def test_login_with_valid_login(chrome_browser):
    """Проверка входа в личный кабинет по номеру телефона с валидным значениями """
    page = AuthPage(chrome_browser)
    page.find_captcha()
    page.enter_login(Config.VALID_LOGIN)
    page.enter_pass(Config.VALID_PASSWORD)
    page.btn_click()
    page.find_logout_btn()
    assert page.get_relative_link() == '/account_b2c/page', "Пользователь не авторизован"
    page.logout_btn_click()

