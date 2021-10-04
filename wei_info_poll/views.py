from django.shortcuts import render
from wei_info_poll.services import get_general_information_context


def home(request):
    context = get_general_information_context()

    return render(request, 'wei_info_poll/home.html', context)
