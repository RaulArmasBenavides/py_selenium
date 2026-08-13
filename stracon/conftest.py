"""
Configuración y fixtures para tests de STRACON
"""
import pytest
from selenium import webdriver
from config import STRACON_BASE_URL, get_chrome_options, IMPLICIT_WAIT

@pytest.fixture(scope='session')
def stracon_driver():
    """Crea un driver Chrome para STRACON"""
    driver = webdriver.Chrome(options=get_chrome_options())
    driver.implicitly_wait(IMPLICIT_WAIT)
    driver.get(STRACON_BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def reset_session(stracon_driver):
    """Limpia cookies entre tests"""
    yield
    stracon_driver.delete_all_cookies()
