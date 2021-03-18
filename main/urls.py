from django.urls import path
from .import views

urlpatterns = [path('', views.test, name = 'test')]
# new entry (1 list) specify path views.FUNCTIONNAME (views.home, views.about)