# lesson05_task1_simple.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def click_blue_button():
    # Инициализация драйвера
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Открытие страницы
        driver.get("http://uitestingplayground.com/classattr")

        # Клик по синей кнопке
        driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()

        # Ожидание ручного закрытия
        input("Нажмите Enter для закрытия браузера...")

    finally:
        # Гарантированное закрытие
        driver.quit()


if __name__ == "__main__":
    for i in range(3):
        print(f"Запуск теста {i+1}/3")
        click_blue_button()
