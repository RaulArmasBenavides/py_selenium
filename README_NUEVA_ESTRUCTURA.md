# py_selenium - Estructura Profesional con POM

🎯 **Automated Testing con Selenium + Python + Pytest** usando **Page Object Model**, la estructura estándar en empresas grandes.

## ¿Qué Cambió?

### Antes ❌
```
tests/
├── test_add_owner.py      # Mezcla de tests y selectores
├── test_add_owner2.py     # Duplicación de código
└── test_add_owner_pet.py
```
**Problemas**: Duplicación, difícil de mantener, no escalable

### Ahora ✅ (Professional POM)
```
stracon/
├── pages/                 # Page Objects (selectores + métodos)
├── modules/
│   ├── asignacion_formatos/
│   │   ├── pages.py       # Page Object para este módulo
│   │   └── test_*.py      # Tests limpios y legibles
│   ├── reportes/
│   ├── tareos/
│   └── dashboard/
├── shared/                # Código reutilizable
└── config.py              # Configuración centralizada
```
**Ventajas**: Reutilizable, mantenible, escalable, profesional

## Instalación Rápida

```bash
# 1. Activar entorno virtual
.\env\Scripts\activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Configurar .env (edita URLs si es necesario)
# Debería estar listo por defecto
```

## Ejecutar Tests

```bash
# 📌 Todos los tests de STRACON
pytest stracon/ -v

# 📌 Solo Asignación de Formatos
pytest stracon/modules/asignacion_formatos/ -v

# 📌 Test específico
pytest stracon/modules/asignacion_formatos/test_asignacion_formatos.py::TestAsignacionFormatos::test_asignar_formato_exitoso

# 📌 Con logs visibles
pytest stracon/ -v -s

# 📌 Parar en primer fallo
pytest stracon/ -x

# 📌 Generar reporte HTML
pytest stracon/ --html=report.html
```

Ver más en `RUN_TESTS.md`

## Cómo Está Organizado

### 1. **config.py** - Configuración Centralizada
```python
STRACON_BASE_URL = os.getenv('STRACON_BASE_URL')
EXPLICIT_WAIT = int(os.getenv('EXPLICIT_WAIT', 20))
```
✅ Una sola fuente de verdad para URLs, timeouts, credenciales

### 2. **.env** - Variables de Entorno
```
STRACON_BASE_URL=https://refactor-straqui.stracon.com
EXPLICIT_WAIT=20
CHROME_HEADLESS=False
```
✅ Credenciales y URLs separadas del código (no commitear)

### 3. **pages/base_page.py** - Clase Base Reutilizable
```python
class BasePage:
    def click(self, locator)      # Click robusto con waits
    def fill(self, locator, text) # Fill con clear
    def get_text(self, locator)   # Obtener texto
    def take_screenshot()         # Captura
    # ... más métodos
```
✅ Todos los Page Objects heredan de aquí

### 4. **Módulos** - Organizados por Funcionalidad
Cada módulo tiene su propia carpeta con:

```
stracon/modules/asignacion_formatos/
├── pages.py                         # Page Object de este módulo
├── test_asignacion_formatos.py      # Tests
└── conftest.py (opcional)           # Fixtures locales
```

**pages.py**:
```python
class AsignacionFormatosPage(BasePage):
    TITULO = (By.XPATH, "//h1[...]")
    BTN_AGREGAR = (By.XPATH, "//button[...]")
    
    def asignar_formato(self, formato, usuario):
        self.click(self.BTN_AGREGAR)
        self.fill(self.CAMPO_FORMATO, formato)
        # ... más acciones
```

**test_asignacion_formatos.py**:
```python
class TestAsignacionFormatos:
    def test_asignar_formato_exitoso(self):
        self.page.asignar_formato("Formato A", "Juan")
        assert self.page.verificar_asignacion("Formato A", "Juan")
```

✅ Tests limpios, locators separados, reutilizable

## ¿Por Qué Page Object Model (POM)?

### Sin POM ❌
```python
def test_agregar():
    driver.find_element(By.XPATH, "//button[@id='agregar']").click()
    driver.find_element(By.ID, "nombre").send_keys("Juan")
    # ❌ Si cambia el HTML, hay que cambiar todos los tests
```

### Con POM ✅
```python
class FormPage(BasePage):
    BTN_AGREGAR = (By.XPATH, "//button[@id='agregar']")
    CAMPO_NOMBRE = (By.ID, "nombre")
    
    def agregar_con_nombre(self, nombre):
        self.click(self.BTN_AGREGAR)
        self.fill(self.CAMPO_NOMBRE, nombre)

def test_agregar():
    page.agregar_con_nombre("Juan")
    # ✅ Si cambia el HTML, cambias solo pages.py
```

**Ventajas POM**:
- 🔧 Cambios en UI en un solo lugar
- 📦 Código reutilizable
- 📖 Tests legibles como documentación
- 🚀 Fácil de mantener y escalar
- 👨‍💼 Estándar en empresas grandes (Google, Amazon, etc.)

## Ejemplo Completo: Crear un Nuevo Test

### 1. Crear carpeta del módulo
```bash
mkdir stracon/modules/nuevo_modulo
touch stracon/modules/nuevo_modulo/pages.py
touch stracon/modules/nuevo_modulo/test_nuevo_modulo.py
```

### 2. Crear **pages.py**
```python
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from shared.logger import get_logger

logger = get_logger(__name__)

class NuevoModuloPage(BasePage):
    TITULO = (By.XPATH, "//h1[contains(text(), 'Nuevo Módulo')]")
    BTN_ACCION = (By.ID, "btn_accion")
    CAMPO_ENTRADA = (By.ID, "entrada")
    TEXTO_RESULTADO = (By.CLASS_NAME, "resultado")
    
    def es_pagina_cargada(self):
        return self.is_element_visible(self.TITULO)
    
    def hacer_accion(self, valor):
        logger.info(f"Haciendo acción con valor: {valor}")
        self.click(self.BTN_ACCION)
        self.fill(self.CAMPO_ENTRADA, valor)
        
    def obtener_resultado(self):
        return self.get_text(self.TEXTO_RESULTADO)
```

### 3. Crear **test_nuevo_modulo.py**
```python
import pytest
from stracon.modules.nuevo_modulo.pages import NuevoModuloPage
from stracon.pages.sidebar_page import SidebarPage

class TestNuevoModulo:
    @pytest.fixture(autouse=True)
    def setup(self, stracon_driver):
        self.driver = stracon_driver
        self.page = NuevoModuloPage(self.driver)
        # Navega al módulo desde sidebar
        sidebar = SidebarPage(self.driver)
        sidebar.click_nuevo_modulo()  # (agrega este método en sidebar_page.py)
    
    def test_pagina_cargada(self):
        assert self.page.es_pagina_cargada()
    
    def test_hacer_accion(self):
        self.page.hacer_accion("valor_prueba")
        resultado = self.page.obtener_resultado()
        assert resultado == "esperado"
```

### 4. Ejecutar
```bash
pytest stracon/modules/nuevo_modulo/ -v
```

## Waits (Explícitos vs Implícitos)

### ✅ Explícitos (Recomendado)
```python
# En base_page.py automáticamente:
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(locator)
)
```

### ❌ Implícitos (Evitar)
```python
# ❌ NO HACER ESTO
driver.implicitly_wait(10)
time.sleep(2)  # ❌ JAMÁS
```

## Logging

Automático en cada Page Object:
```python
logger = get_logger(__name__)
logger.info("Navegando a tal módulo")
logger.warning("Elemento no encontrado")
```

Ver logs en consola:
```bash
pytest stracon/ -v -s
```

## Troubleshooting

| Problema | Solución |
|----------|----------|
| `ElementNotFound` | Revisa locators en `pages.py`, captura screenshot |
| Timeout | Aumenta `EXPLICIT_WAIT` en `.env` (default 20s) |
| Chrome no abre | Descarga ChromeDriver de https://googlechromelabs.github.io/chrome-for-testing/ |
| Tests lentos | Ejecuta en paralelo: `pytest -n auto` |

## Comandos Útiles

```bash
# Activar entorno
.\env\Scripts\activate

# Instalar/actualizar dependencias
pip install -r requirements.txt

# Run all tests
pytest stracon/

# Run con reporte
pytest stracon/ --html=report.html

# Run en headless (sin interfaz gráfica)
CHROME_HEADLESS=True pytest stracon/

# Run en paralelo
pytest stracon/ -n auto
```

## Archivos Importantes

| Archivo | Propósito |
|---------|-----------|
| `config.py` | Lee configuración desde `.env` |
| `.env` | Variables de entorno (URLs, timeouts, credenciales) |
| `conftest.py` | Fixtures globales (driver, setup/teardown) |
| `pytest.ini` | Configuración de pytest |
| `pages/base_page.py` | Métodos comunes para todas las páginas |
| `shared/logger.py` | Logging centralizado |
| `RUN_TESTS.md` | Guía detallada de cómo ejecutar tests |
| `CLAUDE.md` | Documentación técnica para Claude Code |

## Stack Tecnológico

```
✅ Selenium 4.15.2      - Automatización de navegador
✅ Pytest 7.4.3         - Framework de testing
✅ Python-dotenv 1.0.0  - Manejo de variables de entorno
✅ Pytest-xdist         - Ejecución en paralelo (opcional)
✅ Pytest-html          - Reportes HTML (opcional)
```

## Referencias

- 📚 [Selenium Documentation](https://selenium.dev/documentation/)
- 📚 [Pytest Documentation](https://docs.pytest.org/)
- 📚 [Page Object Model](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
- 🎓 [Google Testing Blog](https://testing.googleblog.com/)

---

**¿Preguntas?** Revisa `RUN_TESTS.md` para más comandos o `CLAUDE.md` para detalles técnicos.
