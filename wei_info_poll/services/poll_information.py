from ..models import AverageCharactersRating, Characters, Polls
from django.db.models import Avg


def get_general_information_context():
    ratings = AverageCharactersRating.objects.using('poll_results').all()
    ratings = ratings.values('character__name', 'character__height', 'character__url')
    ratings = ratings.annotate(average_rating=Avg('rating'))

    ratings_data = [{'character__name': rating['character__name'],
                     'character__height': rating['character__height'],
                     'average_rating': round(rating['average_rating'], 4),
                     'character__url': rating['character__url']} for rating in ratings]

    context = {'ratings': ratings_data}

    return context


def get_characters_context():
    characters = Characters.objects.using('poll_results').all()

    context = {'characters': characters}

    return context


def get_polls_context():
    polls = Polls.objects.using('poll_results').all()
    polls = polls.values('id', 'user__first_name', 'concordance_factor')

    characters = Characters.objects.using('poll_results').all()

    context = {'polls': polls, 'characters': characters}

    return context
