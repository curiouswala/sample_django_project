from django.test import TestCase
from django.test import Client

# Create your tests here.

class TestView(TestCase):
    @classmethod
    def test_hello_view(self):
        print('TestHelloView: Simple Test To Check If Hello View Is Working')
        c = Client()
        response = c.get('/hello/Hasan')
        result = response.status_code == 200
        self.assertTrue(result, result)
