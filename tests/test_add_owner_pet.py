
# apuntando a la web : https://spring-framework-petclinic-qctjpkmzuq-od.a.run.app/

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope='session')
def setup():
    # Inicializa Google Chrome
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_add_owner_and_pet(setup):
    driver = setup
    driver.get('https://spring-framework-petclinic-qctjpkmzuq-od.a.run.app/')
    
    # Navega a la página "Find Owners" usando WebDriverWait
    find_owners_link = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'FIND OWNERS'))
    )
    find_owners_link.click()

    # Navega a la página "Add Owner"
    add_owner_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Add Owner'))
    )
    add_owner_button.click()

    # Rellena el formulario del propietario
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'firstName'))
    ).send_keys('Raul')
    driver.find_element(By.ID, 'lastName').send_keys('Armas')
    driver.find_element(By.ID, 'address').send_keys('123 Main St')
    driver.find_element(By.ID, 'city').send_keys('New York')
    driver.find_element(By.ID, 'telephone').send_keys('1234567890')

    # Envía el formulario del propietario
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Verifica que el propietario ha sido añadido
    assert 'Owner Information' in driver.page_source
    assert 'Raul Armas' in driver.page_source

    # Añadir una nueva mascota para el propietario
    add_pet_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Add New Pet'))
    )
    add_pet_button.click()

    # Rellena el formulario de la mascota
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'name'))
    ).send_keys('Pluto')
    driver.execute_script("document.getElementById('birthDate').value = '2020-01-01';")

    # Selecciona el tipo de mascota (por ejemplo, "dog")
    pet_type_dropdown = Select(driver.find_element(By.ID, 'type'))
    pet_type_dropdown.select_by_visible_text('dog')

    # Envía el formulario de la mascota
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Verifica que la mascota ha sido añadida
    assert 'Pluto' in driver.page_source
    assert '2020-01-01' in driver.page_source
    assert 'dog' in driver.page_source

if __name__ == '__main__':
    pytest.main()