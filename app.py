from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = "supersecret"

# Database config
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'todo.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_email = db.Column(db.String(120), db.ForeignKey('user.email'))

# Utility
def valid_user(email, password):
    return User.query.filter_by(email=email, password=password).first()

# Routes
@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = valid_user(email, password)
        print(f"Login attempt: {email}, success: {bool(user)}")
        if user:
            session['user'] = user.email
            flash("Login successful", "success")
            return redirect('/dashboard')
        flash("Invalid credentials", "danger")
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm = request.form.get('confirm_password')
        if password != confirm:
            flash("Passwords do not match", "danger")
        elif User.query.filter_by(email=email).first():
            flash("Email already registered", "warning")
        else:
            new_user = User(email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash("Account created successfully! Please log in.", "success")
            return redirect('/login')
    return render_template('signup.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    user_email = session.get('user')
    if user_email:
        if request.method == 'POST':
            title = request.form.get('title')
            desc = request.form.get('desc')
            new_todo = Todo(title=title, desc=desc, user_email=user_email)
            db.session.add(new_todo)
            db.session.commit()
            return redirect('/dashboard')
        allTodo = Todo.query.filter_by(user_email=user_email).all()
        return render_template('index.html', allTodo=allTodo)
    flash("You must be logged in to access the dashboard", "warning")
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("Logged out successfully", "info")
    return redirect('/')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    todo = Todo.query.get_or_404(id)
    if request.method == 'POST':
        todo.title = request.form.get('title')
        todo.desc = request.form.get('desc')
        db.session.commit()
        return redirect('/dashboard')
    return render_template('update.html', todo=todo)

@app.route('/delete/<int:id>')
def delete(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect('/dashboard')

# Run the app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)
