Тест-кейсы и баг-репорты (https://docs.google.com/spreadsheets/d/1MMXxl_LPs7AARgDa1BZXmrRvufyAw_YbGEI8fH2Jwtw/edit#gid=1715534994)

Для разработки тест-кейсов использованы методы "черного ящика", функционального тестирование, UX тестирование. 
Так же использованы техники тест дизайна : диаграмма состояний и переходов, классы эквивалентности, граничные значения и попарное тестирование.

Разработка проекта автотестирования выполнена по паттерну PageObject. Для разработки автотестов применялись библиотеки pytest, pytest-selenium. 
Использовались фикстуры, фикстуры параметризации, явные и неявные ожидания драйвером, различные способы описания локаторов (СSS_SELECTOR, XPATH, ID, CLASS_NAME, NAME). 

1.Для тестов страницы авторизации: python3 -m pytest -v --driver Chrome --driver-path /driver/chromedriver tests/test_auth_page.py

2.Для тестов страницы регистрации: python3 -m pytest -v --driver Chrome --driver-path /driver/chromedriver tests/test_reg_page.py

3.Для тестов страницы восстановления пароля: python3 -m pytest -v --driver Chrome --driver-path /driver/chromedriver tests/test_reset_page.py

