# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, TemplateView
from crowdrescue.search.forms import SearchForm


class HomeView(TemplateView):
    template_name = "home.html"


@method_decorator(csrf_exempt, name="dispatch")
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
