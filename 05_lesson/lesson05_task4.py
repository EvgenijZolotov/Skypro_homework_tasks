from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
import time


def login():
    # Настройка Firefox с видимым интерфейсом
    options = Options()
    options.headless = False  # Окно браузера будет видимым

    # Инициализация драйвера
    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()),
        options=options
    )

    try:
        # Открытие страницы
        driver.get("http://the-internet.herokuapp.com/login")
        print("Страница авторизации открыта")

        # Заполнение формы
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")

        username.send_keys("tomsmith")
        password.send_keys("SuperSecretPassword!")
        print("Данные для ввода заполнены")

        # Клик по кнопке
        driver.find_element(By.CSS_SELECTOR, "button.radius").click()
        print("Кнопка Login нажата")

        # Получение сообщения
        message = driver.find_element(By.ID, "flash").text
        clean_message = message.split("\n")[0]
        print(f"Сообщение системы: {clean_message}")

        # Пауза для просмотра результата (5 секунд)
        print("Браузер закроется автоматически через 5 секунд...")
        time.sleep(5)

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
    finally:
        # Закрытие браузера
        driver.quit()
        print("Браузер закрыт")


if __name__ == "__main__":
    login()
