# 🚀 Comandos Rápidos - Referencia Rápida

## Setup Inicial

```bash
# Crear entorno virtual (primera vez)
py -m venv env

# Activar entorno virtual ⭐ (ANTES DE CUALQUIER COSA)
.\env\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Verificar que todo esté bien
pytest --version
```

## Ejecutar Tests

### Básico
```bash
# ⭐ Todos los tests de STRACON
pytest stracon/ -v

# Solo un módulo
pytest stracon/modules/asignacion_formatos/ -v

# Un test específico
pytest stracon/modules/asignacion_formatos/test_asignacion_formatos.py -v

# Un test específico (función exacta)
pytest stracon/modules/asignacion_formatos/test_asignacion_formatos.py::TestAsignacionFormatos::test_asignar_formato_exitoso
```

### Avanzado
```bash
# Con logs visibles (show prints)
pytest stracon/ -v -s

# Parar en primer fallo
pytest stracon/ -x

# Mostrar últimos 3 fallos
pytest stracon/ --lf

# Ejecutar en paralelo (muy rápido)
pytest stracon/ -n auto

# Generar reporte HTML
pytest stracon/ --html=report.html

# Solo tests limpios (sin advertencias)
pytest stracon/ -v --disable-warnings

# Ejecutar con timeout (en segundos)
pytest stracon/ --timeout=300
```

## Debug y Troubleshooting

```bash
# Ver todo lo que hace pytest
pytest stracon/ -vv

# Más info en fallos
pytest stracon/ -v --tb=long

# Captura menos info (más rápido)
pytest stracon/ -v --tb=short

# Ejecutar tests que fallaron antes
pytest stracon/ --lf

# Ejecutar solo tests que fallaron + todos
pytest stracon/ --ff

# Ejecutar test por número de línea
pytest stracon/modules/asignacion_formatos/test_asignacion_formatos.py::32

# Mostrar fixtures disponibles
pytest --fixtures

# Mostrar fixtures de un módulo
pytest stracon/modules/asignacion_formatos --fixtures
```

## Filtros

```bash
# Solo tests que contienen "formato"
pytest stracon/ -k "formato" -v

# Excluir tests que contienen "slow"
pytest stracon/ -k "not slow" -v

# Tests marcados como "smoke"
pytest -m smoke -v

# Tests que NO son "slow"
pytest -m "not slow" -v
```

## Markers (Etiquetas)

```bash
# Ejecutar solo tests críticos
pytest stracon/ -m smoke -v

# Ejecutar solo tests de regresión
pytest stracon/ -m regression -v

# Ejecutar TODO excepto tests lentos
pytest stracon/ -m "not slow" -v
```

Agregar markers en tests:
```python
@pytest.mark.smoke
def test_critical():
    pass

@pytest.mark.slow
def test_slow():
    pass
```

## Configuración

```bash
# Listar todas las variables desde .env
cat .env

# Cambiar timeout temporalmente
EXPLICIT_WAIT=30 pytest stracon/

# Correr en headless (sin ventana)
CHROME_HEADLESS=True pytest stracon/

# Activar debug logging
LOG_LEVEL=DEBUG pytest stracon/ -v -s
```

## Monitoreo y Reporting

```bash
# Generar reporte HTML completo
pytest stracon/ --html=report.html --self-contained-html

# Generar reporte con screenshot en fallos
pytest stracon/ --html=report.html --screenshot=on_failure

# Generar reporte JSON
pytest stracon/ --json=report.json

# Generar cobertura (si está instalado)
pytest stracon/ --cov=stracon --cov-report=html
```

## Virtual Environment

```bash
# Actualizar pip
python -m pip install --upgrade pip

# Instalar nuevas dependencias
pip install selenium pytest python-dotenv

# Ver dependencias instaladas
pip list

# Desactivar entorno virtual
deactivate

# Eliminar entorno (si algo falla)
rmdir /s env
# Luego recrear: py -m venv env
```

## Git/GitHub

```bash
# Ver cambios
git status

# Agregar cambios
git add .

# Commitear
git commit -m "Agregar tests para asignación de formatos"

# Push
git push origin master

# Ver último commit
git log -1 --oneline
```

## Archivos Importantes

```bash
# Editar configuración
notepad .env

# Editar config.py
code config.py

# Ver estructura del proyecto
type ARBOL_COMPLETO.txt

# Ver documentación
type README_NUEVA_ESTRUCTURA.md

# Ver cómo ejecutar tests
type RUN_TESTS.md
```

## Una Línea (Copy-Paste)

```bash
# Setup + instalar + ejecutar tests
py -m venv env && .\env\Scripts\activate && pip install -r requirements.txt && pytest stracon/ -v

# Ejecutar tests + generar reporte
pytest stracon/ -v --html=report.html --self-contained-html

# Debug: ver logs + parar en fallo
pytest stracon/ -v -s -x

# Ejecutar en paralelo
pytest stracon/ -n auto -v
```

## Troubleshooting Rápido

| Problema | Comando |
|----------|---------|
| Chrome no abre | `pip install webdriver-manager` |
| Timeout | `EXPLICIT_WAIT=30 pytest stracon/` |
| Tests muy lentos | `pytest stracon/ -n auto` |
| Ver qué falla | `pytest stracon/ -x -v -s` |
| Limpiar cache | `pytest --cache-clear` |
| Reinstalar deps | `pip install --force-reinstall -r requirements.txt` |

## Atajos Personalizados

Puedes crear un alias en PowerShell:

```powershell
# Crear alias para activar entorno
Set-Alias activate '.\env\Scripts\Activate.ps1'

# Luego solo escribes: activate

# Ver aliases
Get-Alias
```

## Pro Tips ⭐

```bash
# Ejecutar con notificación visual
pytest stracon/ && echo "✅ Tests pasaron!" || echo "❌ Tests fallaron!"

# Guardar resultados en archivo
pytest stracon/ -v > test_results.txt

# Ejecutar cada vez que guardes archivo (requiere pytest-watch)
ptw stracon/

# Ejecutar tests cada 2 segundos
pytest-watch stracon/ --runner="pytest -n auto"

# Ejecutar hasta que falle
pytest stracon/ --maxfail=1 -x
```

## Cheat Sheet ASCII

```
pytest stracon/
    │
    ├─ -v           → Verbose (detallado)
    ├─ -s           → Show prints/logs
    ├─ -x           → Stop on first failure
    ├─ -n auto      → Parallel execution
    ├─ --html=R.html → HTML report
    ├─ -k "nombre"  → Filter by name
    ├─ -m smoke     → Filter by marker
    ├─ --lf         → Last failed
    └─ --ff         → Failed first + all
```

---

## Links Rápidos

- 📖 [README_NUEVA_ESTRUCTURA.md](README_NUEVA_ESTRUCTURA.md) - Guía completa
- 🏃 [RUN_TESTS.md](RUN_TESTS.md) - Cómo ejecutar
- 📋 [CHECKLIST_NUEVO_TEST.md](CHECKLIST_NUEVO_TEST.md) - Crear nuevos tests
- 🗺️ [ARBOL_COMPLETO.txt](ARBOL_COMPLETO.txt) - Estructura del proyecto
- 📚 [CLAUDE.md](CLAUDE.md) - Documentación técnica
