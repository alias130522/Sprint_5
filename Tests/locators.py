
from selenium.webdriver.common.by import By

class Locators:

# url
    url_home_page = 'https://stellarburgers.nomoreparties.site/'    # главная страница
    url_login_window = 'https://stellarburgers.nomoreparties.site/login'    # окно Вход
    url_registration_window = 'https://stellarburgers.nomoreparties.site/register'  # окно Регистрация

# Окно Регистрации
    button_registration_in_window_login = By.XPATH, './/*[@id="root"]/div/main/div/div/p[1]/a'  # кнопка Зарегистрироваться в окне Вход
    button_registration_in_registration = By.XPATH, './/*[@id="root"]/div/main/div/form/button'  # кнопка Зарегистрироваться окна Зарегистрироваться
    field_input_name_in_registration = By.XPATH, './/*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'  # поле ввода Имя окна Зарегистрироваться
    field_input_email_in_registration = By.XPATH, './/*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'  # поле ввода Почты окна Зарегистрироваться
    field_input_password_in_registration = By.XPATH, './/*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input'  # поле ввода Пароль окна Зарегистрироваться
    text_registration = By.XPATH, './/*[@id="root"]/div/main/div/h2[text()="Регистрация"]'  # текст Регистрация в окне регистрации
    text_invalid_password = By.XPATH, './/fieldset[3]/div/p[text()="Некорректный пароль"]'  # текст "Неккоректный пароль"
    text_user_already_exists = By.XPATH, '//*[@id="root"]/div/main/div/p'   # текст "Такой пользователь уже существует"

# окно Вход
    button_login_in_window_login = By.XPATH, './/button[text()="Войти"]'  # кнопка Войти окна Вход
    field_input_email_in_window_login = By.NAME, 'name'  # поле ввода Почты окна Вход
    field_input_password_in_window_login = By.XPATH, './/fieldset[2]/div/div/input'  # поле ввода Пароля окна Вход
    text_login = By.XPATH, './/h2[text()="Вход"]'   # текст Вход окна Вход

# кнопки на Главной странице
    button_place_order = By.XPATH, './/button[text()="Оформить заказ"]'     # кнопка Оформить заказ главной страницы
    button_personal_account = By.XPATH, './/*[@id="root"]/div/header/nav/a/p'   # кнопка Личный кабинет на главной странице
    button_sign_in_account = By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button' # кнопка Войти в аккаунт на главной странице

# кнопки в Личном кабинете
    button_save_in_personal_account = By.XPATH, './/button[2][text()="Сохранить"]'  # кнопка Сохранить в Личном кабинете
    button_constructor = By.XPATH, './/nav/ul/li[1]/a/p[text()="Конструктор"]'  # кнопка Конструктов в Личном кабинете
    button_logo_stellar_burgers = By.CLASS_NAME, 'AppHeader_header__logo__2D0X2'    # кнопка логотип stellar_burgers в Личном кабинете
    button_exit_from_personal_account = By.XPATH, './/li[3]/button[text()="Выход"]'     # кнопка Выход в Личном кабинете

# Прочие
    button_password_recovery = By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a'      # кнопка восстановления пароля
    button_login_in_window_password_recovery = By.XPATH, '//*[@id="root"]/div/main/div/div/p/a'     # кнопка Войти в окне Восстановления пароля
    button_login_in_window_registration = By.XPATH, '//*[@id="root"]/div/main/div/div/p/a'      # кнопка Войти в окне регистрации

# Элементы класса TestConstructor
    button_souses = By.XPATH, './/div[2]/span[text()="Соусы"]' # кнопка Соусы
    button_bulki = By.XPATH, './/div[1]/span[text()="Булки"]' # кнопка Булки
    button_nachinki = By.XPATH, './/div[3]/span[text()="Начинки"]'  # кнопка Начинки
    text_bulki = By.XPATH, './/div[2]/h2[1][text()="Булки"]'    # текст Булки
    text_souses = By.XPATH, './/div[2]/h2[2][text()="Соусы"]'   # текст Соусы
    text_nachinki = By.XPATH, './/div[2]/h2[3][text()="Начинки"]'   # текст Начинки
