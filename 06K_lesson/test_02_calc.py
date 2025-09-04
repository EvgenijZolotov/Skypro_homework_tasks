import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    """Простая фикстура для запуска и закрытия Chrome."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator(driver):
    """Проверка калькуляции 7 + 8 = 15 с задержкой 45 секунд."""
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    # Установка задержки
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # Ввод выражения
    for char in ['7', '+', '8', '=']:
        driver.find_element(By.XPATH, f"//span[text()='{char}']").click()

    # Ожидание результата
    result = WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    assert result, "Ожидался результат '15', но он не отобразился"
