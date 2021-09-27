 #-*- coding: utf-8 -*- 
import os 

class Executer(Resource):
    def __init__(self):
        self.type = ["GEOCODE", "MOLIT", "KAKAO_GEOCODE", "ZEEPY"]

    def get(self):
        return self.molit_service.get_jobs()

    def post(self):
        args = self.__make_post_arg()
        return self.molit_service.create(args)
    
    def delete(self):
        args = self.__make_delete_arg()
        return self.molit_service.delete_by_id(args)

    '''
    Argument Create
    - private method
    '''

    def __looping_directory_and_execute_function(self, function, read_directory, write_directory):
        directoies_about_molit_json = os.listdir(read_directory)
        for directory in directoies_about_molit_json:
            print(directory)
            
            if directory == "error":
                break

            if os.path.isdir(f"{write_directory}/{directory}") == False: # 디렉토리 체크
                os.mkdir(f"{write_directory}/{directory}")

            molit_jsons_name = os.listdir(f"{read_directory}/{directory}")

            for molit_json_name in molit_jsons_name:
                count = function(directory, molit_json_name)