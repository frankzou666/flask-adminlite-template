
from flask import Blueprint,flash,get_flashed_messages,redirect,url_for,request,current_app
from flask import render_template,redirect


homeblueprint = Blueprint('homeblueprint', __name__,url_prefix='/home')


@homeblueprint.route('/')
def home():
    return render_template('index.html')


@homeblueprint.route('/das1')
def das1():
    return render_template('das1.html')


@homeblueprint.route('/das2')
def das2():
    return render_template('das2.html')