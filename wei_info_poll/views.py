from django.shortcuts import render


def home(request):
    return render(request, 'wei_info_poll/home.html')
