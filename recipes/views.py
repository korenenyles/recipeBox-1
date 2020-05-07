from recipes.forms import ChefAddForm, RecipeAddForm, LoginForm
from recipes.models import Recipe, Chef
from django.shortcuts import render
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required, login_required


def index(request):
    recipe_list = Recipe.objects.all()

    if request.user.is_authenticated:
        current_user = Chef.objects.get(user=request.user)
        current_user_name = current_user.name
    else:
        current_user_name = None

    return render(request,
                  'index.html',
                  {
                      'recipe_list': recipe_list,
                      'current_user': current_user_name
                  })


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


@login_required
def chef_add(request):

    # POST request handling
    if request.method == 'POST':
        form = ChefAddForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(
                username=data['username'], password=data['password'])
            new_chef = Chef(
                name=data['name'],
                bio=data['bio'],
                user=new_user
            )
            new_chef.save()
            return HttpResponseRedirect(reverse('index'))

    # GET request handling

    # allow users that are staff to access form and add new chefs
    if request.user.is_staff:
        form = ChefAddForm()
        return render(request,
                      'gen_form.html',
                      {
                          'page_title': 'New Chef',
                          'button_value': 'Submit',
                          'form': form
                      })

    # users that are not staff are forbidden from looking at page
    return render(request, 'forbidden.html')


@login_required
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
    chef_field = form.fields['chef']
    chef_field.initial = request.user

    # users that aren't staff can't add recipes for anyone but themselves
    if not request.user.is_staff:
        chef_field.queryset = Chef.objects.filter(user=request.user)

    return render(request,
                  'gen_form.html',
                  {
                      'page_title': 'New Recipe',
                      'button_value': 'Submit',
                      'form': form
                  })


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user_creds = form.cleaned_data
            user = authenticate(
                request=request,
                username=user_creds['username'],
                password=user_creds['password']
            )

            if user:
                login(request=request, user=user)

                if request.GET.get('next'):
                    redirect_path = request.GET['next']
                    return HttpResponseRedirect(redirect_path)

                return HttpResponseRedirect(reverse('index'))

    form = LoginForm()
    return render(request,
                  'gen_form.html',
                  {
                      'page_title': 'Login',
                      'button_value': 'Login',
                      'form': form
                  })


def user_logout(request):
    logout(request=request)
    return HttpResponseRedirect(reverse('index'))
