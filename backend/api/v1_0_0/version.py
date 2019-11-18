from ..ApiRoute import ApiRoute

class Version:
    def __init__(self):
        self.apiRoute = ApiRoute('v1.0.0')
        from .competition.competition import Competition
        self.apiRoute.register_handler(Competition, '/competition/<int:id>')

    def get_api_route(self):
        return self.apiRoute