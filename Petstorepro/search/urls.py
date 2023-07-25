from django.urls import path
from search.views import DogListView,CatListView,SearchQueryView,SearchPetView

app_name="search"
urlpatterns = [
    path('dog/', DogListView.as_view(),name="doglist"),
    path('cat/', CatListView.as_view(),name="catlist"),
    path('searchqview/', SearchQueryView.as_view(),name="q"),
    path('searchview/', SearchPetView.as_view(),name="query"),
]