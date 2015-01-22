"""Words Application Forms"""

from django.utils.translation import gettext as _
from django import forms
from nltk.corpus import wordnet


class EnglishWordForm(forms.Form):
    "Form for submission of English word"

    TOO_SHORT_MSG = _("Please enter at least one character")

    english_word = forms.CharField(min_length=1,
        error_messages={
            'min_length': TOO_SHORT_MSG,
            'required': TOO_SHORT_MSG,
        })

    # TODO extract field cleanup as validator
    def clean_english_word(self):
        word = self.cleaned_data['english_word']
        if not wordnet.synsets(word):
            raise forms.ValidationError(_("The word is not English"))
        return word
