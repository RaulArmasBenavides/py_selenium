#apuntando a angular corriendo localmente   http://localhost:4200/petclinic/


from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope='session')
def setup():
    # Inicializa Google Chrome
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_add_owner_form(setup):
    driver = setup
    driver.get('http://localhost:4200/petclinic/')
    
    # Navega a la página "Find Owners" usando un enfoque robusto
    find_owners_link = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'OWNERS'))  # Asegura que el enlace esté clickeable
    )
    find_owners_link.click()

    # Navega a la página "Add Owner"
    add_owner_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'ADD NEW'))  # Espera hasta que sea clickeable
    )
    add_owner_button.click()

    # Rellena el formulario con datos de prueba
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'firstName'))).send_keys('John')
    driver.find_element(By.ID, 'lastName').send_keys('Doe')
    driver.find_element(By.ID, 'address').send_keys('123 Main St')
    driver.find_element(By.ID, 'city').send_keys('New York')
    driver.find_element(By.ID, 'telephone').send_keys('1234567890')

    # Envía el formulario
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Verifica que el propietario ha sido añadido correctamente
    assert 'Owners' in driver.page_source
    # Esperar a que la tabla que contiene 'John Doe' esté presente en la página
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table")))
    # Luego hacer las aserciones
    assert 'John Doe' in driver.page_source
    assert '123 Main St' in driver.page_source
    assert 'New York' in driver.page_source

    # Captura una captura de pantalla en caso de éxito
    driver.save_screenshot('add_owner_success.png')

if __name__ == '__main__':
    pytest.main()
