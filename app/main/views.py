from flask import render_template
from main import main_blueprint as main

@main.route('/')
def index():
     render_template('index.html')