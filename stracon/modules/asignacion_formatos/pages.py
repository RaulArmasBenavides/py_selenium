"""
Páginas para el módulo Asignación de Formatos
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from shared.logger import get_logger

logger = get_logger(__name__)

class AsignacionFormatosPage(BasePage):
    """Página de Asignación de Formatos"""

    # Locators
    TITULO = (By.XPATH, "//h1[contains(text(), 'Asignación de Formatos')]")
    BTN_AGREGAR = (By.XPATH, "//button[contains(text(), 'Agregar')]")
    BTN_NUEVO = (By.XPATH, "//button[contains(text(), 'Nuevo')]")
    CAMPO_FORMATO = (By.ID, "formato")
    CAMPO_USUARIO = (By.ID, "usuario")
    CAMPO_FECHA = (By.ID, "fecha")
    BTN_GUARDAR = (By.CSS_SELECTOR, "button[type='submit']")
    BTN_CANCELAR = (By.XPATH, "//button[contains(text(), 'Cancelar')]")
    TABLA_FORMATOS = (By.XPATH, "//table")
    MENSAJE_EXITO = (By.XPATH, "//span[contains(text(), 'Formato asignado correctamente')]")
    LOADER = (By.XPATH, "//div[@class='spinner-loader']")

    def is_page_loaded(self):
        """Verifica que la página esté cargada"""
        logger.info("Verificando que página esté cargada")
        return self.is_element_visible(self.TITULO)

    def click_agregar(self):
        """Hace click en agregar"""
        logger.info("Click en agregar")
        self.click(self.BTN_AGREGAR)

    def click_nuevo(self):
        """Hace click en nuevo"""
        logger.info("Click en nuevo")
        self.click(self.BTN_NUEVO)

    def fill_formato(self, formato):
        """Rellena el campo formato"""
        logger.info(f"Rellenando formato: {formato}")
        self.fill(self.CAMPO_FORMATO, formato)

    def fill_usuario(self, usuario):
        """Rellena el campo usuario"""
        logger.info(f"Rellenando usuario: {usuario}")
        self.fill(self.CAMPO_USUARIO, usuario)

    def fill_fecha(self, fecha):
        """Rellena el campo fecha"""
        logger.info(f"Rellenando fecha: {fecha}")
        self.fill(self.CAMPO_FECHA, fecha)

    def asignar_formato(self, formato, usuario, fecha=None):
        """Flujo completo para asignar un formato"""
        logger.info(f"Asignando formato: {formato} a usuario: {usuario}")
        self.click_agregar()
        self.fill_formato(formato)
        self.fill_usuario(usuario)
        if fecha:
            self.fill_fecha(fecha)
        self.click(self.BTN_GUARDAR)
        self.wait_for_loading(self.LOADER)

    def verificar_asignacion(self, formato, usuario):
        """Verifica que la asignación se haya realizado"""
        logger.info(f"Verificando asignación de {formato} a {usuario}")
        return self.is_text_present(formato) and self.is_text_present(usuario)

    def verificar_mensaje_exito(self):
        """Verifica que aparezca el mensaje de éxito"""
        logger.info("Verificando mensaje de éxito")
        return self.is_element_visible(self.MENSAJE_EXITO)
