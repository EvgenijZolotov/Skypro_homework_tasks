import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.safari.options import Options as SafariOptions


@pytest.fixture
def driver():
    """Фикстура для инициализации и закрытия Safari WebDriver."""
    options = SafariOptions()
    driver = webdriver.Safari(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_fill_form(driver):
    """Тест заполнения формы и проверки валидации в Safari."""
    driver.implicitly_wait(10)

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "city": "Москва",
        "country": "Россия",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_name, value in form_data.items():
        field = driver.find_element(By.NAME, field_name)
        field.clear()
        field.send_keys(value)

    zip_field = driver.find_element(By.ID, "zip-code")
    zip_field.clear()

    submit_button = driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']"
    )
    submit_button.click()

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.text_to_be_present_in_element_attribute(
            (By.ID, "zip-code"),
            "class",
            "alert-danger"
        )
    )

    zip_class = driver.find_element(
        By.ID, "zip-code"
    ).get_attribute("class")

    assert "alert-danger" in zip_class, (
        "Поле Zip code должно быть подсвечено красным"
    )
    assert "alert-success" not in zip_class, (
        "Поле Zip code не должно быть зеленым"
    )

    success_fields = [
        "first-name", "last-name", "address", "city",
        "country", "e-mail", "phone", "company"
    ]

    for field_id in success_fields:
        field = driver.find_element(By.ID, field_id)
        field_class = field.get_attribute("class")

        assert "alert-success" in field_class, (
            f"Поле {field_id} должно быть подсвечено зеленым"
        )
        assert "alert-danger" not in field_class, (
            f"Поле {field_id} не должно быть красным"
        )


if __name__ == "__main__":
    # Запуск теста без pytest
    options = SafariOptions()
    driver = webdriver.Safari(options=options)
    driver.maximize_window()

    try:
        test_fill_form(driver)
        print("✓ Тест успешно выполнен!")
    except Exception as e:
        print(f"✗ Ошибка: {str(e)}")
    finally:
        driver.quit()
