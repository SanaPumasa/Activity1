from django.shortcuts import render

# def forms(request):
#     return render(request, "forms.html")

def tweet_detail_view(request, id=1):
    return render(request, 'tweets/detail_view.html')

def tweet_list_view(request):
    return render(request, 'tweets/list_view.html')

