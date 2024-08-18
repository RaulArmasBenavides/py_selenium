from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope='session')
def setup():
    driver = webdriver.Chrome()
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
    
    # Asegura que el URL es el esperado
    assert comm_url == 'https://www.python.org/community-landing/'

def test_downloads_link(setup):
    """Test to verify the Downloads link works correctly"""
    driver = setup
    driver.get('http://www.python.org')
    
    # Encuentra el enlace "Downloads" y verifica su URL
    downloads_elem = driver.find_elements(By.LINK_TEXT, 'Downloads')[0]
    downloads_url = downloads_elem.get_attribute('href')
    
    # Visita el URL y verifica que se redirige correctamente
    driver.get(downloads_url)
    assert driver.title.startswith('Download Python')  # El título debería empezar con "Download Python"
    print('Downloads URL=>', downloads_url)

def test_search_functionality(setup):
    """Test the search functionality on python.org"""
    driver = setup
    driver.get('http://www.python.org')
    
    # Encuentra el cuadro de búsqueda y realiza una búsqueda
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys('pytest')
    search_box.send_keys(Keys.RETURN)
    
    # Verifica que los resultados de la búsqueda se carguen
    assert 'Welcome to Python.org' in driver.title
    results = driver.find_elements(By.CSS_SELECTOR, 'ul.list-recent-events li')
    header = driver.find_element(By.XPATH, "//h2[text()='Search Python.org']")
    assert header is not None
    assert len(results) > 0  # Asegúrate de que haya resultados
    
    # Imprime el número de resultados
    print(f'Found {len(results)} search results for "pytest".')

# Si este archivo se ejecuta como script, corre las pruebas
if __name__ == '__main__':
    pytest.main()