# Se importan las librerias
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Se accede a la página web 
driver= webdriver.Chrome()

driver.implicitly_wait(5)

driver.get("https://www.google.com")

# Maximiza la ventana
driver.maximize_window()

# Se ingresa la palabra a buscar
cuadro_busqueda= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME, 'q'))) 
cuadro_busqueda.clear()
cuadro_busqueda.send_keys("Latam" + Keys.ENTER)

# Se selecciona el resultado de búsqueda
resultado= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//h3[contains(text(),'Cotiza Vuelos, Seguros, Hoteles y Autos | LATAM en')]"))) 
resultado.click()

#Ingresar Origen
origen= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='txtInputOrigin_field']")))  
origen.clear()
origen.send_keys("Buenos Aires")
origen= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Todos los aeropuertos')]")))
origen.click()


# Ingresar Destino
destino= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='txtInputDestination_field']"))) 
destino.clear()
destino.send_keys("Italia")
destino= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnItemAutoComplete_0']//span[@class='sc-inZACr hEOYcR'][normalize-space()='Todos los aeropuertos']"))) 
destino.click()


# Seleccionar la Fecha de Ida
fecha_ida= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='departureDate']"))) 
fecha_ida.click()
fecha_ida= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//td[@aria-label='Elija miércoles, 26 de junio de 2024 como su fecha de ida. Está disponible.']//span[@class='sc-kWhykh gTPxFH'][normalize-space()='26']"))) 
fecha_ida.click()

# Seleccionar la Fecha de Vuelta
fecha_vuelta= WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='arrivalDate']"))) 
fecha_vuelta.click()
fecha_vuelta= WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//td[@aria-label='Elija viernes, 26 de julio de 2024 como fecha de vuelta. Está disponible.']")))
fecha_vuelta.click()

# Seleccionar el botón Buscar
buscar= WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'btnSearchCTA')))
buscar.click()

driver.quit()