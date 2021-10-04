from ..models import Characters


def get_general_information_context():
    characters = Characters.objects.using('poll_results').all()

    characters_data = [{'name': character.name, 'height': character.height} for character in characters]
    context = {'characters_data': characters_data}

    return context
