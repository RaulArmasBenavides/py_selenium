
#apuntando a angular corriendo localmente   http://localhost:4200/petclinic/

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

@pytest.fixture(scope='session')
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_add_owner_form(setup):
    driver = setup
    driver.get('http://localhost:4200/petclinic/')
    
    # Navega a la página "Find Owners"
    find_owners_link = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'OWNERS'))
    )
    find_owners_link.click()

    # Navega a la página "Add Owner"
    add_owner_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'ADD NEW'))
    )
    add_owner_button.click()

    # Completa el formulario de "Add Owner"
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'firstName'))).send_keys('John')
    driver.find_element(By.ID, 'lastName').send_keys('Doe')
    driver.find_element(By.ID, 'address').send_keys('123 Main St')
    driver.find_element(By.ID, 'city').send_keys('New York')
    driver.find_element(By.ID, 'telephone').send_keys('1234567890')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Verifica que el propietario ha sido añadido correctamente
    assert 'Owners' in driver.page_source

    # Espera a que aparezca la tabla
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table")))

    # Encuentra y hace clic en el enlace con 'John Doe'
    john_doe_link = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//a[text()='John Doe']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", john_doe_link)
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='John Doe']"))
    ).click()

    # Navega a la página "Add New Pet"
    add_pet_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add New Pet')]"))
    )
    add_pet_button.click()

    # Completa el formulario de "Add New Pet"
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'name'))).send_keys('Buddy')
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.mat-datepicker-input'))).click()  # Click en el campo para abrir el selector de fecha
    driver.execute_script("document.querySelector('input.mat-datepicker-input').value = '2020-01-01';")
    select_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'type')))
    select = Select(select_element)
    select.select_by_visible_text('dog')

    # Envía el formulario de "Add New Pet"
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Verifica que la nueva mascota ha sido añadida correctamente
    assert 'Buddy' in driver.page_source
    assert 'dog' in driver.page_source
    # Captura una captura de pantalla en caso de éxito
    driver.save_screenshot('add_pet_success.png')

if __name__ == '__main__':
    pytest.main()