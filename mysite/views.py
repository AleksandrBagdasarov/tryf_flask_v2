from flask import render_template, redirect, request, url_for


def about():
    return render_template('about.html')


def home():
    return render_template('home.html')


def register():
    if request.method == 'POST':
        return redirect(url_for('home'))
    else:
        return render_template('register.html')