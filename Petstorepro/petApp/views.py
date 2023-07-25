from django.shortcuts import render
from django.http import HttpResponse
from .models import Pet

from django.views.generic import TemplateView,ListView
# Create your views here.
def PetHome(request):
    pet=Pet.objects.all()
    return render(request,'base/home.html',{'pet':pet})

#
    model=Pet
    template_name='base/home.html'
    context_objects_name='pet'

class PetListView(ListView):
    queryset = Pet.objects.all()
    template_name= 'petApp/list.html' 

  