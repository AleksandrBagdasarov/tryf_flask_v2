from flask import render_template, redirect, request, url_for


def about():
    return render_template('about.html')


def home():
    return render_template('home.html')


def login():
    if request.method == 'POST':
        return redirect(url_for('home'))
    else:
        return render_template('login.html')


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
    if request.method == 'POST':
        return redirect(url_for('home'))
    else:
        return render_template('register.html')