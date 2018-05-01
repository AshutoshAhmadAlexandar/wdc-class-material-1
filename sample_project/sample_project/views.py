from django.http import HttpResponse
from django.shortcuts import render


def step_1(request):
    return HttpResponse("Hello World")


def step_2(request):
    return HttpResponse("<h1>Django Class!</h1>")


def step_3(request):
    return render(request, 'example_template.html', {
        'books': [
            'The Raven',
            'Pride and Prejudice ',
            'The Man Who Was Thursday'],
        'count': 3
    })
