from flask import flash, redirect, render_template, request, url_for

from mysite import bcrypt, db 
from mysite.forms import RegistrationForm, LoginForm
from mysite.models import Product, Product_img, User 
from flask_login import  current_user, login_user, login_required, logout_user


def about():
    return render_template('about.html')


def account():
    return render_template('account.html', title='Account')


def cart():
    if request.method == 'POST':
        return redirect(url_for('product'))
    else:
        return render_template('cart.html')


def confirm():
    if request.method == 'POST':
        return redirect(url_for('home'))
    else:
        return render_template('confirm.html')


def home():
    return render_template('home.html')


def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    else:
        if request.method == 'POST':
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('home'))
            else:
                flash('Login Unsuccessful. Please check email and password', 'danger')
        else:
            return render_template('login.html', title='Login', form=form)


def logout():
    logout_user()
    return redirect(url_for('home'))


def product():
    if request.method == 'POST':
        return redirect(url_for('home'))
    else:
        return render_template('product.html')


def profile():
    if request.method == 'POST':
        return redirect(url_for('home'))
    else:
        return render_template('profile.html')


def register():    
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    else:
        form = RegistrationForm()
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
            user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, password=hashed_password,)
            db.session.add(user)
            db.session.commit()
            flash(f'Your account has been created! You now able to log in', 'success')
            return redirect(url_for('login'))
        else:
            return render_template('register.html', title='Register', form=form)