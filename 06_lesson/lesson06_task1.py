from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# Настройка и запуск браузера
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# Переход на нужную страницу
driver.get("http://uitestingplayground.com/ajax")

# Нажимаем синюю кнопку
button = driver.find_element(By.ID, "ajaxButton")
button.click()

# Явное ожидание появления текста в зеленой плашке
wait = WebDriverWait(driver, 20)
success_text_element = wait.until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "bg-success"),
        "Data loaded with AJAX get request."
    )
)

# Получаем текст из элемента и выводим в консоль
result_text = driver.find_element(By.CLASS_NAME, "bg-success").text
print(result_text)

# Закрываем браузер
driver.quit()
