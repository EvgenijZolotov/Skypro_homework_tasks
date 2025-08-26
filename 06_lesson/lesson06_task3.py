from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Явное ожидание загрузки всех 4 картинок
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#container")))

# Ждём, пока у 3-й картинки появится атрибут src
images = driver.find_elements(By.CSS_SELECTOR, "#container")
wait.until(lambda d: images[4].get_attribute("src") != "")

# Получаем src у третьей картинки
src_value = images[4].get_attribute("src")
print(src_value)

driver.quit()
