import time
from flask import Flask, render_template, request, session, redirect, url_for, escape, abort, make_response
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'allie'

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/hello/<name>')
def  hello_name(name):
    return "Hello, %s" % name

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.is_submitted():
        result = request.form
        # return render_template('user.html', result=result)
        session['email'] = request.form['email']
        session['password'] = request.form['password']
        resp = redirect(url_for('myProfile'))
        resp.set_cookie('username', 'the username')
        return resp
    return render_template('login.html', form=form)

@app.route('/my-profile')
def myProfile():
    if 'email' not in session:
        abort(401)

    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # reading and updating session data
    else:
        session['visits'] = 1 # setting session data
    return render_template('user.html', email=session['email'], password=session['password'], visits=session['visits'], image=url_for('static', filename='user.html'))

@app.route('/logout')
def logout():
    session.pop('email', 'password')
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
