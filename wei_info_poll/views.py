from django.shortcuts import render
from .services import poll_information


def home(request):
    context = poll_information.get_general_information_context()

    return render(request, 'wei_info_poll/home.html', context)


def characters(request):
    context = poll_information.get_characters_context()

    return render(request, 'wei_info_poll/characters.html', context)


def polls(request):
    context = poll_information.get_polls_context()

    return render(request, 'wei_info_poll/polls.html', context)
