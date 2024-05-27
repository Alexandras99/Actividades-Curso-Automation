# Se importan las librerias
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Se accede a la página web 
driver= webdriver.Chrome()
driver.get("https://www.google.com")

# Maximiza la ventana
driver.maximize_window()

# Tiempo de espera
time.sleep(5)

# Se ingresa la palabra a buscar
Cuadro_busqueda= driver.find_element(By.NAME, 'q')
Cuadro_busqueda.send_keys("Latam" + Keys.ENTER)

# Tiempo de espera
time.sleep(5)

# Se selecciona el resultado de búsqueda
Resultado= driver.find_element(By.XPATH, "//h3[contains(text(),'Cotiza Vuelos, Seguros, Hoteles y Autos | LATAM en')]")
Resultado.click()

# Tiempo de espera
time.sleep(5)

#Ingresar Origen

Origen= driver.find_element(By.XPATH, "//input[@id='txtInputOrigin_field']")
Origen.send_keys("Buenos Aires")
Origen= driver.find_element(By.XPATH, "//span[contains(text(), 'Todos los aeropuertos')]")
Origen.click()

# Ingresar Destino
Destino= driver.find_element(By.XPATH, "//input[@id='txtInputDestination_field']")
Destino.send_keys("Italia")
Destino= driver.find_element(By.XPATH, "//button[@id='btnItemAutoComplete_0']//span[@class='sc-inZACr hEOYcR'][normalize-space()='Todos los aeropuertos']")
Destino.click()

# Tiempo de espera
time.sleep(5)

# Seleccionar la Fecha de Ida
Fecha_ida= driver.find_element(By.XPATH, "//div[@class='sc-cIIdys jEBCnD']")
Fecha_ida.click()
Fecha_ida= driver.find_element(By.XPATH, "//td[@aria-label='Elija miércoles, 26 de junio de 2024 como su fecha de ida. Está disponible.']")
Fecha_ida.click()

# Seleccionar la Fecha de Vuelta
Fecha_vuelta= driver.find_element(By.XPATH, "//div[@class='sc-cIIdys gABgRF']")
Fecha_vuelta.click()
Fecha_vuelta= driver.find_element(By.XPATH, "//td[@aria-label='Elija viernes, 26 de julio de 2024 como fecha de vuelta. Está disponible.']")
Fecha_vuelta.click()


# Tiempo de espera
time.sleep(5)

# Seleccionar el botón Buscar
Buscar= driver.find_element(By.ID, 'btnSearchCTA')
Buscar.click()

# Tiempo de espera
time.sleep(10)

driver.quit()