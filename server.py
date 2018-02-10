from flask import Flask, render_template, session, redirect 

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	if 'times' in session:
		session['times'] += 1
	else: 
		session['times'] = 1
	return render_template('index.html', times=session['times'])

@app.route('/zero', methods=['POST'])
def zero():
	session['times'] = -1
	return redirect('/')

@app.route('/add2', methods=['POST'])
def add2():
	session['times'] += 1
	return redirect('/')



app.run(debug=True)

