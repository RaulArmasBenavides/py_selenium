# Checklist: Crear un Nuevo Test

Usa este checklist cuando quieras agregar un nuevo test a la suite.

## 1️⃣ Preparación

- [ ] Identificar a qué módulo pertenece el test
  - ¿Es Asignación de Formatos? → `stracon/modules/asignacion_formatos/`
  - ¿Es un nuevo módulo? → Crear carpeta nueva: `stracon/modules/nuevo_modulo/`

- [ ] Analizar la página/funcionalidad en el navegador
  - Abre DevTools (F12)
  - Identifica los selectores (IDs, XPaths, CSS selectors)
  - Documenta qué acciones hace el usuario

## 2️⃣ Crear Page Object (pages.py)

```python
# stracon/modules/mi_modulo/pages.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from shared.logger import get_logger

logger = get_logger(__name__)

class MiModuloPage(BasePage):
    # Locators (selectores)
    TITULO = (By.XPATH, "//h1[contains(text(), 'Mi Módulo')]")
    BTN_ACCION = (By.ID, "btn_id")
    CAMPO_INPUT = (By.ID, "input_id")
    
    # Métodos de navegación/interacción
    def es_pagina_cargada(self):
        """Verifica que la página esté cargada"""
        logger.info("Verificando página")
        return self.is_element_visible(self.TITULO)
    
    def hacer_algo(self, valor):
        """Flujo: hacer algo con valor"""
        logger.info(f"Haciendo algo con: {valor}")
        self.click(self.BTN_ACCION)
        self.fill(self.CAMPO_INPUT, valor)
```

Checklist de pages.py:
- [ ] Hereda de `BasePage`
- [ ] Importa `By` y logger
- [ ] Todos los selectores son constantes MAYÚSCULAS
- [ ] Métodos documentados con docstrings
- [ ] Métodos usan `self.click()`, `self.fill()`, etc. de BasePage
- [ ] Logs importantes con `logger.info()`

## 3️⃣ Crear Test File (test_*.py)

```python
# stracon/modules/mi_modulo/test_mi_modulo.py

import pytest
from stracon.modules.mi_modulo.pages import MiModuloPage
from stracon.pages.sidebar_page import SidebarPage
from shared.logger import get_logger

logger = get_logger(__name__)

class TestMiModulo:
    """Suite de tests para Mi Módulo"""
    
    @pytest.fixture(autouse=True)
    def setup(self, stracon_driver):
        """Setup: navega al módulo"""
        self.driver = stracon_driver
        self.page = MiModuloPage(self.driver)
        
        # Navega al módulo desde sidebar
        sidebar = SidebarPage(self.driver)
        sidebar.click_mi_modulo()  # (debe existir en sidebar_page.py)
        
        logger.info("Setup completado")
    
    def test_pagina_cargada(self):
        """TEST: Verificar que la página carga correctamente"""
        assert self.page.es_pagina_cargada(), "Página no cargó"
    
    def test_hacer_algo_exitoso(self):
        """TEST: Hacer algo y verificar resultado"""
        # Arrange
        valor_esperado = "algo"
        
        # Act
        self.page.hacer_algo(valor_esperado)
        
        # Assert
        assert self.page.is_text_present(valor_esperado)
    
    @pytest.mark.parametrize("entrada,esperado", [
        ("valor1", "resultado1"),
        ("valor2", "resultado2"),
    ])
    def test_parametrizado(self, entrada, esperado):
        """TEST: Probar múltiples valores"""
        self.page.hacer_algo(entrada)
        assert self.page.is_text_present(esperado)
```

Checklist de test_*.py:
- [ ] Nombre empieza con `test_`
- [ ] Hereda de la clase test (ej: `TestMiModulo`)
- [ ] `setup()` fixture con `autouse=True`
- [ ] Crea instancia de Page Object
- [ ] Navega al módulo con Sidebar
- [ ] Cada test tiene un propósito claro (documentado)
- [ ] Tests siguen patrón Arrange-Act-Assert
- [ ] Tests son independientes (no dependen uno de otro)
- [ ] Usa parametrize para múltiples casos

## 4️⃣ Agregar Navegación en Sidebar

Si es un **nuevo módulo**, necesitas agregar el botón en `stracon/pages/sidebar_page.py`:

```python
# En stracon/pages/sidebar_page.py

class SidebarPage(BasePage):
    # Agrega locator
    MI_MODULO = (By.XPATH, "//span[contains(text(), 'Mi Módulo')]")
    
    # Agrega método
    def click_mi_modulo(self):
        """Navega a Mi Módulo"""
        logger.info("Navegando a Mi Módulo")
        self.click(self.MI_MODULO)
```

- [ ] Locator agregado en `sidebar_page.py`
- [ ] Método agregado en `sidebar_page.py`

## 5️⃣ Ejecutar y Verificar

```bash
# Activar entorno
.\env\Scripts\activate

# Ejecutar solo tu nuevo test
pytest stracon/modules/mi_modulo/test_mi_modulo.py -v -s

# Ejecutar con debug
pytest stracon/modules/mi_modulo/test_mi_modulo.py -v -s --tb=short

# Si falla, captura screenshot
pytest stracon/modules/mi_modulo/test_mi_modulo.py -v -s --capture=no
```

Checklist de ejecución:
- [ ] Test pasa ✓
- [ ] Logs se ven en consola
- [ ] Screenshot se captura en caso de fallo
- [ ] Test es reproducible (pasa siempre)

## 6️⃣ Mejora Continuada

Después de que funcione:

- [ ] ¿Hay código duplicado? → Agregar a `BasePage` o `shared/helpers.py`
- [ ] ¿Test es lento? → Revisar waits, optimizar
- [ ] ¿Test es flaky (falla aleatoriamente)? → Mejorar waits o revisar locators
- [ ] ¿Necesita fixtures extras? → Agregar a `conftest.py`

## Estructura Mínima

Para un test nuevo necesitas **mínimo**:

```
stracon/modules/nuevo_modulo/
├── __init__.py
├── pages.py           ← Locators + métodos (30-50 líneas)
└── test_nuevo_modulo.py  ← Tests (20-40 líneas)
```

## Ejemplo Real Completo

### Archivos Necesarios:

**1. stracon/modules/login/pages.py**
```python
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    CAMPO_EMAIL = (By.ID, "email")
    CAMPO_PASSWORD = (By.ID, "password")
    BTN_LOGIN = (By.XPATH, "//button[contains(text(), 'Login')]")
    MENSAJE_ERROR = (By.CLASS_NAME, "error-message")
    
    def login(self, email, password):
        self.fill(self.CAMPO_EMAIL, email)
        self.fill(self.CAMPO_PASSWORD, password)
        self.click(self.BTN_LOGIN)
    
    def obtener_error(self):
        return self.get_text(self.MENSAJE_ERROR)
```

**2. stracon/modules/login/test_login.py**
```python
import pytest
from stracon.modules.login.pages import LoginPage

class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, stracon_driver):
        self.driver = stracon_driver
        self.page = LoginPage(self.driver)
    
    def test_login_correcto(self):
        self.page.login("user@test.com", "password123")
        assert "Dashboard" in self.driver.page_source
    
    def test_login_incorrecto(self):
        self.page.login("user@test.com", "wrong")
        error = self.page.obtener_error()
        assert "credenciales" in error.lower()
```

**3. Ejecutar:**
```bash
pytest stracon/modules/login/ -v
```

✅ ¡Listo! Ya tienes un test profesional.

## Tips Profesionales

✨ **Naming**:
- Tests: `test_<que_hace>_<resultado_esperado>` (test_login_correcto)
- Pages: `<ModuloName>Page` (LoginPage)
- Métodos: `<verbo>_<que>` (obtener_error, hacer_login)

✨ **Locators**:
- Prefiere IDs (`By.ID`) si existen
- Luego XPath más específicos
- Evita selectores basados en orden o CSS complejos

✨ **Waits**:
- Nunca uses `time.sleep()`
- Siempre `WebDriverWait` (automático en BasePage)

✨ **Assertions**:
- Una assertion por test (idealmente)
- O máximo 2-3 relacionadas

✨ **Dados/Data**:
- Usa fixtures para datos compartidos
- Parametrize para múltiples casos
- Evita hardcoding en tests

---

**Preguntas?** Ver:
- `README_NUEVA_ESTRUCTURA.md` - Guía general
- `RUN_TESTS.md` - Cómo ejecutar
- `CLAUDE.md` - Documentación técnica
