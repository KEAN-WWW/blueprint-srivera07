from flask import Flask
from application.bp.homepage.routes import homepage
def init_app():
    app = Flask(__name__)
    app.register_blueprint(homepage)
    return app

# Optional: for running directly
if __name__ == "__main__":
    app = init_app()
    app.run(debug=True)

app = Flask(__name__)

# Register the Blueprint
app.register_blueprint(homepage)

if __name__ == '__main__':
    app.run(debug=True)
