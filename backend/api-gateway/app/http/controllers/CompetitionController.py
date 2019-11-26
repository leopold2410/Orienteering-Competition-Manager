"""A CompetitionController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.Competition import Competition
from masonite.validation import Validator

class CompetitionController(Controller):
    """CompetitionController Controller Class."""

    def __init__(self, request: Request):
        """CompetitionController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        return {'controller':'Competition'}

    def store(self, request: Request, validator: Validator):
        errors = request.validate(validator.required(['name','description']))

        if errors:
            return {'errors': errors}

        Competition.create(
            name=request.input('name'),
            description=request.input('description')
        )

        return {'status':'success'}


