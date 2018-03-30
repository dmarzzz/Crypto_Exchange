from flask import Flask, render_template, flash, request, redirect, url_for, logging, jsonify, json
from data import Prices
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__, static_url_path='/static')

Prices = Prices()


@app.route('/')
def index():
	return render_template('landing.html')

@app.route('/my_register')
def my_register():
	return render_template('my_register.html')

@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')

@app.route('/dashboard/test')
def test():
	response = {
	"field1": "value1",
	"field2": "value2"
	}
	return jsonify(response)#"It worked"

@app.route('/forum')
def forum():
	return render_template('forum.html')

@app.route('/thread')
def thread():
	return render_template('thread.html')

@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/prices')
def prices():
	return render_template('prices.html', prices = Prices)

@app.route('/register', methods = ['POST'])
def register():
	print(request.get_json())
	return "It worked"

"""class RegisterForm(Form):
	name = StringField('Name', [validators.Length(min=4, max=50)])
	username = StringField('Username', [validators.Length(min=4, max=25)])
	email = StringField('Email', [validators.Length(min=8, max=60)])
	password = StringField('Password', [validators.DataRequired(),
		validators.EqualTo('confirm', message= 'Passwords do not match')
		])
	confirm = PasswordField('Confirm Password')

@app.route('/register', methods= ['GET','POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
		name = form.name.data
		email = form.email.data
		username = form.username.data
		password = sha256_crypt.encrypt(str(form.password.data))

		#Place DB Writing Stuff Here
		###
		###
		###
		#############################
		print(name,email,username,password)

		flash('You are now registered with 0x431 Exchange')

		return redirect(url_for('/register'))

	return render_template('register.html', form= form)
"""

if __name__ == '__main__':
	app.secret_key = "1234"
	app.run(debug=True, threaded=True)