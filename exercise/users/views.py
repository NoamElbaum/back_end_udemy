from django.shortcuts import render
from users.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def data(request):
    user_list = User.objects.order_by('f_name')
    data_dict = {'user_list': user_list}
    return render(request, 'data.html', data_dict)