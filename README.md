# Python Selenium QA Demo  

🚀 End-to-end **QA automation project** built with **Python**, **Flask**, and **Selenium WebDriver**.  
This project demonstrates how to build a small **login + dashboard app** and validate it using an **automated test suite** following QA best practices.  

---

## 📌 Overview
This project consists of:
- A **Flask web app** with:
  - User registration & login (with hashed passwords)  
  - A personal dashboard with CRUD (Create, Update, Delete) items  
  - Accessibility-friendly forms and navigation  
- An **automated test suite** using:
  - **Selenium WebDriver (Python)**  
  - **pytest** test runner  
  - **Page Object Model (POM)** for clean test structure  
- **GitHub Actions CI/CD** (runs tests automatically on every push)  

---

## 🛠️ Tech Stack
- **Backend:** Flask, SQLAlchemy, Flask-Login  
- **Database:** SQLite (default, lightweight)  
- **Frontend:** HTML, Jinja2, CSS  
- **Testing:** Selenium, pytest, WebDriverWait, Page Object Model  
- **CI/CD:** GitHub Actions with headless Chrome  

---

## 📂 Project Structure
```
python-selenium-qa-demo/
│
├── app/                       # Flask app
│   ├── __init__.py
│   ├── models.py               # User + Item models
│   ├── routes.py               # App routes
│   ├── templates/              # HTML templates
│   └── static/                 # CSS, images
│
├── tests/                      # Selenium test suite
│   ├── pages/                  # Page Object classes
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── register_page.py
│   │   └── dashboard_page.py
│   ├── test_auth.py            # Register/Login flow tests
│   ├── test_accessibility.py   # Accessibility tests
│   └── conftest.py             # Fixtures (server + Selenium driver)
│
├── .github/workflows/ci.yml    # GitHub Actions workflow
├── .env.example                # Example environment config
├── app.py                      # App entry point
├── requirements.txt            # Python dependencies
├── pytest.ini                  # pytest configuration
└── README.md                   # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the repo
```bash
git clone https://github.com/avinav456/flask-selenium-automation.git
cd flask-selenium-automation
```

### 2. Create a virtual environment
```bash
python -m venv .venv
# Activate
# Windows (PowerShell):
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the Flask app
```bash
python app.py
```
App will be available at: **http://127.0.0.1:5000**

---

## 🧪 Running Tests

### Run all tests
```bash
pytest -q
```

### Run a specific test file
```bash
pytest tests/test_auth.py -v
```

### See tests in Chrome (non-headless mode)
Edit `tests/conftest.py` and comment out:
```python
# opts.add_argument("--headless=new")
```
Then re-run pytest to watch the browser in action.

---

## 📊 Continuous Integration
This project includes a **GitHub Actions workflow**:
- Installs Python + Chrome  
- Starts the Flask app in the background  
- Runs Selenium tests in headless mode  
- Reports pass/fail status in the **Actions tab**  

---

## 🔑 Environment Variables
Copy `.env.example` → `.env` if needed. Defaults are already set:
```
SECRET_KEY=dev-secret
DATABASE_URL=sqlite:///app.db
```

---

## 🎯 Features Demonstrated
- Automated **end-to-end QA testing**  
- Secure **login & authentication** flow  
- **CRUD dashboard** tested with Selenium  
- Basic **accessibility validation** (labels, alt text)  
- **CI/CD pipeline** with GitHub Actions  

---

## 📌 Future Improvements
- Add **Allure / pytest-html** reports for visual test results  
- Extend **a11y testing** with axe-core integration  
- Add Dockerfile for easy containerized setup  

---

## 📜 License
MIT License © 2025 Avinav 
