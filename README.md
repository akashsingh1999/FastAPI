# 🚀 FastAPI Journey  
*Learning Python API Development with FastAPI*

---

## 📅 Day #1 - Getting Started

### 🧰 Setting Up the Environment

- **Create a Virtual Environment**
  ```bash
  python3 -m venv venv
  ```

- **Activate the Virtual Environment**
  ```bash
  source ./venv/bin/activate
  ```

- **Configure VS Code**
  - Change the Python interpreter to use the virtual environment (`venv`)
  - Change terminal to use the virtual environment

- **Install FastAPI and Uvicorn**
  ```bash
  pip install fastapi uvicorn
  ```

- **View Installed Packages**
  ```bash
  pip freeze
  ```

---

### 📝 First FastAPI App

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}
```

---

### 🚦 Starting the Web Server

```bash
uvicorn main:app --reload
```

---

## ✅ What I Learned

- Basics of Python virtual environments
- FastAPI setup and installation
- Creating a simple API endpoint
- Running a development server with Uvicorn

---

## 📚 Resources

- [FastAPI Official Docs](https://fastapi.tiangolo.com/)
- [Uvicorn GitHub](https://github.com/encode/uvicorn)
- [Youtube Video](https://youtu.be/0sOvCWFmrtA?feature=shared)

---

