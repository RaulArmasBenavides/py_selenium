"""
Tests para Asignación de Formatos
"""
import pytest
from stracon.modules.asignacion_formatos.pages import AsignacionFormatosPage
from stracon.pages.sidebar_page import SidebarPage
from shared.logger import get_logger

logger = get_logger(__name__)

class TestAsignacionFormatos:
    """Suite de tests para Asignación de Formatos"""

    @pytest.fixture(autouse=True)
    def setup(self, stracon_driver):
        """Setup para cada test"""
        self.driver = stracon_driver
        self.sidebar = SidebarPage(self.driver)
        self.asignacion_page = AsignacionFormatosPage(self.driver)

        # Navega al módulo
        logger.info("Navegando al módulo Asignación de Formatos")
        self.sidebar.click_asignacion_formatos()

    def test_pagina_cargada(self):
        """Verifica que la página de asignación se cargue correctamente"""
        assert self.asignacion_page.is_page_loaded(), "La página no se cargó"

    def test_asignar_formato_exitoso(self):
        """Test: Asignar un formato a un usuario correctamente"""
        # Arrange
        formato = "Formato A"
        usuario = "Juan Pérez"

        # Act
        self.asignacion_page.asignar_formato(formato, usuario)

        # Assert
        assert self.asignacion_page.verificar_mensaje_exito(), "No se mostró mensaje de éxito"
        assert self.asignacion_page.verificar_asignacion(formato, usuario), "No se verificó la asignación"

    def test_asignar_formato_con_fecha(self):
        """Test: Asignar un formato con fecha específica"""
        # Arrange
        formato = "Formato B"
        usuario = "María García"
        fecha = "2026-08-15"

        # Act
        self.asignacion_page.asignar_formato(formato, usuario, fecha)

        # Assert
        assert self.asignacion_page.verificar_asignacion(formato, usuario)

    @pytest.mark.parametrize("formato,usuario", [
        ("Formato A", "Juan Pérez"),
        ("Formato B", "María García"),
        ("Formato C", "Carlos López"),
    ])
    def test_asignar_multiples_formatos(self, formato, usuario):
        """Test parameterizado: Asignar múltiples formatos a diferentes usuarios"""
        self.asignacion_page.asignar_formato(formato, usuario)
        assert self.asignacion_page.verificar_asignacion(formato, usuario)
