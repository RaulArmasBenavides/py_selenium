# Cómo Ejecutar los Tests

## Requisitos Previos

```bash
# Activar entorno virtual
.\env\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

## Ejecutar Tests - STRACON

### Todos los tests de STRACON
```bash
pytest stracon/
```

### Solo el módulo Asignación de Formatos
```bash
pytest stracon/modules/asignacion_formatos/
```

### Test específico
```bash
pytest stracon/modules/asignacion_formatos/test_asignacion_formatos.py::TestAsignacionFormatos::test_asignar_formato_exitoso
```

### Con más verbosidad
```bash
pytest stracon/ -v
```

### Mostrar prints y logs
```bash
pytest stracon/ -v -s
```

## Ejecutar Tests - EJEMPLOS (Petclinic)

### Todos los tests de ejemplo
```bash
pytest examples/
```

### Test específico
```bash
pytest examples/petclinic_cloud.py::test_add_owner_form
```

## Ejecutar Todos los Tests

```bash
pytest
```

## Opciones Útiles

### Parar en el primer fallo
```bash
pytest stracon/ -x
```

### Mostrar últimos 3 fallos
```bash
pytest stracon/ --lf -x
```

### Ejecutar en paralelo (requiere pytest-xdist)
```bash
pytest stracon/ -n auto
```

### Generar reporte HTML
```bash
pytest stracon/ --html=report.html
```

### Solo tests marcados como "smoke"
```bash
pytest -m smoke
```

### Excluir tests lentos
```bash
pytest -m "not slow"
```

## Variables de Entorno

Las variables están en `.env`. Antes de ejecutar, asegúrate de:

```bash
# Verificar que .env existe y tiene los valores correctos
cat .env

# Si cambias URLs o credenciales, actualiza .env
```

## Troubleshooting

### Chrome driver no encontrado
- Descarga ChromeDriver: https://googlechromelabs.github.io/chrome-for-testing/
- Asegúrate de que versión coincida con tu Chrome

### Timeouts
- Aumenta `EXPLICIT_WAIT` en `.env` si la conexión es lenta
- Los waits predeterminados son: 20 segundos explícito, 10 implícito

### Tests fallan por elementos no encontrados
- Revisa los locators en las páginas de POM
- Captura screenshot con: `self.asignacion_page.take_screenshot('debug.png')`
