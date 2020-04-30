from django.shortcuts import render
from recipes.models import Recipe, Chef


def index(request):
    recipe_list = Recipe.objects.all()
    return render(request,
                  'index.html',
                  {'recipe_list': recipe_list})


def chef(request, name=None):
    selected_chef = Chef.objects.get(name=name)
    chef_recipes = Recipe.objects.filter(chef=selected_chef)
    return render(request,
                  'chef.html',
                  {
                      'chef': selected_chef,
                      'recipes': chef_recipes
                  })


def recipe(request, recipe_id=None):
    selected_recipe = Recipe.objects.get(id=recipe_id)
    return render(request,
                  'recipe.html',
                  {'recipe': selected_recipe})
