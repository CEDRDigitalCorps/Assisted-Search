# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views.generic import FormView
from crowdrescue.search.forms import SearchForm


@method_decorator(login_required, name="dispatch")
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

    def form_invalid(self, form):
        response = super(SearchView, self).form_invalid(form)
        if self.request.is_ajax():
            return HttpResponse(
                render_to_string("search/results.html", {"results": []})
            )
        return response
