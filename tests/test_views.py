from django.test import TestCase

class ViewTestCase(TestCase):

    def setUp(self):
        pass
        # API for self.client
        # https://docs.djangoproject.com/en/1.10/topics/testing/tools/

    def test_home(self):
        response = self.client.get('/',)
        self.assertEqual(response.status_code, 200)