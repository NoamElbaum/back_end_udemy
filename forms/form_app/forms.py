from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower != 'z':
        raise forms.ValidationError("NAME NEEDS TO START WITH Z")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter yout email again:')
    text = forms.CharField(widget=forms.Textarea)
    botcather = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

    # menual validator
    # def clean_botcather(self):
    #     botcather = self.cleaned_data['botcather']
    #     if len(botcather):
    #         raise forms.ValidationError('GOTCHA BOT!')

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        v_mail = all_clean_data['verify_email']
        if email != v_mail:
            raise forms.ValidationError('Email dont match')




