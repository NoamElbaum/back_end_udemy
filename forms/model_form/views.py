from django.shortcuts import render
from model_form.forms import NewUser

# Create your views here.
def index(request):
    return render(request, 'model_form/index.html')

def users(request):

    form = NewUser()

    if request.method == 'POST':
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'model_form/users.html', {'form': form})

def help(request):

    return render(request, 'model_form/help.html')