from django.urls import path
from .views import invites_received_view, my_profile_view

app_name = 'profiles'

urlpatterns = [
    path('myprofile/', my_profile_view, name='my-profile-view'),
    path('myinvites/', invites_received_view, name='my-invites-view'),
]