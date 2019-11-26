from flask import jsonify, make_response
from flask_restplus import Resource

class CompetitionHandlerV1(Resource):
    def __init__(self, *args, **kwargs):
        self.version = kwargs['version']

    def get(self, id):
        return make_response(jsonify({'competition': id, 'version':self.version}))

