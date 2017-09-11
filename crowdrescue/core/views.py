# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


@method_decorator(login_required, name="dispatch")
class HomeView(TemplateView):
    template_name = "home.html"


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))
