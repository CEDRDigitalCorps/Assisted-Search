from django import forms
from django.utils import timezone


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)

    def search(self):
        # TODO add hook to run the actual search
        return [{
            "date": timezone.now(),
            "handle": "@someone",
            "text": "random test text",
            "link": "http://example.com",
        }]
