"""
Configuración centralizada para todos los tests
Lee variables desde .env
"""
import os
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options

# Cargar variables de entorno
load_dotenv()

# ============================================
# Configuración General
# ============================================
CHROME_HEADLESS = os.getenv('CHROME_HEADLESS', 'False').lower() == 'true'
IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', 10))
EXPLICIT_WAIT = int(os.getenv('EXPLICIT_WAIT', 20))
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

# ============================================
# STRACON App
# ============================================
STRACON_BASE_URL = os.getenv('STRACON_BASE_URL')
STRACON_USERNAME = os.getenv('STRACON_USERNAME')
STRACON_PASSWORD = os.getenv('STRACON_PASSWORD')

# ============================================
# Petclinic Cloud (Ejemplo)
# ============================================
PETCLINIC_CLOUD_URL = os.getenv('PETCLINIC_CLOUD_URL')
PETCLINIC_CLOUD_USERNAME = os.getenv('PETCLINIC_CLOUD_USERNAME')
PETCLINIC_CLOUD_PASSWORD = os.getenv('PETCLINIC_CLOUD_PASSWORD')

# ============================================
# Petclinic Angular Local (Ejemplo)
# ============================================
PETCLINIC_ANGULAR_URL = os.getenv('PETCLINIC_ANGULAR_URL')
PETCLINIC_ANGULAR_USERNAME = os.getenv('PETCLINIC_ANGULAR_USERNAME')
PETCLINIC_ANGULAR_PASSWORD = os.getenv('PETCLINIC_ANGULAR_PASSWORD')

# ============================================
# Chrome Options
# ============================================
def get_chrome_options():
    """Retorna opciones de Chrome configuradas"""
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-infobars')

    if CHROME_HEADLESS:
        options.add_argument('--headless')

    return options
