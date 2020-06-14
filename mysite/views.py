from flask import render_template, redirect, request, url_for, flash
from mysite.forms import RegistrationForm, LoginForm


def about():
    return render_template('about.html')


def home():
    return render_template('home.html')


def login():
    form = LoginForm()
    if request.method == 'POST':
        return redirect(url_for('home'))
    else:
        return render_template('login.html', title='Login', form=form)


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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.first_name.data} {form.last_name.data}!', 'success')
        return redirect(url_for('home'))
    else:
        return render_template('register.html', title='Register', form=form)