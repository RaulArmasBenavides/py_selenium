"""
Tests para Partes Diarios
Incluye tests para componentes: Elementos y Materiales (tabs)
"""
import pytest
from stracon.modules.partes_diarios.pages import (
    PartesDiariosPage,
    ElementosComponent,
    MaterialesComponent
)
from stracon.pages.sidebar_page import SidebarPage
from shared.logger import get_logger

logger = get_logger(__name__)


class TestPartesDiariosBasico:
    """Suite básica de Partes Diarios"""

    @pytest.fixture(autouse=True)
    def setup(self, stracon_driver):
        """Setup: navega al módulo"""
        self.driver = stracon_driver
        self.page = PartesDiariosPage(self.driver)

        # Navega al módulo desde sidebar
        sidebar = SidebarPage(self.driver)
        sidebar.click_partes_diarios()

        logger.info("Setup completado")

    def test_pagina_cargada(self):
        """TEST: Verificar que la página carga correctamente"""
        assert self.page.is_page_loaded(), "Página de Partes Diarios no cargó"

    def test_tabs_visibles(self):
        """TEST: Verificar que los tabs de componentes estén visibles"""
        assert self.page.tabs_visibles(), "Los tabs no son visibles"

    def test_navegar_tab_elementos(self):
        """TEST: Navegar al tab Elementos"""
        self.page.click_tab_elementos()
        # Verificar que el tab está activo
        assert "Elementos" in self.driver.page_source

    def test_navegar_tab_materiales(self):
        """TEST: Navegar al tab Materiales"""
        self.page.click_tab_materiales()
        # Verificar que el tab está activo
        assert "Materiales" in self.driver.page_source


class TestElementos:
    """Suite de tests para el componente Elementos (tab)"""

    @pytest.fixture(autouse=True)
    def setup(self, stracon_driver):
        """Setup: navega al módulo y tab Elementos"""
        self.driver = stracon_driver
        self.parte_page = PartesDiariosPage(self.driver)
        self.elementos = ElementosComponent(self.driver)

        # Navega al módulo
        sidebar = SidebarPage(self.driver)
        sidebar.click_partes_diarios()

        # Navega al tab Elementos
        self.parte_page.click_tab_elementos()

        logger.info("Setup completado - Tab Elementos")

    def test_agregar_elemento_herramienta(self):
        """TEST: Agregar una herramienta al parte diario"""
        # Arrange
        tipo = "Herramienta"
        descripcion = "Taladro Eléctrico"
        cantidad = "1"

        # Act
        self.elementos.agregar_elemento(tipo, descripcion, cantidad)
        self.parte_page.guardar_parte()

        # Assert
        assert self.elementos.verificar_elemento_agregado(), "Elemento no se agregó"
        assert self.elementos.verificar_elemento_existe(descripcion), "No se verificó el elemento"

    def test_agregar_elemento_equipo(self):
        """TEST: Agregar un equipo al parte diario"""
        tipo = "Equipo"
        descripcion = "Compresor de Aire"
        cantidad = "1"

        self.elementos.agregar_elemento(tipo, descripcion, cantidad)
        assert self.elementos.verificar_elemento_existe(descripcion)

    @pytest.mark.parametrize("tipo,descripcion,cantidad,estado", [
        ("Herramienta", "Taladro", "1", "Disponible"),
        ("Herramienta", "Sierra Circular", "1", "Disponible"),
        ("Equipo", "Compresor", "2", "Mantenimiento"),
        ("Herramienta", "Martillo", "5", "Disponible"),
    ])
    def test_agregar_multiples_elementos(self, tipo, descripcion, cantidad, estado):
        """TEST parameterizado: Agregar múltiples elementos"""
        self.elementos.agregar_elemento(tipo, descripcion, cantidad, estado)
        assert self.elementos.verificar_elemento_existe(descripcion)

    def test_obtener_cantidad_elementos(self):
        """TEST: Obtener cantidad de elementos en la tabla"""
        # Agregar algunos elementos
        self.elementos.agregar_elemento("Herramienta", "Elemento 1", "1")
        self.elementos.agregar_elemento("Herramienta", "Elemento 2", "1")

        # Obtener cantidad
        cantidad = self.elementos.obtener_cantidad_elementos()
        assert cantidad >= 2, f"Se esperaban al menos 2 elementos, se encontraron {cantidad}"

    def test_obtener_lista_elementos(self):
        """TEST: Obtener lista completa de elementos"""
        # Agregar elementos
        self.elementos.agregar_elemento("Herramienta", "Taladro", "1")
        self.elementos.agregar_elemento("Equipo", "Compresor", "1")

        # Obtener lista
        elementos = self.elementos.obtener_elementos_tabla()
        assert len(elementos) >= 2
        assert any(e['descripcion'] == "Taladro" for e in elementos)


class TestMateriales:
    """Suite de tests para el componente Materiales (tab)"""

    @pytest.fixture(autouse=True)
    def setup(self, stracon_driver):
        """Setup: navega al módulo y tab Materiales"""
        self.driver = stracon_driver
        self.parte_page = PartesDiariosPage(self.driver)
        self.materiales = MaterialesComponent(self.driver)

        # Navega al módulo
        sidebar = SidebarPage(self.driver)
        sidebar.click_partes_diarios()

        # Navega al tab Materiales
        self.parte_page.click_tab_materiales()

        logger.info("Setup completado - Tab Materiales")

    def test_agregar_material_consumible(self):
        """TEST: Agregar un material consumible"""
        # Arrange
        nombre = "Tubo PVC"
        tipo = "Consumible"
        cantidad = "50"
        unidad = "Metros"

        # Act
        self.materiales.agregar_material(nombre, tipo, cantidad, unidad)
        self.parte_page.guardar_parte()

        # Assert
        assert self.materiales.verificar_material_agregado(), "Material no se agregó"
        assert self.materiales.verificar_material_existe(nombre), "No se verificó el material"

    def test_agregar_material_repuesto(self):
        """TEST: Agregar un material repuesto"""
        nombre = "Rodamiento SKF 6205"
        tipo = "Repuesto"
        cantidad = "4"
        unidad = "Unidad"
        proveedor = "Proveedores Industriales S.A."

        self.materiales.agregar_material(nombre, tipo, cantidad, unidad, proveedor)
        assert self.materiales.verificar_material_existe(nombre)

    @pytest.mark.parametrize("nombre,tipo,cantidad,unidad", [
        ("Tubo PVC 1 inch", "Consumible", "50", "Metros"),
        ("Codo 90 PVC", "Repuesto", "20", "Unidad"),
        ("Sellador", "Consumible", "5", "Litros"),
        ("Válvula Esférica", "Repuesto", "10", "Unidad"),
    ])
    def test_agregar_multiples_materiales(self, nombre, tipo, cantidad, unidad):
        """TEST parameterizado: Agregar múltiples materiales"""
        self.materiales.agregar_material(nombre, tipo, cantidad, unidad)
        assert self.materiales.verificar_material_existe(nombre)

    def test_obtener_cantidad_materiales(self):
        """TEST: Obtener cantidad de materiales en la tabla"""
        # Agregar materiales
        self.materiales.agregar_material("Material 1", "Consumible", "10", "Metros")
        self.materiales.agregar_material("Material 2", "Repuesto", "5", "Unidad")

        # Obtener cantidad
        cantidad = self.materiales.obtener_cantidad_materiales()
        assert cantidad >= 2

    def test_obtener_lista_materiales(self):
        """TEST: Obtener lista completa de materiales"""
        # Agregar materiales
        self.materiales.agregar_material("Tubo PVC", "Consumible", "50", "Metros")
        self.materiales.agregar_material("Rodamiento", "Repuesto", "4", "Unidad")

        # Obtener lista
        materiales = self.materiales.obtener_materiales_tabla()
        assert len(materiales) >= 2
        assert any(m['nombre'] == "Tubo PVC" for m in materiales)


class TestIntegracionElementosYMateriales:
    """Tests de integración: Elementos + Materiales en un mismo parte"""

    @pytest.fixture(autouse=True)
    def setup(self, stracon_driver):
        """Setup: navega al módulo"""
        self.driver = stracon_driver
        self.parte_page = PartesDiariosPage(self.driver)
        self.elementos = ElementosComponent(self.driver)
        self.materiales = MaterialesComponent(self.driver)

        # Navega al módulo
        sidebar = SidebarPage(self.driver)
        sidebar.click_partes_diarios()

    def test_crear_parte_completo_elementos_y_materiales(self):
        """TEST: Crear un parte diario completo con elementos y materiales"""
        # Step 1: Agregar Elementos
        self.parte_page.click_tab_elementos()
        self.elementos.agregar_elemento("Herramienta", "Taladro", "1", "Disponible")
        self.elementos.agregar_elemento("Equipo", "Compresor", "1", "Disponible")

        # Verificar elementos agregados
        assert self.elementos.obtener_cantidad_elementos() >= 2

        # Step 2: Navegar a Materiales
        self.parte_page.click_tab_materiales()
        self.materiales.agregar_material("Tubo PVC", "Consumible", "50", "Metros")
        self.materiales.agregar_material("Rodamiento", "Repuesto", "4", "Unidad")

        # Verificar materiales agregados
        assert self.materiales.obtener_cantidad_materiales() >= 2

        # Step 3: Guardar parte completo
        self.parte_page.guardar_parte()

        # Verificar que se guardó correctamente
        assert "Parte guardado" in self.driver.page_source

    def test_navegar_entre_tabs_mantiene_datos(self):
        """TEST: Navegar entre tabs mantiene los datos ingresados"""
        # Agregar elemento
        self.parte_page.click_tab_elementos()
        self.elementos.agregar_elemento("Herramienta", "Taladro", "1")

        # Navegar a Materiales
        self.parte_page.click_tab_materiales()
        self.materiales.agregar_material("Tubo PVC", "Consumible", "50", "Metros")

        # Volver a Elementos
        self.parte_page.click_tab_elementos()
        assert self.elementos.verificar_elemento_existe("Taladro"), "El elemento se perdió"

        # Volver a Materiales
        self.parte_page.click_tab_materiales()
        assert self.materiales.verificar_material_existe("Tubo PVC"), "El material se perdió"
