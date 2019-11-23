"""Web Routes."""

from masonite.routes import Get, Post, RouteGroup
from app.http.controllers.CompetitionController import CompetitionController
ROUTES = [
    Get('/', 'WelcomeController@show').name('welcome'),
    RouteGroup([
        RouteGroup([
            Get('/competitions', CompetitionController.show),
            Post('/competition', CompetitionController.store)
            ], prefix="/v1.0.0")
    ], prefix="/api")
]
