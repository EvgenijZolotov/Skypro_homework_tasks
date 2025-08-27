from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

# Настройки для браузера Chrome
options = Options()
# Игнорировать ошибки сертификатов (например, если сайт использует самоподписанный SSL)
options.add_argument('--ignore-certificate-errors')

# Инициализация WebDriver с заданными опциями
driver = webdriver.Chrome(options=options)

try:
    # Открываем целевую страницу с динамически загружаемыми изображениями
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Явное ожидание: ждём, пока загрузятся все 4 изображения
    WebDriverWait(driver, 15).until(
        lambda d: len(d.find_elements(
            By.CSS_SELECTOR, "#image-container img")) == 4
    )

    # Получаем список всех загруженных изображений в контейнере
    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")

    # Проверяем, что найдено как минимум 3 изображения
    if len(images) >= 3:
        # Получаем ссылку (атрибут src) третьего изображения (индексация с 0)
        third_img_src = images[2].get_attribute("src")
        print(third_img_src)  # Выводим ссылку на третье изображение
    else:
        # Если изображений меньше 3 — выводим сообщение об ошибке
        print(f"Ошибка: найдено только {len(images)} изображений")

except Exception as e:
    # Обработка исключений: вывод ошибки, если что-то пошло не так
    print(f"Произошла ошибка: {str(e)}")

finally:
    # Закрытие браузера в любом случае (успех или ошибка)
    driver.quit()
