from flask import render_template, url_for, Blueprint, flash, redirect
from webse import application

users = Blueprint('users', __name__)
