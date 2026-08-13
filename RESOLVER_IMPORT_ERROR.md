# 🔧 Resolver Error de Import de Selenium

Si ves este error en VSCode:

```
Import "selenium.webdriver.common.by" could not be resolved
```

## Soluciones

### 1️⃣ Solución Rápida (Recomendado)

```bash
# En la terminal (en la carpeta del proyecto)
.\env\Scripts\activate
pip install --force-reinstall -r requirements.txt
```

Luego **reinicia VSCode**:
- Ctrl + Shift + P
- Busca: "Reload Window"
- Enter

### 2️⃣ Configurar VSCode Correctamente

**Paso 1**: Presiona `Ctrl + Shift + P` y busca:
```
Python: Select Interpreter
```

**Paso 2**: Elige:
```
./env/Scripts/python.exe
```

Si no aparece, agrega manualmente en `.vscode/settings.json`:
```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/env/Scripts/python.exe"
}
```

**Paso 3**: Reinicia VSCode

### 3️⃣ Actualizar Pylance

- Abre: Extensions (Ctrl + Shift + X)
- Busca: "Pylance"
- Click "Update"
- Reinicia VSCode

### 4️⃣ Limpiar Cache de Python

```bash
# Eliminar cache
rm -r __pycache__ .pytest_cache .pytype

# Si en Windows:
rmdir /s __pycache__
rmdir /s .pytest_cache
```

### 5️⃣ Fuerza la Instalación

```bash
# Desactivar entorno
deactivate

# Eliminar env completo
rmdir /s env

# Crear nuevo entorno
py -m venv env

# Activar
.\env\Scripts\activate

# Instalar
pip install -r requirements.txt
```

---

## ✅ Verificar que Funciona

```bash
# Activar entorno
.\env\Scripts\activate

# Verificar importes
python -c "from selenium import webdriver; print('✓ Selenium OK')"
python -c "import pytest; print('✓ Pytest OK')"
python -c "from dotenv import load_dotenv; print('✓ python-dotenv OK')"
```

Si todo muestra `✓`, está bien.

---

## 🎯 El Error NO Afecta los Tests

**Importante**: El warning en VSCode **NO impide que los tests funcionen**.

Puedes ejecutar tests sin problema:

```bash
.\env\Scripts\activate
pytest stracon/ -v
```

El error es solo un **aviso del VSCode** (Pylance), no un error real.

---

## 📋 Checklist

- [ ] Crear/activar entorno virtual: `.\env\Scripts\activate`
- [ ] Instalar dependencias: `pip install -r requirements.txt`
- [ ] Seleccionar interpreter en VSCode: `.env/Scripts/python.exe`
- [ ] Reiniciar VSCode
- [ ] Verificar importes: `python -c "from selenium import webdriver"`
- [ ] Ejecutar test: `pytest stracon/ -v`

Después de esto, el error debería desaparecer.

---

## 💡 Si Persiste el Error

Abre la paleta de comandos (Ctrl + Shift + P) y ejecuta:

```
Pylance: Show Language Server Output
```

Busca mensajes de error específicos. Luego:

1. Verifica que el interpreter correcto está seleccionado
2. Reinicia la "Python Language Server": 

   ```
   Pylance: Restart Language Server
   ```

3. Reinicia VSCode por completo
