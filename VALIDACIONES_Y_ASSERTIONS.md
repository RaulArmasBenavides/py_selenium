# ✅ Validaciones y Assertions - Estrategias Completas

Guía práctica de cómo validar diferentes tipos de elementos y comportamientos en los tests.

## 🎯 Caso Real: Componentes > Elementos (de tu captura)

### Lo que ves en la captura:

```
┌─ Elementos | Materiales                    ← TABS
├─ Componentes | Elementos                   ← Breadcrumb
├─ [Buscar...] [Grupo Proyecto: Indiana] ← Filtros
├─ Tabla:
│  ├─ Código | Descripción | Estado | Acciones
│  ├─ ranm  | ranm         | 🔴 ON | ✏️ 🗑️
│  ├─ hh    | yhhh         | 🔴 ON | ✏️ 🗑️
│  ├─ taladro | taladradr   | ⚪ OFF | ✏️ 🗑️
│  └─ ... (más filas)
└─ [Actualizar] [✏️ Nuevo]
```

---

## 📋 Tipos de Validaciones

### 1️⃣ VALIDAR TABS VISIBLES

```python
def test_tabs_visibles(self):
    """Validar que ambos tabs están presentes"""
    # Opción 1: Verificar que el texto está en la página
    assert "Elementos" in self.driver.page_source
    assert "Materiales" in self.driver.page_source
    
    # Opción 2: Verificar que los elementos son visibles
    tab_elementos = self.page.is_element_visible(self.page.TAB_ELEMENTOS)
    tab_materiales = self.page.is_element_visible(self.page.TAB_MATERIALES)
    assert tab_elementos and tab_materiales
    
    # Opción 3: Verificar que el tab está activo
    tab_active = self.driver.find_element(
        By.XPATH, "//button[contains(@class, 'active') and text()='Elementos']"
    )
    assert tab_active is not None
```

### 2️⃣ VALIDAR TABLA CONTIENE DATOS

```python
def test_tabla_tiene_elementos(self):
    """Validar que la tabla contiene elementos"""
    # Opción 1: Buscar texto específico en la tabla
    assert "ranm" in self.driver.page_source
    assert "taladro" in self.driver.page_source
    
    # Opción 2: Contar filas de la tabla
    filas = self.driver.find_elements(
        By.XPATH, "//table//tbody/tr"
    )
    assert len(filas) > 0, "La tabla está vacía"
    assert len(filas) >= 5, "Debería haber al menos 5 elementos"
    
    # Opción 3: Verificar que la tabla está visible
    tabla = self.driver.find_element(By.XPATH, "//table")
    assert tabla.is_displayed()
```

### 3️⃣ VALIDAR CONTENIDO DE TABLA (Búsqueda de Filas)

```python
def test_fila_existe_en_tabla(self):
    """Validar que una fila específica existe"""
    # Buscar fila por código
    fila = self.driver.find_element(
        By.XPATH, "//table//tr[contains(., 'ranm')]"
    )
    assert fila is not None
    
    # Buscar fila por descripción
    fila = self.driver.find_element(
        By.XPATH, "//table//tr[td[contains(text(), 'taladradr')]]"
    )
    assert fila.is_displayed()

def test_elemento_con_codigo_especifico(self):
    """Validar elemento específico por código y descripción"""
    # Buscar la fila de "taladro" con "taladradr"
    xpath = """
        //table//tr[
            contains(., 'taladro') and 
            contains(., 'taladradr')
        ]
    """
    fila = self.driver.find_element(By.XPATH, xpath)
    assert fila.is_displayed()
```

### 4️⃣ VALIDAR ESTADO (Toggles/Switches)

```python
def test_estado_elemento(self):
    """Validar el estado (ON/OFF) de un elemento"""
    # Buscar el switch de "ranm" (debería estar ON - rojo 🔴)
    switch_ranm = self.driver.find_element(
        By.XPATH, "//tr[contains(., 'ranm')]//input[@type='checkbox']"
    )
    # Verificar si está checkeado (ON)
    assert switch_ranm.is_selected(), "ranm debería estar ON"
    
    # Buscar el switch de "taladro" (debería estar OFF - gris ⚪)
    switch_taladro = self.driver.find_element(
        By.XPATH, "//tr[contains(., 'taladro')]//input[@type='checkbox']"
    )
    # Verificar si NO está checkeado (OFF)
    assert not switch_taladro.is_selected(), "taladro debería estar OFF"

def test_cambiar_estado(self):
    """Validar que se puede cambiar el estado"""
    # Obtener estado anterior
    switch = self.driver.find_element(
        By.XPATH, "//tr[contains(., 'taladro')]//input[@type='checkbox']"
    )
    estado_anterior = switch.is_selected()
    
    # Hacer click para cambiar
    switch.click()
    
    # Verificar que cambió
    estado_nuevo = switch.is_selected()
    assert estado_nuevo != estado_anterior, "El estado no cambió"
```

### 5️⃣ VALIDAR BOTONES DE ACCIONES

```python
def test_botones_acciones_visibles(self):
    """Validar que los botones de editar y eliminar están presentes"""
    # En cada fila debería haber botones de editar y eliminar
    filas = self.driver.find_elements(By.XPATH, "//table//tbody/tr")
    
    for fila in filas:
        # Botón de editar (icono lápiz)
        btn_editar = fila.find_element(
            By.XPATH, ".//button[@title='Editar']"
        )
        assert btn_editar.is_displayed()
        
        # Botón de eliminar (icono papelera)
        btn_eliminar = fila.find_element(
            By.XPATH, ".//button[@title='Eliminar']"
        )
        assert btn_eliminar.is_displayed()

def test_click_botones_acciones(self):
    """Validar que se pueden hacer click en los botones"""
    # Hacer click en editar de "ranm"
    btn_editar = self.driver.find_element(
        By.XPATH, "//tr[contains(., 'ranm')]//button[@title='Editar']"
    )
    btn_editar.click()
    
    # Verificar que se abrió modal o página de edición
    assert "editar" in self.driver.page_source.lower() or \
           "modal" in self.driver.page_source
```

### 6️⃣ VALIDAR FILTROS

```python
def test_filtro_grupo_proyecto(self):
    """Validar que el filtro por Grupo Proyecto funciona"""
    # Obtener el select de grupo
    select_grupo = self.driver.find_element(
        By.XPATH, "//select[@name='grupo_proyecto'] or //div[contains(., 'Grupo Proyecto')]//select"
    )
    
    # Verificar que está visible
    assert select_grupo.is_displayed()
    
    # Verificar que tiene opciones
    opciones = select_grupo.find_elements(By.TAG_NAME, "option")
    assert len(opciones) > 0

def test_filtrar_por_grupo(self):
    """Validar que al filtrar, la tabla se actualiza"""
    # Cambiar filtro a un grupo diferente
    select_grupo = self.driver.find_element(By.NAME, "grupo_proyecto")
    select_grupo.send_keys("Otro Grupo")
    
    # Esperar a que se actualice la tabla
    time.sleep(2)  # ❌ NO HACER ESTO
    # ✅ HACER ESTO:
    self.page.wait_for_loading()
    
    # Verificar que la tabla se actualizó
    # (debería tener diferentes elementos)
    tabla_actualizada = self.driver.find_element(By.XPATH, "//table")
    assert tabla_actualizada.is_displayed()
```

### 7️⃣ VALIDAR BÚSQUEDA

```python
def test_buscar_elemento(self):
    """Validar que se puede buscar elementos"""
    # Llenar campo de búsqueda
    campo_busca = self.driver.find_element(
        By.XPATH, "//input[contains(@placeholder, 'Buscar')]"
    )
    campo_busca.send_keys("taladro")
    campo_busca.send_keys(Keys.RETURN)
    
    # Esperar resultados
    self.page.wait_for_loading()
    
    # Verificar que solo muestra taladro
    filas = self.driver.find_elements(By.XPATH, "//table//tbody/tr")
    for fila in filas:
        assert "taladro" in fila.text.lower()
```

### 8️⃣ VALIDAR MENSAJES/TOAST

```python
def test_mensaje_exito_al_guardar(self):
    """Validar que aparece mensaje de éxito"""
    # Hacer acción que genera mensaje
    # (ej: guardar, eliminar, etc.)
    
    # Esperar mensaje
    mensaje = self.driver.find_element(
        By.XPATH, "//div[@class='toast-success' or @class='alert-success']"
    )
    assert mensaje.is_displayed()
    assert "guardado" in mensaje.text.lower() or "éxito" in mensaje.text.lower()

def test_mensaje_error_al_fallar(self):
    """Validar que aparece mensaje de error"""
    # Hacer acción que falla (ej: validación)
    
    # Esperar mensaje de error
    mensaje = self.driver.find_element(
        By.XPATH, "//div[@class='toast-error' or @class='alert-danger']"
    )
    assert "error" in mensaje.text.lower()
```

---

## 🎯 Patrón Completo: Validar una Fila Completa

```python
def test_validar_elemento_completo(self):
    """TEST COMPLETO: Validar un elemento con todos sus datos"""
    
    # 1. Buscar la fila
    fila = self.driver.find_element(
        By.XPATH, "//table//tr[contains(., 'taladro')]"
    )
    
    # 2. Validar que existe
    assert fila is not None
    assert fila.is_displayed()
    
    # 3. Extraer datos de las celdas
    celdas = fila.find_elements(By.TAG_NAME, "td")
    codigo = celdas[0].text
    descripcion = celdas[1].text
    
    # 4. Validar datos
    assert codigo == "taladro"
    assert descripcion == "taladradr"
    
    # 5. Validar estado
    switch = fila.find_element(By.XPATH, ".//input[@type='checkbox']")
    assert not switch.is_selected()  # OFF
    
    # 6. Validar botones
    btn_editar = fila.find_element(By.XPATH, ".//button[@title='Editar']")
    btn_eliminar = fila.find_element(By.XPATH, ".//button[@title='Eliminar']")
    assert btn_editar.is_displayed()
    assert btn_eliminar.is_displayed()
```

---

## 📊 Tabla de Locators Útiles

| Elemento | XPath | CSS |
|----------|-------|-----|
| Tab Elementos | `//button[text()='Elementos']` | `button:contains("Elementos")` |
| Tabla | `//table` | `table` |
| Filas | `//table//tbody/tr` | `table tbody tr` |
| Celdas | `//table//td` | `table td` |
| Switch ON/OFF | `//input[@type='checkbox']` | `input[type="checkbox"]` |
| Botón Editar | `//button[@title='Editar']` | `button[title="Editar"]` |
| Botón Eliminar | `//button[@title='Eliminar']` | `button[title="Eliminar"]` |
| Campo Búsqueda | `//input[contains(@placeholder, 'Buscar')]` | `input[placeholder*="Buscar"]` |
| Select Grupo | `//select[@name='grupo_proyecto']` | `select[name="grupo_proyecto"]` |

---

## ❌ ERRORES COMUNES

### ❌ Usar time.sleep()
```python
# ❌ MAL
time.sleep(2)
elemento = driver.find_element(...)

# ✅ BIEN
elemento = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "elemento"))
)
```

### ❌ Asumir que algo está visible
```python
# ❌ MAL
elemento = driver.find_element(...)
elemento.click()  # ¿Y si está oculto?

# ✅ BIEN
elemento = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "elemento"))
)
elemento.click()
```

### ❌ No verificar que se actualizó
```python
# ❌ MAL
driver.find_element(...).send_keys("texto")
assert "texto" in driver.page_source  # Podría ser del cambio anterior

# ✅ BIEN
input_elem = driver.find_element(...)
input_elem.clear()
input_elem.send_keys("texto")
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element(input_elem, "texto")
)
```

---

## 🎯 Validaciones en Componentes (Partes Diarios)

### Para ElementosComponent

```python
def test_validar_elemento_en_tabla(self):
    """Validar que un elemento aparece en la tabla"""
    # Agregar elemento
    self.elementos.agregar_elemento("Herramienta", "Taladro", "1")
    
    # Validar
    elementos = self.elementos.obtener_elementos_tabla()
    assert any(e['descripcion'] == "Taladro" for e in elementos)
```

### Para MaterialesComponent

```python
def test_validar_material_en_tabla(self):
    """Validar que un material aparece en la tabla"""
    # Agregar material
    self.materiales.agregar_material("Tubo PVC", "Consumible", "50", "Metros")
    
    # Validar
    materiales = self.materiales.obtener_materiales_tabla()
    assert any(m['nombre'] == "Tubo PVC" for m in materiales)
```

---

## 🚀 Ejecutar Tests de Validación

```bash
# Todos los tests
pytest stracon/modules/partes_diarios/ -v

# Solo tests de tabla
pytest stracon/modules/partes_diarios/ -k "tabla" -v

# Con logs
pytest stracon/modules/partes_diarios/ -v -s

# Ver qué encuentra
pytest stracon/modules/partes_diarios/ -v -s --tb=short
```

---

## 📚 Referencias

- [Selenium Expected Conditions](https://selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html)
- [XPath Tutorial](https://www.w3schools.com/xml/xpath_intro.asp)
- [CSS Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors)
