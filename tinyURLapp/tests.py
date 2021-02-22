from django.test import TestCase
from tinyURLapp.models import short_url
from tinyURLapp.forms import URLForm
from tinyURLapp.shortLogic import Shortner


# Create your tests here.
class SimpleTest(TestCase):
    '''
    1. Testing Shortner Logic (New Short URL Length < Original URL Length)
    '''
    def test_length_check(self):
        long_url = "https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c"
        short_url = Shortner().shorten_url(long_url)
        self.assertLess(len(short_url), len(long_url))
    
    '''
    2. Testing Exisitng URLs in Shortner
    '''
    def test_existing_url_check(self):
        long_url1 = "google.com"
        short_url1 = Shortner().shorten_url(long_url1)

        long_url2 = "google.com"
        short_url2 = Shortner().shorten_url(long_url2)

        self.assertEqual(short_url1, short_url2)


    '''
    3. Testing Models
    '''
    def create_object(self, long_url ="https://www.linkedin.com/feed/"):
        return short_url.objects.create(long_url = long_url)
        
    def test_object_representation(self):
        obj = self.create_object()
        self.assertTrue(isinstance(obj, short_url))
        self.assertEqual(obj.__str__(), obj.long_url)