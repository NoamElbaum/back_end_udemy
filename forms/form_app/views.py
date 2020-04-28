from django.shortcuts import render
from . import forms
# Create your views here.
def index(request):
    return render(request, 'form_app/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form_info = forms.FormName(request.POST)

        if form_info.is_valid():
            print("VALADATION SUCCESS!")
            print('NAME: '+form_info.cleaned_data['name'])
            print('EMAIL: '+form_info.cleaned_data['email'])
            print('TEXT: '+form_info.cleaned_data['text'])

    return render(request, 'form_app/form_page.html', {'form': form})
