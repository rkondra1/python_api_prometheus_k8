import unittest
from src import app as source_code
my_obj = source_code.CustomCollector

class TestStringMethods(unittest.TestCase):

    def test_status(self):
        print("TEST-1--STATUS CODE :: ", source_code.metrics().status_code)

    def test_api_response(self):
        response = source_code.app.test_client().get('/metrics')
        self.assertEqual(response.status_code, 200 )
        print("TEST-2--API Response Code :: ", response.status_code)

if __name__ == '__main__':
    unittest.main()