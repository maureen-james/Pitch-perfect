from flask import render_template
from . import main
from main import main_blueprint as main

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@main.route('/pitches/')
def business():
    # business=get_news('business')
    
    return render_template('business.html',business=business)  