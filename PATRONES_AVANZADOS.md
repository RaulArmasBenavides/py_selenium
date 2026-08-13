# 🎯 Patrones Avanzados - Componentes y Tabs

Este documento muestra patrones profesionales para estructurar tests de componentes complejos con tabs, como **Partes Diarios (Elementos y Materiales)**.

## 🔷 Caso de Uso: Partes Diarios con Tabs

### Estructura Actual
```
stracon/modules/partes_diarios/
├── pages.py                     ← Tres clases, una por componente
│   ├── PartesDiariosPage       ← Página principal
│   ├── ElementosComponent      ← Tab: Elementos
│   └── MaterialesComponent     ← Tab: Materiales
└── test_partes_diarios.py      ← Tests organizados por componente
    ├── TestPartesDiariosBasico
    ├── TestElementos
    ├── TestMateriales
    └── TestIntegracionElementosYMateriales
```

### Ventajas de Esta Estructura

✅ **Separación de responsabilidades** - Cada componente es independiente  
✅ **Reutilizable** - ElementosComponent puede usarse en otros módulos  
✅ **Escalable** - Agregar nuevos componentes es trivial  
✅ **Testeable** - Tests específicos por componente + tests de integración  
✅ **Profesional** - Patrón usado en empresas grandes  

---

## 📋 Patrones Incluidos en Partes Diarios

### 1. Componente Simple (ElementosComponent)

```python
class ElementosComponent(BasePage):
    """Componente: Tab de Elementos"""

    # Locators
    TAB_ELEMENTOS = (By.XPATH, "//button[contains(text(), 'Elementos')]")
    BTN_AGREGAR = (By.XPATH, "//button[contains(text(), 'Agregar Elemento')]")
    TABLA = (By.XPATH, "//table[@class='tabla-elementos']")

    def click_tab(self):
        """Navega al tab"""
        self.click(self.TAB_ELEMENTOS)

    def agregar_elemento(self, tipo, descripcion, cantidad, estado="Disponible"):
        """Flujo: agregar elemento"""
        self.click(self.BTN_AGREGAR)
        self.fill(self.CAMPO_TIPO, tipo)
        self.fill(self.CAMPO_DESC, descripcion)
        # ... más interacciones

    def obtener_elementos_tabla(self):
        """Extrae datos de la tabla"""
        elementos = []
        filas = self.driver.find_elements(*self.FILA)
        for fila in filas:
            celdas = fila.find_elements(By.TAG_NAME, "td")
            elementos.append({
                'tipo': celdas[0].text,
                'descripcion': celdas[1].text,
            })
        return elementos
```

**Características**:
- ✅ Hereda de `BasePage`
- ✅ Métodos específicos del componente
- ✅ Extrae datos de tablas
- ✅ Puede ser usado en múltiples tests

### 2. Tests por Componente

```python
class TestElementos:
    """Suite de tests para el componente Elementos"""

    @pytest.fixture(autouse=True)
    def setup(self, stracon_driver):
        self.driver = stracon_driver
        self.elementos = ElementosComponent(self.driver)
        # Navega al tab
        self.elementos.click_tab()

    def test_agregar_elemento(self):
        """Test específico del componente"""
        self.elementos.agregar_elemento("Herramienta", "Taladro", "1")
        assert self.elementos.verificar_elemento_existe("Taladro")

    @pytest.mark.parametrize("tipo,desc", [
        ("Herramienta", "Taladro"),
        ("Equipo", "Compresor"),
    ])
    def test_parametrizado(self, tipo, desc):
        """Test parameterizado para múltiples casos"""
        self.elementos.agregar_elemento(tipo, desc, "1")
        assert self.elementos.verificar_elemento_existe(desc)
```

### 3. Tests de Integración (Componentes Juntos)

```python
class TestIntegracionElementosYMateriales:
    """Tests que usan múltiples componentes"""

    def test_crear_parte_completo(self):
        """Test: flujo completo con elementos + materiales"""
        # Step 1: Agregar Elementos
        self.parte_page.click_tab_elementos()
        self.elementos.agregar_elemento("Herramienta", "Taladro", "1")

        # Step 2: Navegar a Materiales
        self.parte_page.click_tab_materiales()
        self.materiales.agregar_material("Tubo PVC", "Consumible", "50", "Metros")

        # Step 3: Guardar completo
        self.parte_page.guardar_parte()

        # Assert
        assert "Parte guardado" in self.driver.page_source
```

---

## 🎯 Cuándo Usar Este Patrón

### ✅ Usa múltiples clases (ElementosComponent + MaterialesComponent) cuando:

1. **Hay tabs o secciones distintas** con UI separada
2. **Cada sección es independiente** (se puede testear por separado)
3. **Se pueden reutilizar en otros módulos** (ej: ElementosComponent podría usarse en "Inventario")
4. **Quieres tests organizados por funcionalidad**

### ❌ Usa una sola clase cuando:

1. Todo es muy simple (una sola página, sin tabs)
2. No hay separación clara de funcionalidad
3. No se reutiliza en otros módulos

---

## 📈 Estructura Mental

```
PartesDiariosPage (Página Principal)
    ├─ click_tab_elementos()     ← Navega a tab
    ├─ click_tab_materiales()    ← Navega a tab
    └─ guardar_parte()           ← Acción global

ElementosComponent (Tab 1)
    ├─ click_tab()               ← Accede al tab
    ├─ agregar_elemento()        ← Acción específica
    ├─ obtener_elementos_tabla() ← Extrae datos
    └─ verificar_elemento_existe()

MaterialesComponent (Tab 2)
    ├─ click_tab()               ← Accede al tab
    ├─ agregar_material()        ← Acción específica
    ├─ obtener_materiales_tabla() ← Extrae datos
    └─ verificar_material_existe()

Tests
    ├─ TestPartesDiariosBasico   ← Tests de página
    ├─ TestElementos             ← Tests del componente 1
    ├─ TestMateriales            ← Tests del componente 2
    └─ TestIntegracion           ← Tests usando ambos
```

---

## 🔄 Cómo Ejecutar

### Ejecutar todos los tests de Partes Diarios
```bash
pytest stracon/modules/partes_diarios/ -v
```

### Ejecutar solo tests del componente Elementos
```bash
pytest stracon/modules/partes_diarios/test_partes_diarios.py::TestElementos -v
```

### Ejecutar solo tests de integración
```bash
pytest stracon/modules/partes_diarios/test_partes_diarios.py::TestIntegracionElementosYMateriales -v
```

### Ejecutar con parametrización
```bash
pytest stracon/modules/partes_diarios/test_partes_diarios.py::TestElementos::test_agregar_multiples_elementos -v
```

### Con logs visibles
```bash
pytest stracon/modules/partes_diarios/ -v -s
```

---

## 💡 Tips Profesionales

### 1. Métodos Reutilizables

```python
# BUENO: Método reutilizable
def agregar_elemento(self, tipo, descripcion, cantidad, estado="Disponible"):
    self.click(self.BTN_AGREGAR)
    self.fill(self.CAMPO_TIPO, tipo)
    self.fill(self.CAMPO_DESC, descripcion)
    self.fill(self.CAMPO_CANT, cantidad)
    self.fill(self.CAMPO_ESTADO, estado)

# En test: fácil de reutilizar
self.elementos.agregar_elemento("Herramienta", "Taladro", "1")
self.elementos.agregar_elemento("Equipo", "Compresor", "1")
```

### 2. Extracción de Datos

```python
# Extraer lista de elementos para verificaciones
elementos = self.elementos.obtener_elementos_tabla()
assert len(elementos) == 2
assert elementos[0]['tipo'] == "Herramienta"
```

### 3. Fixtures Limpias

```python
@pytest.fixture(autouse=True)
def setup(self, stracon_driver):
    self.elementos = ElementosComponent(self.driver)
    self.elementos.click_tab()  # Navega al tab automáticamente
    # Todos los tests ya están en el tab correcto
```

### 4. Tests Claros

```python
def test_agregar_elemento_herramienta(self):
    """TEST: Agregar una herramienta al parte diario"""
    # Arrange
    tipo = "Herramienta"
    descripcion = "Taladro Eléctrico"
    cantidad = "1"

    # Act
    self.elementos.agregar_elemento(tipo, descripcion, cantidad)

    # Assert
    assert self.elementos.verificar_elemento_existe(descripcion)
```

---

## 🚀 Escalando el Patrón

### Agregar un 3er Componente

```python
# En pages.py: agregar nueva clase
class EquiposSegundadComponent(BasePage):
    """Componente: Tab de Equipos de Seguridad"""
    # ... locators y métodos

# En test_partes_diarios.py: agregar nueva test class
class TestEquiposSeguridad:
    # ... tests
```

### Agregar Nuevo Módulo con Mismo Patrón

```
stracon/modules/mantenimiento/
├── pages.py
│   ├── MantenimientoPage
│   ├── RevisionComponent    ← Multiple tabs
│   └── ReparacionComponent
└── test_mantenimiento.py
    ├── TestRevision
    ├── TestReparacion
    └── TestIntegracion
```

---

## 🎓 Comparación: Antes vs Después

### ❌ SIN patrón de componentes

```python
# Todo en una sola clase
class PartesDiariosPage(BasePage):
    # 50+ locators
    # 30+ métodos
    # Difícil de mantener
    # No reutilizable
```

### ✅ CON patrón de componentes

```python
# Dividido en 3 clases lógicas
class PartesDiariosPage(BasePage):       # 8 locators, 5 métodos
class ElementosComponent(BasePage):      # 10 locators, 8 métodos
class MaterialesComponent(BasePage):     # 10 locators, 8 métodos

# Fácil de mantener
# Reutilizable
# Testeable
```

---

## 📊 Resumen: Archivos de Partes Diarios

| Archivo | Líneas | Propósito |
|---------|--------|----------|
| `pages.py` | ~200 | 3 clases (Página + 2 Componentes) |
| `test_partes_diarios.py` | ~250 | 4 test classes, ~20 test methods |

**Total: Estructura profesional, escalable, mantenible.**

---

## 🔗 Relacionado

- `README_NUEVA_ESTRUCTURA.md` - Guía general de POM
- `CHECKLIST_NUEVO_TEST.md` - Cómo crear nuevos tests
- Carpeta: `stracon/modules/partes_diarios/` - Implementación completa
