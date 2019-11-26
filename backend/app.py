import argparse
from flask import Flask, jsonify, make_response
from flask_restplus import Api, Resource

app = Flask(__name__)


from api.api import VersionRouter
versionRouter = VersionRouter()
versionRouter.register_blueprints(app)

from openapi.openapi import OpenApi
openapi = OpenApi(openapi_url = '/openapi',
    api_url = '/static/swagger.json')
openapi.register_blueprint(app)

@app.errorhandler(400)
def handle_400_error(_error):
    """Return a http 400 error to client"""
    return make_response(jsonify({'error': 'Misunderstood'}), 400)


@app.errorhandler(401)
def handle_401_error(_error):
    """Return a http 401 error to client"""
    return make_response(jsonify({'error': 'Unauthorised'}), 401)


@app.errorhandler(404)
def handle_404_error(_error):
    """Return a http 404 error to client"""
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(500)
def handle_500_error(_error):
    """Return a http 500 error to client"""
    return make_response(jsonify({'error': 'Server error'}), 500)

	
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Orienteering Competition Manager")
	parser.add_argument('--debug', action='store_true', help="debug mode")
	parser.add_argument('--port', type=int, default=8080, help="port")
	args = parser.parse_args()   

	if args.debug:
		print("Running in debug mode")
		app.run(host='0.0.0.0', port=args.port, debug=True)
	else:
		app.run(host='0.0.0.0', port=args.port, debug=False)