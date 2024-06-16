from django.shortcuts import render

# Create your views here.


def comments(request):
    return render(request, 'comments.html', {})
