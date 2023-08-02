from selenium.webdriver.common.by import By


class GlobalLocators: # Общие локаторы
    RIGHT_BLOCK = (By.ID, "page-right")  # правый блок страницы
    LEFT_BLOCK = (By.ID, "page-left")  # левый блок страницы
    TAGLINE = (By.CSS_SELECTOR, ".what-is__desc") #слоган Ростелекома


class AuthLocators:

    AUTH_TITLE = (By.XPATH, "//h1[@class='card-container__title']")  # названия формы "Авторизация"/"Регистрация"/"Восстановить пароль"
    AUTH_BLOCK = (By.CLASS_NAME, "rt-tabs.rt-tabs--orange.rt-tabs--small.tabs-input-container__tabs")
    TAB_TEL = (By.ID, "t-btn-tab-phone")  # Таб авторизации по телефону
    TAB_EMAIL = (By.ID, "t-btn-tab-mail")  # Таб авторизации по почте
    TAB_LOGIN = (By.ID, "t-btn-tab-login")  # Таб авторизации по логину
    TAB_LS = (By.ID, "t-btn-tab-ls")  # Таб авторизации по лицевому счету
    AUTH_LOGIN = (By.ID, "username")  # Поле ввода телефона/почты/логина/лицевого счета
    AUTH_PASS = (By.ID, "password")  # Поле ввода пароля
    AUTH_BTN = (By.ID, "kc-login")  # Кнопка "Войти"
    REG_BTN = (By.ID, "kc-register")
    # Текст внутри поля для ввода телефона/почты/логина/лицевого счета
    AUTH_LOGIN_TEXT = (By.XPATH, '//div[@class="rt-input-container tabs-input-container__login"]'
                                 '//span[@class="rt-input__placeholder"]')
    LOGOUT_BTN = (By.ID, "logout-btn")  # Кнопка "Выйти" в личном кабинете
    # кнопки быстрой аутентификации
    AUTH_VK = (By.ID, "oidc_vk")
    AUTH_OK = (By.ID, "oidc_ok")
    AUTH_EMAIL = (By.ID, "oidc_mail")
    AUTH_GOOGLE = (By.ID, "oidc_google")
    AUTH_YA = (By.ID, "oidc_ya")
    FORGOT_PASSWORD = (By.ID, "forgot_password")


class ResetLocators:
    # Текст из формы восстановления пароля
    TEXT_RESET_FORM = (By.XPATH, "//h1[@class='card-container__title']")
    # Получили id блока, где находится форма авторизации
    RIGHT_BLOCK_TABS = (By.XPATH, '//div[@class="rt-tabs rt-tabs--orange rt-tabs--small tabs-input-container__tabs"]')
    AUTH_LOGIN = (By.ID, "username")  # Поле ввода телефона/почты/логина/лицевого счета
    RESET_LOGIN_TEXT = (By.XPATH, '//div[@class="rt-input-container tabs-input-container__login"]'
                                 '//span[@class="rt-input__placeholder"]')
    CAPTCHA = (By.ID, "captcha")
    BACK_BTN = (By.ID, "reset-back")
    CONTINUE_BTN = (By.ID, "reset-back")
    LOGIN_ERROR_BOX = (By.XPATH, "//*[@class='rt-input-container__meta rt-input-container__meta--error']")
    GENERAL_ERROR_BOX = (By.ID, "form-error-message") #Неверный логин или текст с картинки
    TAB_TEL = (By.ID, "t-btn-tab-phone")  # Таб авторизации по телефону
    TAB_EMAIL = (By.ID, "t-btn-tab-mail")  # Таб авторизации по почте
    TAB_LOGIN = (By.ID, "t-btn-tab-login")  # Таб авторизации по логину
    TAB_LS = (By.ID, "t-btn-tab-ls")  # Таб авторизации по лицевому счету

class RegLocators:

    REG_TITLE = (By.XPATH, "//h1[contains(text(),'Регистрация')]")
    REG_NAME = (By.NAME, "firstName")
    REG_SURNAME = (By.NAME, "lastName")
    REG_REGION_TEXT = (By.XPATH, "//span[contains(text(),'Москва г')]")
    CHOOSE_REG_BTN = (By.XPATH, "//div[@class='rt-input-container rt-select__input']//input[@class='rt-input__input rt-input__input--rounded rt-input__input--orange']")
    REG_REGION = (By.XPATH, "//span[contains(text(), 'Москва г')]")
    REG_LOGIN = (By.XPATH, "//input[@id='address']") #поле ввода телефона или электронной почты для регистрации
    REG_PASS = (By.XPATH, "//input[@id='password']")
    REG_PASS_CONFIRM = (By.XPATH, "//input[@id='password-confirm']")
    REG_BTN_SUBMIT = (By.XPATH, '//*[@type="submit"]')
    REG_USER_AGREEMENT = (By.XPATH, "//*[@id='page-right']//a[@class]")
    REG_POLITIC_CONF = (By.XPATH, "//*[@id='page-right']//a[@href='https://b2c.passport.rt.ru/sso-static/agreement/agreement.html']")
    REG_RIGHT_ELEMENTS = (By.CLASS_NAME, "rt-input--rounded")
    REG_BTN = (By.ID, "kc-register")
    REG_CONFIRM_PAGE_TEXT = (By.XPATH, "//h1[@class='card-container__title']")
    ERROR_PASSWORD = (By.CLASS_NAME, "rt-input-container__meta.rt-input-container__meta--error")
    ERROR_CONFIRM_PASSWORD = (By.CLASS_NAME, "rt-input-container__meta.rt-input-container__meta--error")
    ERROR_NAME = (By.CLASS_NAME, "rt-input-container__meta.rt-input-container__meta--error")
    POP_UP_WINDOW_TITLE = (By.XPATH, "//h2[@class='card-modal__title']")
    USER_AGREEMENT_TITLE = (By.XPATH, "//title")
