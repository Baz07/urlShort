from django.db import models

class short_url(models.Model):
    long_url = models.URLField('URL', max_length=1000)
    short_url = models.CharField(max_length=20)

    def __str__(self):
        return self.long_url
