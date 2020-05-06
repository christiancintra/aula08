# controllers.py
from flask import render_template
from aplicacao import app

@app.route('/')

def index():
    return render_template('C:\Users\chris\Desktop\intro-flask\env\templates\index.html')
