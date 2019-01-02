from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('WELCOME HOME PAGE')


def about(request):
    return  HttpResponse('ABOUT PAGE')
