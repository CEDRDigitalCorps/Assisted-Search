# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views.generic import FormView
from crowdrescue.core.views import decorators
from crowdrescue.search.forms import SearchForm


@method_decorator(decorators, name="dispatch")
class SearchView(FormView):
    template_name = "home.html"
    form_class = SearchForm

    def form_valid(self, form):
        data = form.search()

        context = {"results": data}
        if self.request.is_ajax():
            return HttpResponse(
                render_to_string("search/results.html", context)
            )
        return TemplateResponse(
            self.request,
            self.template_name,
            context
        ).render()
