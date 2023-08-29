import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.urls import reverse
from .models import Complaints, Suggestions


def create_complaints(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, 'create.html', {'mode': 'create_complaints'})
    elif request.method == "POST":
        title = str(request.POST.get('title')).strip()
        if len(title) <= 1:
            raise Exception('Too short title')
        
        description = str(request.POST.get('description'))
        Complaints.objects.create(
            author=request.user.username,
            title=title,
            description=description
        )
        return redirect(reverse('complaints'))
    else:
        raise Exception('Method is not allowed')


def create_suggestions(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, 'create.html', {'mode': 'create_suggestions'})
    elif request.method == "POST":
        title = str(request.POST.get('title')).strip()
        if len(title) <= 1:
            raise Exception('Too short title')

        description = str(request.POST.get('description'))
        Suggestions.objects.create(
            author=request.user.username,
            title=title,
            description=description
        )

        return redirect(reverse('suggestions'))
    else:
        raise Exception('Method is not allowed')


def complaints(request: HttpRequest) -> HttpResponse:
    # complaints_obj = Complaints.objects.all()
    complaints_obj = Complaints.objects.raw("""SELECT * FROM reviews_complaints""")
    return render(request, 'list.html', {'list': complaints_obj})


def suggestions(request: HttpRequest) -> HttpResponse:
    # suggestions_obj = Suggestions.objects.all()
    suggestions_obj = Suggestions.objects.raw("""SELECT * FROM reviews_suggestions""")
    return render(request, 'list.html', {'list': suggestions_obj})
