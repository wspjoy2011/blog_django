from django.urls import path
from .views import *

app_name = 'base'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         post_detail, name='post_detail'),
]
