from flask import Flask

def create_app():
    # Initialize the Flask application
    app = Flask(__name__)
    
    # Encrypt/Secure session data
    app.config['SECRET_KEY'] = '2340c78hnm0uh)(MH*FWpppxXPM*(H$F#$F*()J'
    
    # Import the Blueprints
    from .views import views
    from .auth import auth
    
    # Register the blueprints with a default prefix of /
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app