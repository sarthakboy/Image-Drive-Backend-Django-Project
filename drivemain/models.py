from django.db import models

class MyModel(models.Model):
    image = models.ImageField(upload_to='my_image')
    text = models.CharField(max_length=255)
    date_time = models.DateTimeField(auto_now_add=True)
