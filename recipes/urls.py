from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chefs/<chef_id>', views.chefs, name='chefs'),
    path('recipes/<recipe_id>', views.recipes, name='recipes')
]
