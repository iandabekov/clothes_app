from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView

from .models import Clothes


# Create your views here.


class Home(ListView):
    paginate_by = 2
    model = Clothes
    template_name = 'clothes_shop/index.html'
    context_object_name = 'clothes'
    queryset = Clothes.objects.all().order_by('category')


class Retrieve_clothes(DetailView):
    model = Clothes
    template_name = 'clothes_shop/retrieve.html'
    context_object_name = 'cloth'
