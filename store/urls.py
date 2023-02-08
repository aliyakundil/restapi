from .views import BookViewsSet
from django.urls import path
from rest_framework import routers

routers = routers.SimpleRouter()

routers.register(r'book', BookViewsSet)

urlpatterns = []
urlpatterns += routers.urls
