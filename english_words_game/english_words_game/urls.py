from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'scores.views.top_scores_list', name='top-scores'),
    url('^submit/$', 'words.views.word_submission', name='word-submission'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'extra_context': {'next': '/'}}, name='login'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)
