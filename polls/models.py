import datetime

from django.db import models
from django.utils import timezone

# models are the groups you can update, like 'cards'
class Question(models.Model):
    #CharField: character fields. required args: max_length
    #DateTimeField: date fields
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Player (models.Model):
    game_tag = models.CharField(max_length=50)
    uID = models.IntegerField(default=0)
    # player variable means this is attached to player class
    character_main = models.CharField(max_length=50, default = '')
    characters_obtained = models.IntegerField(default=0)
    days_played = models.IntegerField(default=0)

    def __str__(self):
        return self.game_tag