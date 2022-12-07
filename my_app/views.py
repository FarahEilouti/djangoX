from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Car
from django.urls import reverse_lazy
# Create your views here.


class CarListView(ListView):

    template_name= 'car/car_list.html'
    model=Car


class CarDetailView(DetailView):

    template_name= 'car/car_detail.html'
    model=Car


class CarCreateView(CreateView):

    template_name= 'car/car_create.html'
    model=Car
    fields=['title', 'purchaser', 'description']

class CarUpdateView(UpdateView):

    template_name= 'car/car_update.html'
    model=Car
    fields=['title', 'purchaser', 'description']

class CarDeleteView(DeleteView):

    template_name= 'car/car_delete.html'
    model=Car
    success_url=reverse_lazy('car_list')


