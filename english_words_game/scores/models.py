"Models for scores application"

import datetime

from django.db import models


class Score(models.Model):
    """Model to keep a top score of user submission.

    There should be a single top record for each user,
    so at the worst (or best case) number of records will
    correspond to the number of users in the system.
    """
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    word_score = models.PositiveIntegerField(db_index=True)
    submitted_on = models.DateTimeField(auto_now=True,
                                        blank=True, db_index=True)
    word = models.TextField()

    @staticmethod
    def filter_by_day(queryset, day=None):
        if not day:
            day = datetime.date.today()
        next_day = day + datetime.timedelta(days=1)
        return queryset.filter(
            submitted_on__gte=day, submitted_on__lt=next_day)

    @classmethod
    def top_daily_scores(cls, day, count=10):
        "Return top scores for given day"
        queryset = cls.objects.select_related('user')
        return Score.filter_by_day(queryset, day)\
            .order_by('-word_score')[:count]

    @classmethod
    def get_top_score(cls, user=None):
        "Return top score object"
        scores = Score.filter_by_day(cls.objects)
        if user:
            # only personal best are stored, so omit sorting
            scores = scores.filter(user=user)
        else:
            scores = scores.order_by('-word_score')
        try:
            return scores[0]
        except IndexError:
            return None

    @staticmethod
    def calculate(word):
        "Return calculated score of submitted word"
        # TODO may be better to extract from the model
        return len(word)

    def __unicode__(self):
        return u'#{o.id} with {o.word_score} for {o.word}'\
               ' by {o.user_id} on {o.submitted_on}'.format(o=self)
