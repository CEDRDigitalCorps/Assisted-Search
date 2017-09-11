from django import forms
from django.utils import timezone


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
    query_type = forms.ChoiceField(
        choices=[
            ("filter", "Filter"),
            ("bayesian", "Bayesian"),
        ],
        initial="filter"
    )

    def search(self):
        # TODO add hook to run the actual search
        # tweets = requests.get("http://www.example.com")  # will be replaced by twitterbot API address
        # response = json.loads(tweets)  # used if we need to deserialize the response
        # return response --> this will send the dictionary over to the template
        if self.cleaned_data["query_type"] == "bayesian":
            # TODO run bayesian search
            name = "@bayesian"
        else:
            # TODO run bayesian search
            name = "@filter"

        return [{
            "created_at": timezone.now(),
            "screen_name": name,
            "text": "random test text",
            "source": "http://example.com",
        }]
