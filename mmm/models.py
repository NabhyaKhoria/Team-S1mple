from operator import le
from unicodedata import name
from django.db import models
import uuid

Category = (
    ('Technology','Technology'),
    ('Socult','Socult'),
    ('Sports','Sports'),
    ('Welfare','Welfare'),
    ('Others','Others'),
)

# Create your models here.
class Superviser(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=50,null=True)
    contact = models.CharField(max_length=30,null=True)
    por = models.CharField(max_length=150,null=True)
    linkedin = models.CharField(max_length=200, null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.fullname

class Notice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=30, choices=Category, default='Others')
    venue = models.CharField(max_length=60,null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to ='misc/')
    date = models.DateField(null=True)
    Supervisers = models.ManyToManyField(Superviser)

    def __str__(self):
        return self.name
    


