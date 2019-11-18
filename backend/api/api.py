
class VersionRouter:
    def __init__(self):
        self.versions = []
        from .v1_0_0.version import Version as Version_1_0_0
        v100 = Version_1_0_0()
        self.versions.append(v100)

    def register_blueprints(self, app):
        for version in self.versions:
            apiRoute = version.get_api_route()
            app.register_blueprint(apiRoute.get_blueprint(), url_prefix=apiRoute.get_prefix())