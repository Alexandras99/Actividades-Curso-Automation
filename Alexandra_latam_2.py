# Se importan las librerias
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Se accede a la página web 
driver= webdriver.Chrome()
driver.get("https://www.google.com")

# Maximiza la ventana
driver.maximize_window()

# Tiempo de espera
time.sleep(5)

# Se ingresa la palabra a buscar
Cuadro_busqueda= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME, 'q'))) 
Cuadro_busqueda.send_keys("Latam" + Keys.ENTER)

# Se selecciona el resultado de búsqueda
Resultado= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h3[contains(text(),'Cotiza Vuelos, Seguros, Hoteles y Autos | LATAM en')]"))) 
Resultado.click()

#Ingresar Origen
Origen= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='txtInputOrigin_field']")))  
Origen.send_keys("Buenos Aires")
Origen= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Todos los aeropuertos')]")))
Origen.click()


# Ingresar Destino
Destino= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='txtInputDestination_field']"))) 
Destino.send_keys("Italia")
Destino= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='btnItemAutoComplete_0']//span[@class='sc-inZACr hEOYcR'][normalize-space()='Todos los aeropuertos']"))) 
Destino.click()


# Seleccionar la Fecha de Ida
Fecha_ida= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='departureDate']"))) 
Fecha_ida.click()
time.sleep(5)
Fecha_ida= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//td[@aria-label='Elija miércoles, 26 de junio de 2024 como su fecha de ida. Está disponible.']//span[@class='sc-kWhykh gTPxFH'][normalize-space()='26']"))) 
Fecha_ida.click()

time.sleep(3)

# Seleccionar la Fecha de Vuelta
Fecha_vuelta= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='arrivalDate']"))) 
Fecha_vuelta.click()

time.sleep(3)

Fecha_vuelta= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//td[@aria-label='Elija viernes, 26 de julio de 2024 como fecha de vuelta. Está disponible.']")))
Fecha_vuelta.click()

time.sleep(3)

# Seleccionar el botón Buscar
Buscar= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'btnSearchCTA')))
Buscar.click()

# Tiempo de espera
time.sleep(10)

driver.quit()