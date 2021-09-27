from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api, Resource
from user.controller.user import User
from auth.controller.auth import Auth
from building.controller.building import Building
from building.controller.building_batch import BuildingBatch
from areacode.controller.area_code import AreaCode
from flask_jwt_extended import JWTManager
from datetime import timedelta
from config.settings import Settings

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = Settings.return_jwt_secret_token()
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=int(Settings.return_jwt_access_token_expires()))
# app.config['JWT_REFRESH_TOKEN_EXPIRES'] = Settings.refresh
jwt = JWTManager(app)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

api.add_resource(Building, '/api/buildings')
api.add_resource(BuildingBatch, '/api/buildings/batch')
api.add_resource(AreaCode, '/api/codes')
api.add_resource(User, '/api/users')
api.add_resource(Auth, '/api/auth')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)