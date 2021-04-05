from flask import Blueprint, render_template, request
from .static.password_generator import generate_password

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    return render_template('home.html')
