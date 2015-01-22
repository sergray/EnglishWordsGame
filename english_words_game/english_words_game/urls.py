from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'english_words_game.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    url('^$', 'words.views.word_submission', name='word-submission'),
    # url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/login', 'django.contrib.auth.views.login',
        {'extra_context': {'next': '/'}}, name='login'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)
