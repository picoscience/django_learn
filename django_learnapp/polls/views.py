from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('You are in the Index page')


def detail(request, question_id):
    return HttpResponse(f'You are seeing the Question number {question_id}')


def results(request, question_id):
    return HttpResponse(f'You are seeing the results to Question number {question_id}')


def vote(request, question_id):
    return HttpResponse(f'You are voting to Question number {question_id}')