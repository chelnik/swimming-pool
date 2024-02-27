from django.shortcuts import render


def index(request):
    return render(request, 'pool_app/index.html')
