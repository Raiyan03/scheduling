from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from datetime import datetime

from django.http import HttpResponse


def greet(request):
    name = request.GET.get('name', 'Guest')
    return JsonResponse({'response': name})

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)