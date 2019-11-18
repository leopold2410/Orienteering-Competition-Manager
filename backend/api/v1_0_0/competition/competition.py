from flask import jsonify, make_response
from flask_restful import Resource

class Competition(Resource):
    def get(self, id):
        return make_response(jsonify({'competition': id}))

