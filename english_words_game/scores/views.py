"Views for scores application"

import datetime

from django.shortcuts import render

from scores.models import Score


# TODO add caching
def top_scores_list(request):
    "View shows top 10 daily scores even for non logged users"
    today = datetime.date.today()
    top10 = list(Score.top_daily_scores(today, 10))
    return render(request, 'top_scores.html', dict(scores=top10))
