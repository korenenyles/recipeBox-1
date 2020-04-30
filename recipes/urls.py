from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chef/<name>', views.chef, name='chef'),
    path('recipe/<recipe_id>', views.recipe, name='recipe')
]
