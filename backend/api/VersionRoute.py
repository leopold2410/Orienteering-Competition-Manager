from .ApiRoute import ApiRoute

class VersionRoute:
    def __init__(self, version):
        self.apiRoute = ApiRoute(version)
        from .handlers.CompetitionHandler import CompetitionHandlerV1
        self.apiRoute.register_handler(CompetitionHandlerV1, '/competition/<int:id>')

    def get_api_route(self):
        return self.apiRoute