from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)

    def search(self):
        # TODO add hook to run the actual search
        return [self.cleaned_data["query"]]
