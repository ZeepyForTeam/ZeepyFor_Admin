from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api, Resource
from user.controller.user import User
from auth.controller.auth import Auth
from building.controller.building import Building
from building.controller.building_batch import BuildingBatch
from areacode.controller.area_code import AreaCode
from job.controller.job import Job
from job.controller.job_cron import JobCron
from job.controller.job_date import JobDate
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

api.add_resource(Building, '/api/buildings') # 빌딩 컨트롤러
api.add_resource(BuildingBatch, '/api/buildings/batch') # 빌딩 배치 컨트롤러
api.add_resource(AreaCode, '/api/codes') # 지역코드 컨트롤러 (미사용)
api.add_resource(User, '/api/users') # 유저 컨트롤러
api.add_resource(Auth, '/api/auth') # 인증 컨트롤러
api.add_resource(Job, '/api/jobs') # 스케줄 잡 조회, 삭제 컨트롤러
api.add_resource(JobDate, '/api/jobs/date') # 스케줄 일회용 잡 등록 컨트롤러
api.add_resource(JobCron, '/api/jobs/cron') # 스케줄 주기 잡 등록 컨트롤러

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)