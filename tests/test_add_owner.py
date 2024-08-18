from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

@pytest.fixture(scope='session')
def setup():
    # Inicializa Google Chrome
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_add_owner_form(setup):
    driver = setup
    driver.get('https://spring-framework-petclinic-qctjpkmzuq-od.a.run.app/')
    
    # Navega a la página "Find owners"
    find_owners_link = driver.find_element(By.LINK_TEXT, 'FIND OWNERS')
    find_owners_link.click()

    # Navega a la página "Add Owner"
    add_owner_button = driver.find_element(By.LINK_TEXT, 'Add Owner')
    add_owner_button.click()

    # Rellena el formulario
    driver.find_element(By.ID, 'firstName').send_keys('John')
    driver.find_element(By.ID, 'lastName').send_keys('Doe')
    driver.find_element(By.ID, 'address').send_keys('123 Main St')
    driver.find_element(By.ID, 'city').send_keys('New York')
    driver.find_element(By.ID, 'telephone').send_keys('1234567890')

    # Envía el formulario
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Verifica que el propietario ha sido añadido
    assert 'Owner Information' in driver.page_source
    assert 'John Doe' in driver.page_source
    assert '123 Main St' in driver.page_source
    assert 'New York' in driver.page_source

if __name__ == '__main__':
    pytest.main()