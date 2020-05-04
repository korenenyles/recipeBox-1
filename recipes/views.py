from recipes.forms import ChefAddForm, RecipeAddForm
from recipes.models import Recipe, Chef
from django.shortcuts import render
from django.shortcuts import reverse
from django.http import HttpResponseRedirect


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


def chef_add(request):
    # POST request handling
    if request.method == 'POST':
        form = ChefAddForm(data=request.POST)
        form.save()
        return HttpResponseRedirect(reverse('index'))

    # GET request handling
    form = ChefAddForm()
    return render(request,
                  'gen_form.html',
                  {
                      'page_title': 'New Chef',
                      'form': form
                  })


def recipe_add(request):
    # POST request handling
    if request.method == 'POST':
        form = RecipeAddForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_recipe = Recipe(
                title=data['title'],
                chef=data['chef'],
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions']
            )
            new_recipe.save()
            return HttpResponseRedirect(reverse('index'))

    # GET request handling
    form = RecipeAddForm()
    return render(request,
                  'gen_form.html',
                  {
                      'page_title': 'New Recipe',
                      'form': form
                  })
