from django.db import models


class Users(models.Model):
    id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Characters(models.Model):
    name = models.CharField(max_length=150)
    height = models.IntegerField()
    short_description = models.CharField(max_length=1000)
    url = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'characters'


class Polls(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    date_completed = models.DateTimeField()
    analysis_usage = models.BooleanField()
    concordance_factor = models.FloatField()

    class Meta:
        managed = False
        db_table = 'polls'


class Answers(models.Model):
    poll = models.ForeignKey('Polls', models.DO_NOTHING)
    character_a = models.ForeignKey('Characters', models.DO_NOTHING, related_name='character_a')
    character_b = models.ForeignKey('Characters', models.DO_NOTHING, related_name='character_b')
    ratio_a_to_b = models.FloatField()

    class Meta:
        managed = False
        db_table = 'answers'
        unique_together = (('poll', 'character_a', 'character_b'),)


class AverageCharactersRating(models.Model):
    poll = models.ForeignKey('Polls', models.DO_NOTHING)
    character = models.ForeignKey('Characters', models.DO_NOTHING)
    rating = models.FloatField()

    class Meta:
        managed = False
        db_table = 'average_characters_rating'
