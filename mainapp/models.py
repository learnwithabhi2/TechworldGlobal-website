from django.db import models

# Create your models here.
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class JobApplication(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    coverletter = models.TextField()
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name


class ClientFeedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.feedback}'
