"""
EJEMPLO: Tests para Spring Petclinic (Cloud)
Referencia - para ver la estructura anterior
Nota: Usar la estructura profesional en /stracon en su lugar
"""
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope='session')
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_add_owner_form(setup):
    """EJEMPLO: Agregar un propietario en Petclinic Cloud"""
    driver = setup
    driver.get('https://spring-framework-petclinic-qctjpkmzuq-od.a.run.app/')

    find_owners_link = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'FIND OWNERS'))
    )
    find_owners_link.click()

    add_owner_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Add Owner'))
    )
    add_owner_button.click()

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'firstName'))).send_keys('John')
    driver.find_element(By.ID, 'lastName').send_keys('Doe')
    driver.find_element(By.ID, 'address').send_keys('123 Main St')
    driver.find_element(By.ID, 'city').send_keys('New York')
    driver.find_element(By.ID, 'telephone').send_keys('1234567890')

    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    assert 'Owner Information' in driver.page_source
    assert 'John Doe' in driver.page_source
    driver.save_screenshot('add_owner_success.png')
