"""
Clase base para todas las páginas
Contiene métodos comunes reutilizables
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config import EXPLICIT_WAIT
from shared.logger import get_logger

logger = get_logger(__name__)

class BasePage:
    """Clase base con métodos comunes para todas las páginas"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)

    def click(self, locator):
        """Espera y hace click en un elemento"""
        logger.info(f"Haciendo click en: {locator}")
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def fill(self, locator, text):
        """Espera, limpia y rellena un campo de input"""
        logger.info(f"Rellenando {locator} con: {text}")
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Espera y obtiene el texto de un elemento"""
        logger.info(f"Obteniendo texto de: {locator}")
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.text

    def is_element_visible(self, locator):
        """Verifica si un elemento es visible"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            logger.info(f"Elemento visible: {locator}")
            return True
        except:
            logger.warning(f"Elemento no visible: {locator}")
            return False

    def is_text_present(self, text):
        """Verifica si un texto está presente en la página"""
        is_present = text in self.driver.page_source
        logger.info(f"Texto '{text}' presente: {is_present}")
        return is_present

    def get_current_url(self):
        """Retorna la URL actual"""
        return self.driver.current_url

    def wait_for_url_to_contain(self, substring, timeout=EXPLICIT_WAIT):
        """Espera a que la URL contenga un substring"""
        logger.info(f"Esperando que URL contenga: {substring}")
        self.wait.until(EC.url_contains(substring))

    def take_screenshot(self, filename):
        """Captura pantalla"""
        logger.info(f"Capturando pantalla: {filename}")
        self.driver.save_screenshot(filename)

    def scroll_to_element(self, locator):
        """Desplaza hasta un elemento"""
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        logger.info(f"Desplazado a: {locator}")

    def wait_for_loading(self, loader_locator=None, timeout=EXPLICIT_WAIT):
        """Espera a que desaparezca un loader"""
        if loader_locator:
            logger.info(f"Esperando a que desaparezca loader: {loader_locator}")
            self.wait.until(EC.invisibility_of_element_located(loader_locator))
