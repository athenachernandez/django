from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    """
        This view was my main way of understanding how views worked in general.
        It's the very basic page that works with user's information.
    """
    user = request.user
    hello = "Hello, world!"
    context = {
        'user' : user,
        'hello' : hello,
    }
    return render(request, 'main/home.html', context)
    # return HttpResponse('Hello, world!')