"""
Configuración global de Pytest
Fixtures compartidas para todos los tests
"""
import pytest
from selenium import webdriver
from config import get_chrome_options, IMPLICIT_WAIT

@pytest.fixture(scope='session')
def driver():
    """Driver genérico para tests"""
    driver = webdriver.Chrome(options=get_chrome_options())
    driver.implicitly_wait(IMPLICIT_WAIT)
    yield driver
    driver.quit()
