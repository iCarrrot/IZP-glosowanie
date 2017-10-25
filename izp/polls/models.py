from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    question_text = models.CharField('Treść pytania', max_length=200)
    pub_date = models.DateTimeField('Data publikacji')
    access_codes = ['AAA', 'BBB', 'CCC']  # TODO generate random codes

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Opublikowane niedawno?'

    def is_code_correct(self, code):
        return code in self.access_codes


# TODO Create SimpleQuestion class (derived from Question) with predefined, fixed set of choices - (Yes/No)
# TODO Create OpenQuestion class (derived from Question) with no predefined choices

# TODO I think we need to keep track of all votes with information about vote date and used access code. Maybe it would
#      be nice to introduce Vote model, with foreign keys to Question and Choice.

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
