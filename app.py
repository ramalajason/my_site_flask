from flask import Flask,session, redirect, url_for,render_template,request
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY','1234')
UTILISATEUR = {'username':'etudiant','password':'edt2026'}

@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return redirect(url_for('home'))

@app.route('/home')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('home.html',username=session['username'])

@app.route('/login',methods=['GET','POST'])
def login():
    message = None #Mbola tsy misy message
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        if username == UTILISATEUR['username'] and password == UTILISATEUR['password']:
            session['username'] = username 
            return redirect(url_for('home'))
        else:
            message = "Identification incorrect."
    return render_template('index.html',message = message)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

app.run(host='0.0.0.0', port=5000, debug=True) 
# run sur n'importe quel adresse IP du client 0.0.0.0

