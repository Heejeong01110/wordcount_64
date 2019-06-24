from django.db import models

# Create your models here.

class Text(models.Model):
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.body