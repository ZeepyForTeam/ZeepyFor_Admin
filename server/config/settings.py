import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

class Settings:
    @staticmethod
    def return_molit_api_key():
        return os.getenv('MOLIT_API_KEY')

    @staticmethod
    def return_geocoder_api_key():
        return os.getenv('GEOCODER_API_KEY')
    
    @staticmethod
    def return_kakao_api_key():
        return os.getenv('KAKAO_API_KEY')

    @staticmethod
    def return_jwt_secret_token():
        return os.getenv('JWT_SECRET_TOKEN')

    @staticmethod
    def return_jwt_access_token_expires():
        return os.getenv('JWT_ACCESS_TOKEN_EXPIRES')