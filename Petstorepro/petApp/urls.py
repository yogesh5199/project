from django.urls import path
from petApp import views

urlpatterns = [
    path('',views.PetHome,name='pet'),
    path('petlist/', views.PetListView.as_view(),name='list'),
    
]