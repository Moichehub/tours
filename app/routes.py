from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, current_user
from app.models import User, Tour
from app.forms import LoginForm

main = Blueprint('main', __name__)
admin = Blueprint('admin', __name__)
auth = Blueprint('auth', __name__)

@main.route('/')
def index():
    tours = Tour.query.all()
    return render_template('index.html', tours=tours)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:  # Replace with proper password hashing
            login_user(user)
            return redirect(url_for('main.index'))
        flash('Login failed. Check your credentials.')
    return render_template('login.html', form=form)

@admin.route('/dashboard')
@login_required
def dashboard():
    if current_user.role != 'admin':
        flash('Access denied.')
        return redirect(url_for('main.index'))
    tours = Tour.query.all()
    return render_template('admin_dashboard.html', tours=tours)
