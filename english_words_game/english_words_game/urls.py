from django.urls import include, path
from django.contrib import admin
from django.contrib.auth.views import login

import words.views
import scores.views

urlpatterns = [
    path(r'', scores.views.top_scores_list, name='top-scores'),
    path('submit/', words.views.word_submission, name='word-submission'),
    path(r'accounts/login/', login, {'extra_context': {'next': '/'}}, name='login'),
    path(r'accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]
