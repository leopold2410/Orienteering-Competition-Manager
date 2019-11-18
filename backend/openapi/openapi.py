from flask_swagger_ui import get_swaggerui_blueprint

class OpenApi:
    def __init__(self, openapi_url, api_url):
        self.openapi_url = openapi_url
        self.api_url = api_url
        self.blueprint = get_swaggerui_blueprint(
            self.openapi_url,
            self.api_url,
            config={
                'app_name': "Orienteering Competition Manager"
            }
        )

    def register_blueprint(self, app):
        app.register_blueprint(self.blueprint, url_prefix=self.openapi_url)