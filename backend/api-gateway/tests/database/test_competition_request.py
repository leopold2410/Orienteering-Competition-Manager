"""Testcompetition_request Testcase."""

from masonite.testing import TestCase
from app.Competition import Competition

class TestCompetitionRequest(TestCase):
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
    def test_get_competitions(self):
        self.get('/api/v1.0.0/competitions').assertIsStatus(200)

    def test_create(self):
        self.assertFalse(Competition.find(1))
        self.post('/api/v1.0.0/competition', {'name': 'competition1', 'description': 'decsription1'}).assertIsStatus(
            200)
        self.assertTrue(Competition.find(1))
