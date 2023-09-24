# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, name='name')
    amount = models.IntegerField(name='amount')
    description = models.TextField(name='description')
    category = models.TextField (name='category')
    date_added = models.DateTimeField(auto_now_add=True, name='date_added')
    