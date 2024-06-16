from django.shortcuts import render, redirect
from django.views import View
from . import models
from brand.models import Brand
from comments.models import Comment
from comments.form import CommentForm
# Create your views here.


def car(request, id):
    car = models.Car.objects.get(pk=id)
    comments = Comment.objects.filter(car=id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        print(form)
        if form.is_valid():
            commnet = form.save(commit=False)
            commnet.car = car
            commnet.save()
    form = CommentForm()
    return render(request, 'car.html', {'car': car, 'form': form, 'comments': comments})


def cars(request, id=None):
    cars = models.Car.objects
    brands = Brand.objects.all()
    if id:
        cars = cars.filter(brand=id)
    else:
        cars = cars.all()
    return render(request, 'cars.html', {'cars': cars, 'brands': brands, 'id': id})


class Cars(View):
    def get(self, request, id=None):
        cars = models.Car.objects
        brands = Brand.objects.all()
        if id:
            cars = cars.filter(brand=id)
        else:
            cars = cars.all()
        return render(request, 'cars.html', {'cars': cars, 'brands': brands, 'id': id})
