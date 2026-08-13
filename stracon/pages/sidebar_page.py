"""
Página del Sidebar de STRACON
Contiene la navegación principal
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from shared.logger import get_logger

logger = get_logger(__name__)

class SidebarPage(BasePage):
    """Gestiona la navegación del sidebar de STRACON"""

    # Locators del Sidebar
    CONFIGURACIONES = (By.XPATH, "//span[contains(text(), 'Configuraciones')]")
    ASISTENCIA_DIGITAL = (By.XPATH, "//span[contains(text(), 'Asistencia Digital')]")
    TAREOS = (By.XPATH, "//span[contains(text(), 'Tareos')]")
    GESTION_EQUIPOS = (By.XPATH, "//span[contains(text(), 'Gestión de Equipos')]")
    PARTES_DIARIOS = (By.XPATH, "//span[contains(text(), 'Partes Diarios')]")
    ASIGNACION_FORMATOS = (By.XPATH, "//span[contains(text(), 'Asignación de Formatos')]")
    REPORTES = (By.XPATH, "//span[contains(text(), 'Reportes')]")
    DASHBOARD = (By.XPATH, "//span[contains(text(), 'Dashboard')]")

    def click_configuraciones(self):
        """Navega a Configuraciones"""
        logger.info("Navegando a Configuraciones")
        self.click(self.CONFIGURACIONES)

    def click_asistencia_digital(self):
        """Navega a Asistencia Digital"""
        logger.info("Navegando a Asistencia Digital")
        self.click(self.ASISTENCIA_DIGITAL)

    def click_tareos(self):
        """Navega a Tareos"""
        logger.info("Navegando a Tareos")
        self.click(self.TAREOS)

    def click_gestion_equipos(self):
        """Navega a Gestión de Equipos"""
        logger.info("Navegando a Gestión de Equipos")
        self.click(self.GESTION_EQUIPOS)

    def click_partes_diarios(self):
        """Navega a Partes Diarios"""
        logger.info("Navegando a Partes Diarios")
        self.click(self.PARTES_DIARIOS)

    def click_asignacion_formatos(self):
        """Navega a Asignación de Formatos"""
        logger.info("Navegando a Asignación de Formatos")
        self.click(self.ASIGNACION_FORMATOS)

    def click_reportes(self):
        """Navega a Reportes"""
        logger.info("Navegando a Reportes")
        self.click(self.REPORTES)

    def click_dashboard(self):
        """Navega a Dashboard"""
        logger.info("Navegando a Dashboard")
        self.click(self.DASHBOARD)
