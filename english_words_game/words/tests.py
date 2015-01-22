# coding=utf8
"Tests for words application"

from django.test import TestCase

from words.forms import EnglishWordForm


class TestEnglishWordForm(TestCase):
    "Tests EnglishWordForm"

    def test_empty(self):
        form = EnglishWordForm()
        self.assertFalse(form.is_valid())
        # import ipdb; ipdb.set_trace()
        self.assertEqual(form.errors, {})  # need to investigate why it's empty

    def test_min_length(self):
        form = EnglishWordForm({'english_word': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors,
            {'english_word': [u'Please enter at least one character']})

    def test_english_word(self):
        test_word = 'validation'
        form = EnglishWordForm({'english_word': test_word})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['english_word'], test_word)

    def test_non_english_word(self):
        test_word = 'проверка'
        form = EnglishWordForm({'english_word': test_word})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {'english_word': [u'The word is not English']})
