"Views for words application"
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from words.forms import EnglishWordForm
from scores.models import Score


@login_required
def word_submission(request):
    word_score = None
    personal_best = False
    overall_record = False

    if request.method == 'POST':
        form = EnglishWordForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['english_word']
            word_score = Score.calculate(word)
            # TODO wrap in transaction, but it's going to become a bottleneck as number of users grow
            top_score = Score.get_top_score()
            personal_score = Score.get_top_score(request.user)

            if not personal_score:
                personal_best = True
                personal_score = Score.objects.create(
                    user=request.user, word=word, word_score=word_score)
            else:
                personal_best = personal_score.word_score < word_score
                if personal_best:
                    personal_score.word = word
                    personal_score.word_score = word_score
                    personal_score.save()
            if top_score:
                overall_record = top_score.word_score < word_score
            else:
                overall_record = True
    else:
        form = EnglishWordForm()
    return render(request, 'word_submission.html', 
        dict(
            form=form,
            personal_best=personal_best,
            overall_record=overall_record,
            word_score=word_score,
        ))
