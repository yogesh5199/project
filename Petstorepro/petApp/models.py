from django.db import models
from django.db.models import Q
# Create your models here.
class Pet(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
    description=models.CharField(max_length=100)
    image=models.CharField(max_length=200)

class PetsQuerySet(models.QuerySet):
    def dog_list(self):
        return
    def cat_list(self):
        return
    def search(self,query):
        print(query)
        lookups= (Q(name_icontains=query) |
                 Q(animal_type_icontains=query) |
                 Q(breed_icontains=query)| Q(age_icontains=query))
        return self.filter(lookups)
class CustomManager(models.Model):
    def get_queryset(self):
        return PetsQuerySet(self.model,using=self._db)

    def get_pets_price_range(self,r1,r2):    
     def search(self,query):
        print(query)
        return self.get_queryset().search(query)