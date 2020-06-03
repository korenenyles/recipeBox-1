from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addchef/', views.chef_add, name='new_chef'),
    path('chefs/<chef_id>/', views.chefs, name='chefs'),
    path('addrecipe/', views.recipe_add, name='new_recipe'),
    path('recipes/<recipe_id>/', views.recipes, name='recipes'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('edit/<int:recipe_id>/', views.edit_recipe, name='edit'),
    path('favorite/<int:id>/', views.favorite_view, name='favorite'),
    path('unfavorite/<int:id>/', views.unfavorite_view, name='unfavorite'),
    
]