"Views for words application"
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from words.forms import EnglishWordForm


@login_required
def word_submission(request):
    if request.method == 'POST':
        form = EnglishWordForm(request.POST)
        if form.is_valid():
            pass  # TODO save submission and redirect to top-scores page
    else:
        form = EnglishWordForm()
    return render(request, 'word_submission.html', dict(form=form))
