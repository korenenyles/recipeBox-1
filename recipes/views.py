from django.shortcuts import render
from recipes.models import Recipe, Chef


def index(request):
    recipe_list = Recipe.objects.all()
    return render(request,
                  'index.html',
                  {'recipe_list': recipe_list})


def chefs(request, chef_id=None):
    selected_chef = Chef.objects.get(id=chef_id)
    chef_recipes = Recipe.objects.filter(chef=selected_chef)
    return render(request,
                  'chef.html',
                  {
                      'chef': selected_chef,
                      'recipes': chef_recipes
                  })


def recipes(request, recipe_id=None):
    selected_recipe = Recipe.objects.get(id=recipe_id)
    return render(request,
                  'recipe.html',
                  {'recipe': selected_recipe})
