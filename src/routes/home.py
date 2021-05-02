from src import app
from flask import render_template, request, redirect, url_for, session 

@app.route('/')
def index():
    return render_template('index.html')