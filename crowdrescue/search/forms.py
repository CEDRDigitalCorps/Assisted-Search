import logging

from django import forms
from django.utils import timezone
from spicey import Spicey

log = logging.getLogger(__name__)


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
    query_type = forms.ChoiceField(
        choices=[
            ("filter", "Filter"),
            ("bayesian", "Bayesian"),
        ],
        initial="bayesian"
    )

    def search(self):
        # TODO add hook to run the actual search
        # tweets = requests.get("http://www.example.com")  # will be replaced by twitterbot API address
        # response = json.loads(tweets)  # used if we need to deserialize the response
        # return response --> this will send the dictionary over to the template
        if self.cleaned_data["query_type"] == "bayesian":
            try:
                spicey_bot = Spicey(bot_mode=False)
                results = spicey_bot.bayesian_search(
                    self.cleaned_data["query"]
                )
            except Exception as e:
                log.info(e)
                print(e)
                results = [{"text": "Oops, an error occurred"}]
        else:
            return [{
                "created_at": timezone.now(),
                "screen_name": "@filter",
                "text": "filtering is not operational at present",
                "source": "http://example.com",
            }]
        return results
