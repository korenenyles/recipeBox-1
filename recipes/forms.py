import django.forms as forms
from recipes.models import Chef


class RecipeAddForm(forms.Form):
    title = forms.CharField(label='Title', max_length=50)
    chef = forms.ModelChoiceField(label='Chef', queryset=Chef.objects.all())
    description = forms.CharField(label='Description', widget=forms.Textarea)
    time_required = forms.CharField(label='Time Required', max_length=30)
    instructions = forms.CharField(label='Instructions', widget=forms.Textarea)


class ChefAddForm(forms.ModelForm):
    class Meta:
        model = Chef
        fields = ['name', 'bio']
