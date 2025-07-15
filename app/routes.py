from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.forms import RegisterForm, LoginForm, FitnessProfileForm
from app.models import User
from app import db
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html', current_year=datetime.now().year)

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('Registration successful! Please complete your profile.', 'success')
        return redirect(url_for('main.fitness_profile'))
    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        flash('Invalid credentials. Try again.', 'danger')
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@main.route('/workout-plans')
def workout_plans():
    return render_template('workout.html')

@main.route('/diet-plans')
def diet_plans():
    return render_template('diet.html')

@main.route('/bmi', methods=['GET', 'POST'])
def bmi():
    bmi_result = None
    status = None
    recommendation = {}

    if request.method == 'POST':
        try:
            height = float(request.form['height']) / 100
            weight = float(request.form['weight'])
            bmi_result = round(weight / (height ** 2), 2)

            if bmi_result < 18.5:
                status = "Underweight"
                recommendation = {
                    "calories": "2500–2800 kcal/day",
                    "protein": "1.2–1.5 g/kg",
                    "carbs": "55–60% of total calories",
                    "fat": "Healthy fats like nuts, seeds, avocado"
                }
            elif 18.5 <= bmi_result < 24.9:
                status = "Normal"
                recommendation = {
                    "calories": "2200–2500 kcal/day",
                    "protein": "1.0–1.2 g/kg",
                    "carbs": "50–55% of total calories",
                    "fat": "Balanced fat intake (25–30%)"
                }
            elif 25 <= bmi_result < 29.9:
                status = "Overweight"
                recommendation = {
                    "calories": "1800–2000 kcal/day",
                    "protein": "1.5 g/kg",
                    "carbs": "Low-GI carbs, fiber-rich foods",
                    "fat": "Healthy fats in moderation"
                }
            else:
                status = "Obese"
                recommendation = {
                    "calories": "1500–1800 kcal/day",
                    "protein": "1.5–2.0 g/kg",
                    "carbs": "Whole grains, avoid sugars",
                    "fat": "Avoid trans/saturated fats"
                }

        except (ValueError, ZeroDivisionError):
            flash("Invalid input. Please enter correct height and weight.", "danger")

    return render_template("bmi.html", bmi=bmi_result, status=status, recommendation=recommendation)

@main.route('/fitness-profile', methods=['GET', 'POST'])
@login_required
def fitness_profile():
    form = FitnessProfileForm()
    if form.validate_on_submit():
        current_user.age = form.age.data
        current_user.gender = form.gender.data
        current_user.weight = form.weight.data
        current_user.height = form.height.data
        current_user.body_fat = form.body_fat.data
        current_user.routine = form.routine.data
        current_user.goal = form.goal.data
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('fitness_profile.html', form=form)


@main.route('/your-workout-plan')
@login_required
def dynamic_workout():
        goal = current_user.goal.lower().replace(" ", "_")
        routine = current_user.routine.lower().replace(" ", "_")
        template_name = f"workout_{goal}_{routine}.html"
        return render_template(template_name)

@main.route('/your-diet-plan')
@login_required
def dynamic_diet():
        goal = current_user.goal.lower().replace(" ", "_")
        routine = current_user.routine.lower().replace(" ", "_")
        template_name = f"diet_{goal}_{routine}.html"
        return render_template(template_name)

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Here you can log, email, or store the data in a DB
        flash("Thank you for contacting us! We'll get back to you soon.", 'success')
        return redirect(url_for('main.contact'))
    return render_template('contact.html')
