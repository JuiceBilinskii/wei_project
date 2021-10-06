from ..models import AverageCharactersRating, Characters, Polls, Answers
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
    polls = polls.values('id', 'user__first_name', 'concordance_factor', 'analysis_usage')

    answers = Answers.objects.using('poll_results').filter(poll_id=25)
    answers = answers.values('character_a__name', 'character_b__name', 'ratio_a_to_b')
    answers = answers.order_by('character_a__name', 'character_b__name')

    characters = Characters.objects.using('poll_results').all().order_by('name')
    number_of_characters = characters.count()

    poll_table = {
        'column_headers': [character.name for character in characters],
        'poll_rows': [{
            'row_header': answers[i * number_of_characters]['character_a__name'],
            'row_data': [round(answers[i * number_of_characters + j]['ratio_a_to_b'], 2) for j in range(number_of_characters)]
        } for i in range(number_of_characters)]
    }

    context = {'polls': polls,
               'number_of_characters': number_of_characters,
               'answers': answers,
               'poll_table': poll_table}

    return context
