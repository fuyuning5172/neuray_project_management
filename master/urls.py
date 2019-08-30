from django.urls import path
from master.views import *

app_name = 'app'

urlpatterns = [
    path('index/', index, name='index'),
    path('login/', login, name='login'),
    path('test/', test, name='test')
    # path('main/',main,name='main')
]
