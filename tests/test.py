import unittest2
from twisted.internet import reactor
from app import app


class TestExecutionError(unittest2.TestCase):
    def setUp(self):
        self.valid_cpfs = [18966470491, 41067304720, 39265420715, 18789862520, 39414361472,
                           13352849587, 38077892434, 2648077740, 40557499704, 98869167704]
        self.auth = {
            "user": "RodGom21",
            "password": "konsi2022*"
        }

        # creates a test client
        self.flaskapp = app.test_client()
        # propagate the exceptions to the test client
        self.flaskapp.testing = True

    def test_execute_scraper(self):
        for cpf in self.valid_cpfs:
            response = app.test_client().post(f'user_options/benefits/{cpf}', json=self.auth)
            self.assertTrue(response.status_code == 200)


if __name__ == '__main__':
    unittest2.main()
