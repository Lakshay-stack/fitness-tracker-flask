# 🏋️ Fitness Tracker Flask App

A fully functional fitness tracking web application built with **Flask**, allowing users to register, track their fitness progress, get personalized **workout** and **diet plans**, and calculate their **BMI**.

## 🚀 Features

- 🔐 User Registration & Login
- 📋 Fitness Profile with Goal & Routine
- 📊 BMI Calculator with Recommendations
- 💪 Personalized Workout Plans (Goal + Routine-based)
- 🍽 Custom Diet Plans
- 📞 Contact Us Page
- 🖼 Beautiful Bootstrap-based UI
- 🗄 SQLite Database Integration

## 🛠 Tech Stack

- Python (Flask Framework)
- HTML, CSS, Bootstrap
- Jinja2 Templating
- SQLite (SQLAlchemy ORM)
- Flask-Login for Authentication

## 🧠 Logic Highlights

- 9 Combinations of Goal + Routine (e.g., Build Muscle + Beginner)
- Smart Template Routing Based on User Profile
- Fallback if data is missing

## 📦 Setup Instructions

```bash
git clone https://github.com/Lakshay-stack/fitness-tracker-flask.git
cd fitness-tracker-flask
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python run.py
