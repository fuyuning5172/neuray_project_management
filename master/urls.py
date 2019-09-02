from django.urls import path
from master.views import *

app_name = 'master'

urlpatterns = [
    path('index/', index, name='index'),
    path('login/', login, name='login'),
    path('test/', test, name='test'),
    path('test/update/1', update_person, name='update_person'),
    path('test/delete/1', delete_person, name='delete_person')

    # path('main/',main,name='main')
]
