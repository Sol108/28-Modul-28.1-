import pytest
from pages.reg_page import RegPage
from pages.locators import RegLocators
from tests.config import Config



"""Хотел сделать фикустуру, которая бы сохраняла куку сессии и по ней проводить тесты, чтобы не осуществлять постоянный 
переход со страницы автооризации на страницу регистрации. Но не получилось. """
# @pytest.fixture(scope='session', autouse=True)
# def get_cookies_reg_page(chrome_browser):
#     page = AuthPage(chrome_browser)
#     page.go_to_reg_page()
#     pickle.dump(chrome_browser.get_cookies(), open("cookies.pkl", "wb"))

#работает
# @pytest.mark.skip
@pytest.mark.reg
def test_go_to_reg_page_from_auth_page(chrome_browser):
    """Проверяем возможность перехода со страницы "Авторизация" на страницу "Регистрация" """
    page = RegPage(chrome_browser)
    page.go_to_reg_page()
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

#работает
# @pytest.mark.skip
@pytest.mark.reg
def test_check_elem_reg_form(chrome_browser):
    """Проверяем что в правой части страницы форме "Регистрация" присутствуют основные элементы"""
    page = RegPage(chrome_browser)
    page.go_to_reg_page()
    assert page.get_right_elem_reg() == Config.REQ_ELEMENTS_REG


#работает
# @pytest.mark.skip
@pytest.mark.reg
def test_chek_user_agreement_rightside(chrome_browser):
    """Проверяем, что в правой части страницы есть ссылка на пользовательское соглашение"""
    page = RegPage(chrome_browser)
    page.go_to_reg_page()
    window_before = chrome_browser.window_handles[0]
    user_agree = page.find_element(RegLocators.REG_POLITIC_CONF)
    user_agree.click()
    window_after = chrome_browser.window_handles[1]
    chrome_browser.switch_to.window(window_after)
    assert chrome_browser.title == 'User agreement'


# работает
# @pytest.mark.skip
@pytest.mark.reg
def test_check_requirement_fields(chrome_browser):
    """Проверяем, что при попытке отправить пустые значения в требуемых полях, приведет к выпадению сообщений об ошибках под этими полями"""
    page = RegPage(chrome_browser)
    page.go_to_reg_page()
    page.btn_click_registration_btn()
    assert page.get_errors_of_fields() == Config.ERRORS_OF_FIELDS_TEXT


# работает
# @pytest.mark.skip
@pytest.mark.reg
@pytest.mark.parametrize("valid_login", ["+79823107555", "max@gmail.com"],
                         ids=["Valid phone number", "Valid email"])
def test_registration_with_valid_data(chrome_browser, valid_login, name=Config.VALID_NAME, surname=Config.VALID_SURNAME,
                                      password=Config.VALID_PASSWORD, confirm_password=Config.CONFIRM_VALID_PASSWORD):
    """Регистрация с валидными данными и ранее не использованными телефоном / электронной почтой"""
    page = RegPage(chrome_browser)
    page.go_to_reg_page()
    page.enter_name(name)
    page.enter_surname(surname)
    page.enter_login(valid_login)
    page.enter_pass(password)
    page.confirm_pass(confirm_password)
    page.btn_click_registration_btn()
    assert page.find_element(RegLocators.REG_CONFIRM_PAGE_TEXT).text == 'Подтверждение телефона' or \
           page.find_element(RegLocators.REG_CONFIRM_PAGE_TEXT).text == "Подтверждение email", \
        "Данные не приняты, либо кука сессии протухла"


#работает
# @pytest.mark.skip
@pytest.mark.reg
@pytest.mark.parametrize("valid_login", ["+79954737748", "mz-teplostroy@yandex.ru"],
                         ids=["Early used phone number", "Early used e-mail"])
def test_registration_with_early_used_valid_data(chrome_browser, valid_login, name=Config.VALID_NAME, surname=Config.VALID_SURNAME,
                                      password=Config.VALID_PASSWORD, confirm_password=Config.CONFIRM_VALID_PASSWORD):
    """Проверка, что система распознает ранее зарегистрированные телефон / почту, и при попытке повторной регистрации,
    сообщает об этом пользоваетлю """
    page = RegPage(chrome_browser)
    page.go_to_reg_page()
    page.enter_name(name)
    page.enter_surname(surname)
    page.enter_login(valid_login)
    page.enter_pass(password)
    page.confirm_pass(confirm_password)
    page.btn_click_registration_btn()
    assert page.find_element(RegLocators.POP_UP_WINDOW_TITLE).text == Config.POP_UP_WINDOW_TITLE, "Текст во всплывающем окне не соответсвует требованиям"


# работает
# @pytest.mark.skip
@pytest.mark.reg
@pytest.mark.parametrize("name", ["", "7555", "Maksim", "中国语言测试", "Ффффффффффффффффффффффффффффффыыыыыыы", "Опарывлофлорвыиаалофрыиывмлорфиыаармифьыааимьыаимьриывавьимьиыабмофиаломотбываимбьывиамьивбьаимьбытапарывлофлорвыиаалофрыиывмлорфиыаармифьыааимьыаимьриывавьимьиыабмофиаломотбываимбьывиамьивбьаимьбытапарывлофлорвыиаалофрыиывмлорфиыаармифьыааимьыаимьриывавьимьиыабмофиаломотбываимбьывиамьивбьаимьбытапарывлофлорвыиаалофрыиывмлорфиыаармифьыааимьыаимьриывавьимьиыабмофиаломотбываимбьывиамьивбьаимьбытапарывлофлорвыиаалофрыиывмлорфиыаармифьыааимьыаимьриывавьимьиыабмофиаломотбываимбьывиамьивбьаимьбытапарывлофлорвыиаалофрыиывмлорфиыаармифьыааимьыаимьриывавьимьиыабмофиаломотбываимбьывиамьивбьаимьбытапарывлофлорвыиаалофрыиывмлорфиыаармифьыааимьыаимьриывавьимьиыабмофиаломотбываимбьывиамьивбьаимьбытапарывлофлорвыиаалофрыиывмлорфиыаармифьыааимьыаимьриывавьимьиыабмофиаломотбываимбьывиамьивбьаимьбытапарывлофлорвыиаалофрыиывмлорфиыаармифьыааимьыаимьриывавьимьиыабмофиаломотбываимбьывиамьивбьаимьбытапарывлофлорвыиаалофрыиывмлорфиыаармифьыааимьыаимьриывавьимьиыабмофиаломотбываимбьывиамьивбьаимьбытаавпвапрсс"],
                         ids=["Empty", "Numbers", "English", "Chinese", "31 symbol", "1001 symbol"])
def test_reg_user_invalid_first_name(chrome_browser, name, surname=Config.VALID_SURNAME,
                                     login=Config.VALID_PHONE,
                                     password=Config.VALID_PASSWORD,
                                     confirm_password=Config.CONFIRM_VALID_PASSWORD):
    """Проверка распозновании системой отправленных не валидных значений имени в форме регистрации"""
    page = RegPage(chrome_browser)
    page.go_to_reg_page()
    page.enter_name(name)
    page.enter_surname(surname)
    page.enter_login(login)
    page.enter_pass(password)
    page.confirm_pass(confirm_password)
    page.btn_click_registration_btn()
    assert page.find_element(RegLocators.ERROR_NAME).text == Config.ERROR_VALIDATION_NAME
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'




# БУДЕТ ПАДАТЬ, БАГ
# @pytest.mark.skip
@pytest.mark.reg
def test_chek_left_block_reg(chrome_browser):
    """Проверяем, что в левой части страницы Регистрации имеется слоган компании"""
    page = RegPage(chrome_browser)
    page.go_to_reg_page()
    assert page.check_info_left_block() == Config.TAGLINE_TEXT, "Слоган компании отсуствует"


# тест не работает, какие только локаторы не прописывал, ничего не получилось, время ушло невероятное количество
# думаю, это связно со style="display: none;"
# @pytest.mark.skip
@pytest.mark.reg
def test_default_region(chrome_browser):
    """Проверяем, что поумолчанию в поле "Регион" указана Москва"""
    page = RegPage(chrome_browser)
    page.go_to_reg_page()
    assert page.get_text_from_region() == Config.DEFAULT_REGION

