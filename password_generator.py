from random import choices


def get_available_chars(checkbox_statuses):

    char_groups = {
        'uppercase': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'lowercase': 'abcdefghijklmnopqrstuvwxyz',
        'numbers'  : '0123456789',
        'symbols'  : r'!@#$%^&*()-=_+<>,./?;:\'"[]{}\|'
        }
    available_chars = ''
    
    # Add the correct character groups to available chars based on checkbox_statuses
    available_chars += char_groups['uppercase'] if checkbox_statuses[0] else ''
    available_chars += char_groups['lowercase'] if checkbox_statuses[1] else ''
    available_chars += char_groups['numbers']   if checkbox_statuses[2] else ''
    available_chars += char_groups['symbols']   if checkbox_statuses[3] else ''

    return available_chars


def generate_password(length, checkbox_statuses):

    # Get the characters that the password should be made up of
    available_chars = get_available_chars(checkbox_statuses)
    # Generate the password as a list and transform it into a string
    password = choices(available_chars, k=length)
    password = ''.join(password)

    return password
