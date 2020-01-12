import os
from models import setup_db
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from server import AuthError, requires_auth, requires_scope

app = Flask(__name__)


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    # This doesn't need authentication
    @app.route("/api/public")
    @cross_origin(headers=["Content-Type", "Authorization"])
    def public():
        response = "Hello from a public endpoint! You don't need to be authenticated to see this."
        return jsonify(message=response)

    # This needs authentication
    @app.route("/api/private")
    @cross_origin(headers=["Content-Type", "Authorization"])
    @requires_auth
    def private():
        response = "Hello from a private endpoint! You need to be authenticated to see this."
        return jsonify(message=response)

    # This needs authorization
    @app.route("/api/private-scoped")
    @cross_origin(headers=["Content-Type", "Authorization"])
    @requires_auth
    def private_scoped():
        if requires_scope("read:messages"):
            response = "Hello from a private endpoint! You need to be authenticated and have a scope of read:messages to see this."
            return jsonify(message=response)
        raise AuthError({
            "code": "Unauthorized",
            "description": "You don't have access to this resource"
        }, 403)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
