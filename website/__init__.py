from flask import Flask

def create_app():
    # Initialize the Flask application
    app = Flask(__name__)
    
    # Encrypt/Secure session data
    app.config['SECRET_KEY'] = '2340c78hnm0uh)(MH*FWpppxXPM*(H$F#$F*()J'
    
    return app