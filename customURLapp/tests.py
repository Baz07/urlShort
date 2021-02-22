from django.test import TestCase
from customURLapp.models import custom_url
from customURLapp.forms import CustomURLForm

# Create your tests here.
class TestModels(TestCase):
    '''
    1. Testing Custom URL Models
    '''
    def create_object(self, original_url ="https://www.linkedin.com/feed/", hash_value="info"):
        return custom_url.objects.create(original_url = original_url, hash_value=hash_value)

    def test_object_representation(self):
        obj = self.create_object()
        self.assertTrue(isinstance(obj, custom_url))
        self.assertEqual(obj.__str__(), obj.original_url)

    '''
    2. Testing Custom URL Views (Whether Page is loading proiperly or not)
    '''
    def test_customURL_view(self):
        response = self.client.get('http://127.0.0.1:8000')
        self.assertEqual(response.status_code, 200)

    '''
    3. Testing Custom URL forms with Valid data and Invalid Data
    '''
    def test_customURL_form(self):
        obj = custom_url.objects.create(original_url="https://stackoverflow.com/", hash_value="stack")
        true_data = {'original_url': obj.original_url, 'hash_value': obj.hash_value}
        form = CustomURLForm(data=true_data)
        self.assertFalse(form.is_valid())
    
    def test_customURL_invalidform(self):
        obj = custom_url.objects.create(original_url="https://www.facebook.com/", hash_value="")
        fake_data = {'original_url': obj.original_url, 'hash_value': obj.hash_value}
        form = CustomURLForm(data=fake_data)
        self.assertFalse(form.is_valid())

