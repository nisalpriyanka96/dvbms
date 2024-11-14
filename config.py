import os
import connexion
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Create Connexion app
vuln_app = connexion.App(__name__, specification_dir='./openapi_specs')

# Enable CORS on the underlying Flask app
CORS(vuln_app.app)  # This line enables CORS on the actual Flask app object

# Configure the database URI for SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(vuln_app.app.root_path, 'database/database.db')
vuln_app.app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
vuln_app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set a secret key for the app
vuln_app.app.config['SECRET_KEY'] = 'random'

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(vuln_app.app)

# Custom error handler for 401 Unauthorized errors
@vuln_app.app.errorhandler(401)
def custom_401(error):
    # Custom 401 response to match the original response sent by Vampi
    response = jsonify({"status": "fail", "message": "Invalid token. Please log in again."})
    response.status_code = 401
    return response

# Add API endpoints defined in the OpenAPI 3.0 specification
vuln_app.add_api('openapi3.yml')
