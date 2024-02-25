from django.db import models

# Create your models here.


class Email(models.Model):
    recipient = models.EmailField()
    message = models.TextField()
    class Meta:
        app_label = 'emailapi'
