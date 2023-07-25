from django.db import models
from django.contrib.auth.models import User
from petApp.models import Pet
# Create your models here.
class Payment(models.Model):
    Payment_id=models.CharField(max_length=100)
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    amount_paid=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Payment_id

class Orders(models.Model):
    status=(('new','new'),('pending','pending'),('delivered','delivered'),('cancelled','cancelled'))
    status=[
        ('AP','Andhra Pradesh'),
        ('TN','Tamil Nadu'),
        ('BR','Bihar'),
        ('KL','Kerela'),
    ]
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    payment=models.ForeignKey(Payment,on_delete=models.SET_NULL,blank=True,null=True)
    order_number=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100,choices=status,default='new')
    ip=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.User.first_name

class OrderPet(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    payment=models.ForeignKey(Payment,on_delete=models.SET_NULL,blank=True,null=True)
    pet=models.ForeignKey(Pet,on_delete=models.SET_NULL,blank=True,null=True)
    quantity=models.IntegerField()
    pet_price=models.FloatField()
    is_order=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pet.name