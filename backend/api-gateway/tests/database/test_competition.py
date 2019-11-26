"""TestCompetition Testcase."""

from masonite.testing import TestCase
from app.Competition import Competition

class TestCompetition(TestCase):

    """All tests by default will run inside of a database transaction."""
    transactions = True

    def setUp(self):
        """Anytime you override the setUp method you must call the setUp method
        on the parent class like below.
        """
        super().setUp()

    def setUpFactories(self):
        """This runs when the test class first starts up.
        This does not run before every test case. Use this method to
        set your database up.
        """
        result = Competition.create(
            name='competition1',
            description='description1'
        )


    def test_creates_competition(self):
        self.assertTrue(Competition.find(1))
