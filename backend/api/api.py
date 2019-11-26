
class VersionRouter:
    def __init__(self):
        self.versions = []
        from .VersionRoute import VersionRoute
        self.versions.append(VersionRoute('v1.0.0'))
        self.versions.append(VersionRoute('v1.0'))
        self.versions.append(VersionRoute('v1'))

    def register_blueprints(self, app):
        for version in self.versions:
            apiRoute = version.get_api_route()
            app.register_blueprint(apiRoute.get_blueprint(), url_prefix=apiRoute.get_prefix())