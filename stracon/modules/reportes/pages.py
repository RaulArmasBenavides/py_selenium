"""
Páginas para el módulo Reportes
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from shared.logger import get_logger

logger = get_logger(__name__)

class ReportesPage(BasePage):
    """Página de Reportes"""

    # Locators
    TITULO = (By.XPATH, "//h1[contains(text(), 'Reportes')]")
    BTN_GENERAR = (By.XPATH, "//button[contains(text(), 'Generar Reporte')]")
    SELECT_TIPO_REPORTE = (By.ID, "tipo_reporte")
    SELECT_FECHA_INICIO = (By.ID, "fecha_inicio")
    SELECT_FECHA_FIN = (By.ID, "fecha_fin")
    BTN_EXPORTAR = (By.XPATH, "//button[contains(text(), 'Exportar')]")
    TABLA_RESULTADOS = (By.XPATH, "//table[@class='resultados']")
    MENSAJE_GENERADO = (By.XPATH, "//span[contains(text(), 'Reporte generado')]")

    def is_page_loaded(self):
        """Verifica que la página esté cargada"""
        logger.info("Verificando que página de reportes esté cargada")
        return self.is_element_visible(self.TITULO)

    def seleccionar_tipo_reporte(self, tipo):
        """Selecciona un tipo de reporte"""
        logger.info(f"Seleccionando tipo de reporte: {tipo}")
        self.fill(self.SELECT_TIPO_REPORTE, tipo)

    def generar_reporte(self, tipo_reporte, fecha_inicio, fecha_fin):
        """Flujo completo para generar un reporte"""
        logger.info(f"Generando reporte: {tipo_reporte} del {fecha_inicio} al {fecha_fin}")
        self.seleccionar_tipo_reporte(tipo_reporte)
        self.fill(self.SELECT_FECHA_INICIO, fecha_inicio)
        self.fill(self.SELECT_FECHA_FIN, fecha_fin)
        self.click(self.BTN_GENERAR)

    def exportar_reporte(self):
        """Exporta el reporte actual"""
        logger.info("Exportando reporte")
        self.click(self.BTN_EXPORTAR)

    def verificar_reporte_generado(self):
        """Verifica que el reporte se haya generado"""
        logger.info("Verificando que reporte fue generado")
        return self.is_element_visible(self.TABLA_RESULTADOS)
