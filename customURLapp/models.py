from django.db import models

## Model for CustomURLapp
class custom_url(models.Model):
    original_url = models.URLField('Enter a Long URL', max_length=1000) ## For User Provided URL
    hash_value = models.TextField('Short/Hash value', unique=True) ## For User Provided Hash Value (!!UNIQUE!!)

    def __str__(self):
        return self.original_url