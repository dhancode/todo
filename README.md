
# 📝 Django To-Do List Application

A production-ready **Django To-Do List web application** implementing full **CRUD functionality**, secure environment configuration using **`.env`**, and clean project architecture.
This project is structured to be **easily deployable** on platforms like **Render, Railway, Heroku, or VPS**.

---

## 🚀 Features

* ➕ Create to-do items
* 📋 List all to-dos
* 🔍 View detailed task information
* ✏️ Update tasks
* 🗑 Delete tasks
* 🔐 Environment-based configuration
* 🛠 Django Admin panel
* 🎨 Clean UI using HTML & CSS

---

## 🛠 Tech Stack

* **Backend:** Python 3.10, Django 5.x
* **Frontend:** HTML, CSS
* **Database:** SQLite (development)
* **Version Control:** Git & GitHub
* **Environment Management:** python-dotenv

---

## 📂 Project Structure

```
todoproject/
├── config/
│   └── settings.py
├── todo/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│       └── todo/
│           ├── index.html
│           ├── form.html
│           └── detail.html
├── .env.example
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Local Setup (Development)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/dhancode/todo.git
cd todoproject
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate (Windows):

```bash
venv\Scripts\Activate.ps1
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DB_NAME=db.sqlite3
```

> ⚠️ `.env` is excluded from version control for security reasons.

---

## 🗄 Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🔐 Admin Setup

```bash
python manage.py createsuperuser
```

Access admin panel:

```
http://127.0.0.1:8000/admin/
```

---

## ▶️ Run the Application

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 🚀 Deployment Notes

This project is deployment-ready with minimal changes:

### ✔ For Production:

* Set `DEBUG=False`
* Add production domain to `ALLOWED_HOSTS`
* Replace SQLite with PostgreSQL
* Use a production WSGI server (Gunicorn)
* Configure static files

Example production `.env`:

```env
DEBUG=False
SECRET_KEY=production-secret-key
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=postgres://user:password@host:port/dbname
```

---

## 🧠 What This Project Demonstrates

* Django MTV architecture
* Secure configuration management
* CRUD operations with ORM
* Admin customization
* Git-based deployment workflow
* Production readiness awareness

---

## 🔮 Future Enhancements

* User authentication
* Task priorities & deadlines
* REST API integration
* Responsive UI framework
* Cloud deployment (Render / AWS / Railway)

---

## 👨‍💻 Author

**Santhosh**
GitHub: [https://github.com/dhancode](https://github.com/dhancode)

---

## 📜 License

This project is intended for **educational and portfolio use**.

---

### ✅ Portfolio Tip

Include:

* Screenshots
* Deployed URL
* Short demo GIF

This makes your repository **recruiter-ready** 🚀

---

If you want next:

* Render / Railway deployment steps
* PostgreSQL migration
* Gunicorn + Whitenoise setup
* Resume project summary

Just tell me 👍
