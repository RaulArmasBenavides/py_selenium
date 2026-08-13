"""
Páginas para el módulo Partes Diarios
Componentes: Elementos y Materiales (tabs)
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from shared.logger import get_logger

logger = get_logger(__name__)

class PartesDiariosPage(BasePage):
    """Página principal de Partes Diarios"""

    # Locators principales
    TITULO = (By.XPATH, "//h1[contains(text(), 'Partes Diarios')]")
    BTN_NUEVO = (By.XPATH, "//button[contains(text(), 'Nuevo')]")
    BTN_GUARDAR = (By.CSS_SELECTOR, "button[type='submit']")
    BTN_CANCELAR = (By.XPATH, "//button[contains(text(), 'Cancelar')]")
    LOADER = (By.XPATH, "//div[@class='spinner-loader']")

    # Tabs de Componentes
    TAB_ELEMENTOS = (By.XPATH, "//button[contains(text(), 'Elementos')]")
    TAB_MATERIALES = (By.XPATH, "//button[contains(text(), 'Materiales')]")
    CONTENEDOR_TABS = (By.XPATH, "//div[@role='tablist']")

    def is_page_loaded(self):
        """Verifica que la página esté cargada"""
        logger.info("Verificando que página esté cargada")
        return self.is_element_visible(self.TITULO)

    def click_nuevo(self):
        """Hace click en nuevo parte diario"""
        logger.info("Click en crear nuevo parte diario")
        self.click(self.BTN_NUEVO)

    def guardar_parte(self):
        """Guarda el parte diario"""
        logger.info("Guardando parte diario")
        self.click(self.BTN_GUARDAR)
        self.wait_for_loading(self.LOADER)

    def cancelar(self):
        """Cancela la operación"""
        logger.info("Cancelando")
        self.click(self.BTN_CANCELAR)

    def click_tab_elementos(self):
        """Navega al tab de Elementos"""
        logger.info("Click en tab 'Elementos'")
        self.click(self.TAB_ELEMENTOS)

    def click_tab_materiales(self):
        """Navega al tab de Materiales"""
        logger.info("Click en tab 'Materiales'")
        self.click(self.TAB_MATERIALES)

    def tabs_visibles(self):
        """Verifica que ambos tabs sean visibles"""
        logger.info("Verificando que los tabs estén visibles")
        return self.is_element_visible(self.CONTENEDOR_TABS)


class ElementosComponent(BasePage):
    """Componente: Tab de Elementos

    Gestiona los elementos del parte diario (herramientas, equipos, etc.)
    """

    # Locators del componente Elementos
    TAB_ELEMENTOS = (By.XPATH, "//button[contains(text(), 'Elementos')]")
    BTN_AGREGAR_ELEMENTO = (By.XPATH, "//button[contains(text(), 'Agregar Elemento')]")
    CAMPO_TIPO_ELEMENTO = (By.ID, "tipo_elemento")
    CAMPO_DESCRIPCION_ELEMENTO = (By.ID, "descripcion_elemento")
    CAMPO_CANTIDAD = (By.ID, "cantidad_elemento")
    CAMPO_ESTADO = (By.ID, "estado_elemento")
    TABLA_ELEMENTOS = (By.XPATH, "//table[@class='tabla-elementos']")
    FILA_ELEMENTO = (By.XPATH, "//table[@class='tabla-elementos']//tbody/tr")
    BTN_ELIMINAR_ELEMENTO = (By.XPATH, "//button[@title='Eliminar elemento']")
    MENSAJE_ELEMENTO_AGREGADO = (By.XPATH, "//span[contains(text(), 'Elemento agregado')]")

    def click_tab(self):
        """Navega al tab de Elementos"""
        logger.info("Accediendo a tab Elementos")
        self.click(self.TAB_ELEMENTOS)

    def agregar_elemento(self, tipo, descripcion, cantidad, estado="Disponible"):
        """Flujo completo: agregar un nuevo elemento

        Args:
            tipo: Tipo de elemento (Herramienta, Equipo, etc.)
            descripcion: Descripción del elemento
            cantidad: Cantidad del elemento
            estado: Estado (Disponible, Mantenimiento, Dañado)
        """
        logger.info(f"Agregando elemento: {tipo} - {descripcion}")

        self.click(self.BTN_AGREGAR_ELEMENTO)
        self.fill(self.CAMPO_TIPO_ELEMENTO, tipo)
        self.fill(self.CAMPO_DESCRIPCION_ELEMENTO, descripcion)
        self.fill(self.CAMPO_CANTIDAD, cantidad)
        self.fill(self.CAMPO_ESTADO, estado)

    def obtener_cantidad_elementos(self):
        """Retorna la cantidad de elementos agregados"""
        logger.info("Obteniendo cantidad de elementos")
        elementos = self.driver.find_elements(*self.FILA_ELEMENTO)
        return len(elementos)

    def verificar_elemento_existe(self, descripcion):
        """Verifica si un elemento existe en la tabla"""
        logger.info(f"Verificando si existe elemento: {descripcion}")
        return self.is_text_present(descripcion)

    def verificar_elemento_agregado(self):
        """Verifica que aparezca el mensaje de éxito"""
        logger.info("Verificando mensaje de elemento agregado")
        return self.is_element_visible(self.MENSAJE_ELEMENTO_AGREGADO)

    def obtener_elementos_tabla(self):
        """Obtiene lista de elementos de la tabla"""
        logger.info("Obteniendo elementos de la tabla")
        elementos = []
        filas = self.driver.find_elements(*self.FILA_ELEMENTO)
        for fila in filas:
            celdas = fila.find_elements(By.TAG_NAME, "td")
            if len(celdas) >= 2:
                elementos.append({
                    'tipo': celdas[0].text,
                    'descripcion': celdas[1].text,
                })
        return elementos


class MaterialesComponent(BasePage):
    """Componente: Tab de Materiales

    Gestiona los materiales del parte diario (consumibles, repuestos, etc.)
    """

    # Locators del componente Materiales
    TAB_MATERIALES = (By.XPATH, "//button[contains(text(), 'Materiales')]")
    BTN_AGREGAR_MATERIAL = (By.XPATH, "//button[contains(text(), 'Agregar Material')]")
    CAMPO_NOMBRE_MATERIAL = (By.ID, "nombre_material")
    CAMPO_TIPO_MATERIAL = (By.ID, "tipo_material")
    CAMPO_CANTIDAD_MATERIAL = (By.ID, "cantidad_material")
    CAMPO_UNIDAD = (By.ID, "unidad_material")
    CAMPO_PROVEEDOR = (By.ID, "proveedor")
    TABLA_MATERIALES = (By.XPATH, "//table[@class='tabla-materiales']")
    FILA_MATERIAL = (By.XPATH, "//table[@class='tabla-materiales']//tbody/tr")
    BTN_ELIMINAR_MATERIAL = (By.XPATH, "//button[@title='Eliminar material']")
    MENSAJE_MATERIAL_AGREGADO = (By.XPATH, "//span[contains(text(), 'Material agregado')]")

    def click_tab(self):
        """Navega al tab de Materiales"""
        logger.info("Accediendo a tab Materiales")
        self.click(self.TAB_MATERIALES)

    def agregar_material(self, nombre, tipo, cantidad, unidad, proveedor=None):
        """Flujo completo: agregar un nuevo material

        Args:
            nombre: Nombre del material
            tipo: Tipo de material (Consumible, Repuesto, etc.)
            cantidad: Cantidad del material
            unidad: Unidad (Metros, Kilos, Litros, etc.)
            proveedor: Proveedor (opcional)
        """
        logger.info(f"Agregando material: {nombre} - {tipo}")

        self.click(self.BTN_AGREGAR_MATERIAL)
        self.fill(self.CAMPO_NOMBRE_MATERIAL, nombre)
        self.fill(self.CAMPO_TIPO_MATERIAL, tipo)
        self.fill(self.CAMPO_CANTIDAD_MATERIAL, cantidad)
        self.fill(self.CAMPO_UNIDAD, unidad)
        if proveedor:
            self.fill(self.CAMPO_PROVEEDOR, proveedor)

    def obtener_cantidad_materiales(self):
        """Retorna la cantidad de materiales agregados"""
        logger.info("Obteniendo cantidad de materiales")
        materiales = self.driver.find_elements(*self.FILA_MATERIAL)
        return len(materiales)

    def verificar_material_existe(self, nombre):
        """Verifica si un material existe en la tabla"""
        logger.info(f"Verificando si existe material: {nombre}")
        return self.is_text_present(nombre)

    def verificar_material_agregado(self):
        """Verifica que aparezca el mensaje de éxito"""
        logger.info("Verificando mensaje de material agregado")
        return self.is_element_visible(self.MENSAJE_MATERIAL_AGREGADO)

    def obtener_materiales_tabla(self):
        """Obtiene lista de materiales de la tabla"""
        logger.info("Obteniendo materiales de la tabla")
        materiales = []
        filas = self.driver.find_elements(*self.FILA_MATERIAL)
        for fila in filas:
            celdas = fila.find_elements(By.TAG_NAME, "td")
            if len(celdas) >= 2:
                materiales.append({
                    'nombre': celdas[0].text,
                    'tipo': celdas[1].text,
                })
        return materiales
