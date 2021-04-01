from website import create_app
from password_generator import generate_password


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
    