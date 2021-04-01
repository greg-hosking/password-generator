from flask import Blueprint, render_template, request
from password_generator import generate_password

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    # Initialize the values in the fields and set the password to an empty string
    selected_length = 16
    checkbox_statuses = [True, True, True, True]
    password = ''

    if request.method == 'POST':
        # Get the password length and checkbox statuses from the form
        selected_length = int(request.form.get('password-length-select', 16))
        checkbox_names = ['checkbox-1', 'checkbox-2', 'checkbox-3', 'checkbox-4']
        checkbox_statuses = []
        for name in checkbox_names:
            checkbox_statuses.append(request.form.get(name, 'off') == 'on')
        # Generate the new password
        password = generate_password(selected_length, checkbox_statuses)

    return render_template('home.html', selected_length=selected_length, 
                           checkbox_statuses=checkbox_statuses, password=password)
