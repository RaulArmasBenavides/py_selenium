# 🚀 START HERE - Comienza Aquí

Bienvenido a la **estructura profesional de testing** con Selenium, Python y Pytest.

## ⚡ Comienza en 2 Minutos

```bash
# 1. Activar entorno virtual
.\env\Scripts\activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar tests
pytest stracon/ -v
```

✅ ¡Listo! Los tests empezarán a ejecutarse.

---

## 📚 Documentación (Elige Tu Camino)

### 🟢 Si Eres Nuevo en Testing
1. Empieza por: **[README_NUEVA_ESTRUCTURA.md](README_NUEVA_ESTRUCTURA.md)** - Explicación general con ejemplos
2. Luego: **[CHECKLIST_NUEVO_TEST.md](CHECKLIST_NUEVO_TEST.md)** - Cómo crear un test nuevo

### 🟡 Si Quieres Ejecutar Tests Ya
1. Ve a: **[COMANDOS_RAPIDOS.md](COMANDOS_RAPIDOS.md)** - Referencia rápida de comandos
2. O: **[RUN_TESTS.md](RUN_TESTS.md)** - Guía detallada de ejecución

### 🔵 Si Quieres Entender la Arquitectura
1. Lee: **[ESTRUCTURA_DEL_PROYECTO.txt](ESTRUCTURA_DEL_PROYECTO.txt)** - Explicación de carpetas
2. O: **[ARBOL_COMPLETO.txt](ARBOL_COMPLETO.txt)** - Árbol visual del proyecto

### ⚫ Si Eres Desarrollador/Técnico
1. Consulta: **[CLAUDE.md](CLAUDE.md)** - Documentación técnica completa

---

## 🎯 Guía Rápida por Tarea

### "Quiero ejecutar los tests"
```bash
pytest stracon/ -v
# Ver más opciones en: COMANDOS_RAPIDOS.md
```

### "Quiero crear un nuevo test"
```
1. Abre: CHECKLIST_NUEVO_TEST.md
2. Crea carpeta: stracon/modules/nuevo_modulo/
3. Crea: pages.py (Page Objects)
4. Crea: test_nuevo_modulo.py (Tests)
5. Ejecuta: pytest stracon/modules/nuevo_modulo/ -v
```

### "Quiero entender la estructura"
```
1. Lee: ESTRUCTURA_DEL_PROYECTO.txt
2. Ve: ARBOL_COMPLETO.txt
3. Consulta: CLAUDE.md
```

### "Algo no funciona"
```
1. Revisa: RUN_TESTS.md (sección Troubleshooting)
2. O: COMANDOS_RAPIDOS.md (troubleshooting table)
```

---

## 📁 Estructura del Proyecto

```
py_selenium/
├── config.py                    ← Configuración centralizada
├── .env                         ← Variables de entorno
├── conftest.py                  ← Fixtures globales
├── requirements.txt             ← Dependencias
│
├── pages/                       ← Componentes base
│   └── base_page.py            ← Métodos comunes
│
├── shared/                      ← Código compartido
│   ├── logger.py               ← Logging
│   └── helpers.py              ← Funciones auxiliares
│
├── stracon/                     ← APP PRINCIPAL
│   └── modules/
│       ├── asignacion_formatos/
│       │   ├── pages.py        ← Page Objects
│       │   └── test_*.py       ← Tests
│       └── reportes/
│           ├── pages.py
│           └── test_*.py
│
└── examples/                    ← Ejemplos (referencia)
    └── petclinic_cloud.py
```

---

## 🔥 Los 3 Conceptos Clave

### 1️⃣ Page Object Model (POM)
Separa **selectores** de **tests**.

❌ Antes:
```python
driver.find_element(By.ID, "email").send_keys("user")  # En el test
```

✅ Ahora:
```python
# En pages.py
class LoginPage(BasePage):
    CAMPO_EMAIL = (By.ID, "email")
    def fill_email(self, email):
        self.fill(self.CAMPO_EMAIL, email)

# En test
page.fill_email("user")
```

### 2️⃣ Waits Explícitos
Nunca uses `time.sleep()`.

```python
# ❌ NO
import time
time.sleep(2)

# ✅ SÍ
from selenium.webdriver.support.ui import WebDriverWait
element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(locator))
```

### 3️⃣ Fixtures de Pytest
Setup/teardown automático.

```python
@pytest.fixture(autouse=True)
def setup(self, stracon_driver):
    self.driver = stracon_driver
    self.page = MiPagina(self.driver)
    # Tests usan self.page automáticamente
```

---

## 📊 Stack Tecnológico

| Herramienta | Versión | Para Qué |
|------------|---------|----------|
| Python | 3.8+ | Lenguaje |
| Selenium | 4.15.2 | Automatizar navegador |
| Pytest | 7.4.3 | Framework de testing |
| python-dotenv | 1.0.0 | Variables de entorno |
| pytest-xdist | 3.5.0 | Parallelización (opcional) |

---

## ✨ Ventajas de Esta Estructura

| Aspecto | Antes | Ahora |
|--------|-------|-------|
| **Mantenibilidad** | ❌ Tests duplicados | ✅ Código DRY |
| **Escalabilidad** | ❌ 10 tests = difícil | ✅ 100 tests = fácil |
| **Profesionalismo** | ❌ Caótico | ✅ Estándar industria |
| **Reutilización** | ❌ Copia-pega | ✅ Herencia y helpers |
| **Debugging** | ❌ Difícil | ✅ Logs + Screenshots |

---

## 🎓 Ejemplos de Código

### Crear una Página (Page Object)
```python
# stracon/modules/mi_modulo/pages.py
from pages.base_page import BasePage

class MiModuloPage(BasePage):
    TITULO = (By.XPATH, "//h1[contains(text(), 'Mi Módulo')]")
    BTN_ACCION = (By.ID, "btn")
    
    def hacer_algo(self):
        self.click(self.BTN_ACCION)
```

### Crear un Test
```python
# stracon/modules/mi_modulo/test_mi_modulo.py
class TestMiModulo:
    @pytest.fixture(autouse=True)
    def setup(self, stracon_driver):
        self.page = MiModuloPage(stracon_driver)
    
    def test_algo(self):
        self.page.hacer_algo()
        assert self.page.is_text_present("esperado")
```

### Ejecutar
```bash
pytest stracon/modules/mi_modulo/ -v
```

---

## 🚨 Primeros Pasos

### Paso 1: Verificar Instalación
```bash
# Estar en la carpeta del proyecto
cd C:\dev\python\py_selenium

# Activar entorno
.\env\Scripts\activate

# Verificar pytest
pytest --version
```

### Paso 2: Ejecutar Tests Existentes
```bash
# Todos los tests
pytest stracon/ -v

# O uno específico
pytest stracon/modules/asignacion_formatos/test_asignacion_formatos.py -v
```

### Paso 3: Ver Documentación
- Abre: `README_NUEVA_ESTRUCTURA.md`
- Luego: `CHECKLIST_NUEVO_TEST.md`

### Paso 4: Crear Tu Primer Test
- Sigue: `CHECKLIST_NUEVO_TEST.md`
- Copia desde un test existente
- Adapta para tu caso

---

## 🔗 Enlaces Importantes

| Documento | Para Qué |
|-----------|----------|
| [README_NUEVA_ESTRUCTURA.md](README_NUEVA_ESTRUCTURA.md) | Entender la arquitectura |
| [COMANDOS_RAPIDOS.md](COMANDOS_RAPIDOS.md) | Referencia de comandos |
| [RUN_TESTS.md](RUN_TESTS.md) | Cómo ejecutar tests |
| [CHECKLIST_NUEVO_TEST.md](CHECKLIST_NUEVO_TEST.md) | Crear tests nuevos |
| [ESTRUCTURA_DEL_PROYECTO.txt](ESTRUCTURA_DEL_PROYECTO.txt) | Carpetas y archivos |
| [ARBOL_COMPLETO.txt](ARBOL_COMPLETO.txt) | Árbol visual |
| [CLAUDE.md](CLAUDE.md) | Documentación técnica |

---

## ❓ Preguntas Frecuentes

**P: ¿Dónde están los tests?**  
R: En `stracon/modules/*/test_*.py`

**P: ¿Cómo cambio la URL a testear?**  
R: Edita `.env`, busca `STRACON_BASE_URL`

**P: ¿Cómo agrego un nuevo módulo?**  
R: Lee `CHECKLIST_NUEVO_TEST.md`

**P: ¿Cómo veo los logs?**  
R: Ejecuta con `-v -s`: `pytest stracon/ -v -s`

**P: ¿Cómo ejecuto tests en paralelo?**  
R: `pytest stracon/ -n auto`

**P: ¿Qué pasa si un test falla?**  
R: Se captura screenshot en `.png` y ves logs en terminal

---

## 🎯 Próximas Acciones

1. ✅ Lee este archivo (START_HERE.md)
2. ✅ Lee README_NUEVA_ESTRUCTURA.md (5 min)
3. ✅ Ejecuta: `pytest stracon/ -v` (2 min)
4. ✅ Lee CHECKLIST_NUEVO_TEST.md (5 min)
5. ✅ Crea tu primer test (15 min)

**Total: 30 minutos para estar productivo** ⚡

---

## 📞 Ayuda Rápida

```bash
# Ver estructura
type ARBOL_COMPLETO.txt

# Ver comandos
type COMANDOS_RAPIDOS.md

# Ver cómo ejecutar
type RUN_TESTS.md

# Ver cómo crear tests
type CHECKLIST_NUEVO_TEST.md

# Ver documentación técnica
type CLAUDE.md
```

---

**¿Listo?** Ve a **[README_NUEVA_ESTRUCTURA.md](README_NUEVA_ESTRUCTURA.md)** y comienza. 🚀
