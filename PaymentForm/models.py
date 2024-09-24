from django.db import models
from django.db import models
from authentication.models import User

class Payment(models.Model):
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=2000.00)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

