from application import app
from application.models.users_model import User
from flask import render_template, redirect, request, session, flash

def invalidCreds():
    flash('Invalid credentials', 'error_login_inv_creds')
    return redirect('/login')

@app.route('/login')
def showLoginPage():
    return render_template('login.html')

@app.route('/login/process_login', methods=['POST'])
def processLogin():
    login_token = User.validateLogin(request.form)
    if not login_token:
        return invalidCreds()
    session['logged_user'] = login_token
    return redirect(f'/users/{login_token}/dashboard')

@app.route('/login/process_registration', methods=['POST'])
def processRegistration():
    if User.validateRegist(request.form):
        new_user = User.registerNewUser(request.form)
        if new_user:
            session['logged_user'] = new_user
            return redirect(f'/users/{new_user}/dashboard')
    return redirect('/login')

@app.route('/users/<int:id>/dashboard')
def showDashboard(id):
    if 'logged_user' not in session:
        return redirect('/login')
    if id != session['logged_user']:
        return redirect('/login')
    current_user = User.getUser(id=id)
    return render_template('dashboard.html', user=current_user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')