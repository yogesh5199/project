from django.db import models
from django.contrib.auth.models import User
from search.models import Pet
# Create your models here.
class Cart(models.Model):
    cart_id=models.CharField(max_length=200,blank=True)
    pet=models.ForeignKey(Pet,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    totalprice=models.FloatField(default=0.00)
    timestamp=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='cart'