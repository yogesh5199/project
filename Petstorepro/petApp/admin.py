from django.contrib import admin
from .models import Pet
# Register your models here.
class PetAdmin(admin.ModelAdmin):
    list_display=['name','price','description','image']
admin.site.register(Pet)
