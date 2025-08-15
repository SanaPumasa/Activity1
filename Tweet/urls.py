from django.urls import path

from Activity1.views import tweet_list_view, tweet_detail_view
from .views import *

urlpatterns = [

    path('', tweet_list_view, name='list_view'),
    path('1/', tweet_detail_view, name='detail_view'),
]