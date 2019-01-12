from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,DetailView,
                                CreateView,UpdateView,DeleteView)
from . import models
from django.urls import reverse_lazy


class HomePage(TemplateView):
    template_name = 'index.html'




