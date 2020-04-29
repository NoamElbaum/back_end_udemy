from django import forms
from model_form.models import User

class NewUser(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'