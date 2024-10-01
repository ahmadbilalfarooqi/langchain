from django import forms

class RecipeForm(forms.Form):
    receipe_message = forms.CharField(max_length=255, widget=forms.TextInput
                                      (attrs={'placeholder': 'Enter a recipe about any food'}))