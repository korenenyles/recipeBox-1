from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addchef/', views.chef_add, name='new_chef'),
    path('chefs/<chef_id>', views.chefs, name='chefs'),
    path('addrecipe/', views.recipe_add, name='new_recipe'),
    path('recipes/<recipe_id>', views.recipes, name='recipes')
]
