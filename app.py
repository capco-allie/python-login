import time
from flask import Flask, render_template, request
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
        return render_template('user.html', result=result)
    return render_template('login.html', form=form)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
