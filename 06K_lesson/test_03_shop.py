import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    """Фикстура для запуска Firefox и его закрытия после теста."""
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_shop_checkout_total(driver):
    """Проверка суммы покупки в магазине saucedemo.com."""
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")

    # Логин
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))
               ).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Добавление 3 товаров
    product_ids = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]
    for pid in product_ids:
        wait.until(EC.element_to_be_clickable((By.ID, pid))).click()

    # Корзина → Checkout
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    # Заполнение формы
    wait.until(
        EC.visibility_of_element_located((By.ID, "first-name"))
        ).send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Тестов")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()

    # Получение итоговой суммы
    total_text = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_total_label")
            )
    ).text

    assert "$58.29" in total_text, (
        f"Ожидалась сумма $58.29, но получено: {total_text}"
    )
