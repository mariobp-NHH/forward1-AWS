from flask import render_template, url_for, Blueprint
from webse import application
forward_home= Blueprint('forward_home', __name__)


@forward_home.route('/home')
@forward_home.route('/')
def home():
    return 'Hello World'

