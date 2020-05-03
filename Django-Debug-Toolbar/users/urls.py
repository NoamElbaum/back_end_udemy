from django.conf.urls import url
from users import views

app_name = 'users'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^data/', views.data, name='data')
]