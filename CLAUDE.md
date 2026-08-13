# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**py_selenium** is a professional automated browser testing suite using Selenium with Python and Pytest, following enterprise best practices with **Page Object Model (POM)** architecture. It tests multiple web applications:

- **STRACON App**: Enterprise application with multiple modules (Configuraciones, Asignación de Formatos, Reportes, etc.)
- **Examples**: Spring Petclinic (reference/legacy tests kept for learning)

## Architecture & Structure (Professional POM)

### Directory Structure
```
py_selenium/
├── config.py                 # Configuración centralizada (lee desde .env)
├── conftest.py              # Fixtures globales
├── .env                      # Variables de entorno (URLs, credenciales, timeouts)
├── pytest.ini               # Configuración de pytest
├── requirements.txt         # Dependencias Python
│
├── pages/                    # Componentes reutilizables
│   ├── base_page.py         # Clase base con métodos comunes
│   └── sidebar_page.py      # Componentes compartidas
│
├── shared/                   # Utilidades compartidas
│   ├── logger.py            # Logging centralizado
│   └── helpers.py           # Funciones auxiliares
│
├── stracon/                  # APP PRINCIPAL: STRACON
│   ├── conftest.py          # Fixtures específicas de STRACON
│   ├── pages/
│   │   └── sidebar_page.py  # Navegación del sidebar
│   └── modules/             # Cada módulo es una carpeta
│       ├── asignacion_formatos/
│       │   ├── pages.py             # Page Objects para este módulo
│       │   └── test_asignacion_formatos.py
│       ├── reportes/
│       ├── tareos/
│       └── dashboard/
│
└── examples/                 # Tests de referencia (legacy)
    ├── petclinic_cloud.py   # Ejemplo antiguo - para referencia
    └── petclinic_angular.py
```

### Key Architectural Patterns

#### 1. **Page Object Model (POM)**
- Cada página/módulo tiene una clase que hereda de `BasePage`
- Locators y métodos están separados de los tests
- Cambios en UI solo afectan las páginas, no los tests
- Ejemplo: `stracon/modules/asignacion_formatos/pages.py`

#### 2. **Base Page Class** (`pages/base_page.py`)
Métodos reutilizables para toda interacción:
```python
self.click(locator)           # Click con wait
self.fill(locator, text)      # Fill con clear
self.get_text(locator)        # Get text
self.is_element_visible()     # Verificar visibilidad
self.is_text_present()        # Verificar texto en página
self.take_screenshot()        # Captura
```

#### 3. **Explicit Waits**
Todos usan `WebDriverWait` con `expected_conditions`:
- Links/botones: `EC.element_to_be_clickable()`
- Inputs: `EC.presence_of_element_located()`
- Textos: Verificar en `page_source`

#### 4. **Modular Organization**
- Cada módulo es independiente
- Puede tener su propio `conftest.py` con fixtures
- Los tests son específicos del módulo
- Fácil agregar nuevos módulos

## Development Setup

### Prerequisites
- Python 3.8+
- Chrome browser
- ChromeDriver (matching Chrome version)

### Initial Setup
```bash
# Create and activate virtual environment
py -m venv env
.\env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Verify .env exists with your URLs and credentials
# Edit .env if needed:
# - STRACON_BASE_URL=https://refactor-straqui.stracon.com
# - EXPLICIT_WAIT=20 (aumentar si conexión lenta)
```

## Common Commands

### Run Tests
```bash
.\env\Scripts\activate

# All STRACON tests
pytest stracon/

# Specific module
pytest stracon/modules/asignacion_formatos/

# Specific test
pytest stracon/modules/asignacion_formatos/test_asignacion_formatos.py::TestAsignacionFormatos::test_asignar_formato_exitoso

# With verbose output
pytest stracon/ -v

# Show prints/logs
pytest stracon/ -v -s

# Stop on first failure
pytest stracon/ -x

# Parallel execution
pytest stracon/ -n auto

# Generate HTML report
pytest stracon/ --html=report.html
```

## Creating New Tests

### Template for New Module

1. **Create module folder**:
   ```
   stracon/modules/new_module/
   ├── pages.py
   └── test_new_module.py
   ```

2. **pages.py**:
   ```python
   from pages.base_page import BasePage
   from selenium.webdriver.common.by import By
   
   class NewModulePage(BasePage):
       LOCATOR_EJEMPLO = (By.ID, "elemento")
       
       def mi_accion(self):
           self.click(self.LOCATOR_EJEMPLO)
   ```

3. **test_new_module.py**:
   ```python
   from stracon.modules.new_module.pages import NewModulePage
   from stracon.pages.sidebar_page import SidebarPage
   
   class TestNewModule:
       @pytest.fixture(autouse=True)
       def setup(self, stracon_driver):
           self.page = NewModulePage(stracon_driver)
           SidebarPage(stracon_driver).click_new_module()
       
       def test_algo(self):
           self.page.mi_accion()
           assert self.page.is_text_present("resultado esperado")
   ```

## Configuration (.env)

- `STRACON_BASE_URL`: URL de STRACON a testear
- `EXPLICIT_WAIT`: Timeout para waits (default 20s)
- `CHROME_HEADLESS`: True para correr sin interfaz gráfica
- `LOG_LEVEL`: INFO, DEBUG, WARNING, ERROR

## Important Implementation Notes

- **Fixtures**: Scoped por sesión para performance. Usa `reset_session` para limpiar cookies
- **Logging**: Usa `get_logger(__name__)` en cada archivo para tracking
- **Screenshots**: `self.page.take_screenshot('nombre.png')` en assertions fallidas
- **Waits**: Nunca hardcodear `.sleep()` - siempre usar `WebDriverWait`
- **Test Data**: Mantén parametrizado con `@pytest.mark.parametrize`

## Files Reference

- `config.py`: Centraliza todas las configuraciones (URLs, timeouts)
- `.env`: Variables de entorno (no commitear credenciales reales)
- `pages/base_page.py`: Métodos base para todas las páginas
- `shared/logger.py`: Logging centralizado
- `conftest.py`: Fixtures globales (driver, setup/teardown)
- `pytest.ini`: Configuración de pytest (testpaths, markers, opciones)
