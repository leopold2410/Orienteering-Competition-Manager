from flask import Blueprint
from flask_restful import Api

class ApiRoute:
    def __init__(self, version):
        self.prefix = '/api/{}'.format(version)
        self.blueprint = Blueprint(self.prefix, __name__)
        self.restApi = Api(self.blueprint)
    
    def get_blueprint(self):
        return self.blueprint

    def get_prefix(self):
        return self.prefix

    def get_rest_api(self):
        return self.restApi

    def register_handler(self, handler, path):
        self.restApi.add_resource(handler, path)