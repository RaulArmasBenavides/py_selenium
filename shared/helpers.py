"""
Helpers y funciones reutilizables compartidas
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import EXPLICIT_WAIT

def wait_and_click(driver, locator, timeout=EXPLICIT_WAIT):
    """Espera a que un elemento sea clickeable y lo hace click"""
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
    element.click()

def wait_and_fill(driver, locator, text, timeout=EXPLICIT_WAIT):
    """Espera a que un elemento esté presente, lo limpia y rellena"""
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )
    element.clear()
    element.send_keys(text)

def wait_for_text(driver, locator, timeout=EXPLICIT_WAIT):
    """Espera a que un elemento esté presente y retorna su texto"""
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )
    return element.text

def is_text_present(driver, text):
    """Verifica si un texto está presente en la página"""
    return text in driver.page_source

def wait_for_element_visibility(driver, locator, timeout=EXPLICIT_WAIT):
    """Espera a que un elemento sea visible"""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )

def wait_for_elements_count(driver, locator, count, timeout=EXPLICIT_WAIT):
    """Espera a que haya N elementos con el locator dado"""
    return WebDriverWait(driver, timeout).until(
        lambda d: len(d.find_elements(*locator)) >= count
    )
