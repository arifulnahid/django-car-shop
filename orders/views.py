from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order
from cars.models import Car

# Create your views here.


@login_required
def buy_now(request, id):
    user = request.user
    car = Car.objects.get(pk=id)
    Order.objects.create(customer=user, car=car)
    car.qunatity -= 1
    car.save()
    return redirect('orders')


@login_required
def orders(request):
    user = request.user
    orders = Order.objects.filter(customer=user)
    return render(request, 'profile.html', {'orders': orders})
