
from django.urls import path
from .views import article_list
from .views import user_list

urlpatterns = [
    path('article/', article_list),
    path('user/', user_list),
]
