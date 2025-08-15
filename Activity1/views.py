from django.shortcuts import render
from .models import Tweet

def home(request):
    return render(request, "home.html")

def tweet_detail_view(request, id=1):
    obj = Tweet.objects.get(id=id)
    print(obj)
    context = {
        'object': obj,
    }
    return render(request, 'tweets/detail_view.html', context)

def tweet_list_view(request):
    qs = Tweet.objects.all()
    print(qs)
    context = {
        'query': qs,
    }
    return render(request, 'tweets/list_view.html', context)

