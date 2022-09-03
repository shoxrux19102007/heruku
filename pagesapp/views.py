from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
class AbautPageView (TemplateView):
    template_name = 'about.html'
class NewPageView (TemplateView):
    template_name = 'new.html'