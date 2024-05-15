from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def greet(request):
    name = request.GET.get('name', 'Guest')
    return JsonResponse({'response': name})

