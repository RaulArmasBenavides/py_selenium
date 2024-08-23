
# 🐍 py_selenium - Automated Testing with Selenium

Welcome to **py_selenium**, a repository to help you kickstart automated browser testing using **Selenium** with **Python** and **Pytest**. 🚀

## 🚀 Getting Started

### 🛠️ Setting Up the Virtual Environment

First, you need to set up a Python virtual environment to isolate the project dependencies. Follow these steps:

1. **Create a virtual environment**: 
   ```bash
   py -m venv env
   ```

2. **Activate the virtual environment**:
   - On **Windows**:
     ```bash
     .\env\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source env/bin/activate
     ```

### 📦 Install Dependencies

Once your virtual environment is activated, install the required packages:

```bash
pip install pytest selenium
```

### 🖥️ Setting Up Google Chrome for Testing

If you plan on using **Google Chrome** for running your Selenium tests, ensure you have the appropriate ChromeDriver version installed.

🔗 **Google Chrome for Testing**: Please visit the following link to download and set up the necessary ChromeDriver:

[https://googlechromelabs.github.io/chrome-for-testing/#stable](https://googlechromelabs.github.io/chrome-for-testing/#stable)

> **Pro Tip**: Ensure that the ChromeDriver version matches the version of Google Chrome installed on your machine.

### 🧪 Running Your Tests

To execute the tests, simply run the following command in your terminal:

```bash
pytest selenium_testcase.py
```

This command will automatically discover and run all your test cases defined in `selenium_testcase.py`.

## 🎯 Project Structure

Here’s a quick overview of the typical structure for this project:

```
py_selenium/
│
├── env/                   # Virtual environment directory
├── tests/
│   └── selenium_testcase.py # Your Selenium test cases
├── README.md               # Project documentation
└── requirements.txt        # Dependency list (optional)
```

### 🗂️ tests/selenium_testcase.py

This is where your Selenium test cases will reside. You can organize your test files by creating subdirectories for better scalability.

## 💡 Tips & Tricks

- **Browser Compatibility**: Selenium supports multiple browsers such as Chrome, Firefox, Safari, and Edge. If you plan to test across different browsers, you can use WebDriver Manager for easier setup.
- **Headless Testing**: If you want to run your tests in the background (without opening a browser window), consider running your tests in **headless mode**:
  ```python
  from selenium.webdriver.chrome.options import Options

  options = Options()
  options.headless = True
  ```

- **Pytest Features**: Leverage the full power of `pytest` with features like fixtures, parameterized tests, and plugins for more robust and scalable testing.

## 🎉 Contributing

We welcome contributions! If you find a bug 🐛, want to request a feature 🌟, or just improve the documentation 📚, feel free to open an issue or submit a pull request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Enjoy automated testing with **Selenium** and **Pytest**! 🚀🖥️












Correr : 
Primero activar el entorno virtual ( tiene que aparecer (env) en la terminal)
.\env\Scripts\activate 

 Luego correr los siguientes comandos 
 pytest tests\test_add_owner_pet.py
 pytest tests\test_add_owner.py     
 
 Para probar la version de angular , primero levantar el angular y el backend (el servicio tiene que estar corriendo en docker)

 Descargar la version de angular aqui : https://github.com/spring-petclinic/spring-petclinic-angular
 Luego ejecutar npm install 
 Luego ejecutar ng serve -o

 pytest tests\test_add_owner2.py  
 pytest tests\test_add_owner_pet2.py   

