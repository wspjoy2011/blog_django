from django.urls import path
from .views import *

app_name = 'base'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         post_detail, name='post_detail'),
    path('<int:post_id>/', post_share, name='post_share')
]
