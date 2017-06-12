# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class HomeView(View):
    template_name = 'website/home.html'

    def get(self, request, *args, **kwargs):
        data = dict()
        return render(request, self.template_name, data)
