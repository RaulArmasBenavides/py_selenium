from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

@pytest.fixture(scope='session')
def setup():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_python_dotorg(setup):
    """Test details of python.org website URLs"""
    driver = setup
    driver.get('http://www.python.org')
    
    # Verifica el título de la página principal
    assert driver.title == 'Welcome to Python.org'
    
    # Encuentra el enlace "Community" y obtiene su URL
    comm_elem = driver.find_elements(By.LINK_TEXT, 'Community')[0]
    comm_url = comm_elem.get_attribute('href')
    
    # Visita el URL y verifica que se redirige correctamente
    print('Community URL=>', comm_url)
    driver.get(comm_url)
    assert driver.title == 'Our Community | Python.org'
    
    # Asegura que el URL es el esperado (ajustado para reflejar el cambio en el sitio web)
    assert comm_url == 'https://www.python.org/community-landing/'

# Si este archivo se ejecuta como script, corre las pruebas
if __name__ == '__main__':
    pytest.main()