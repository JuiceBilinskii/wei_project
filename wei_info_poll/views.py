from django.shortcuts import render
from .services import get_general_information_context, get_characters_context, get_polls_context


def home(request):
    context = get_general_information_context()

    return render(request, 'wei_info_poll/home.html', context)


def characters(request):
    context = get_characters_context()

    return render(request, 'wei_info_poll/characters.html', context)


def polls(request):
    context = get_polls_context()

    return render(request, 'wei_info_poll/polls.html', context)
