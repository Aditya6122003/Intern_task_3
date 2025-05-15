# Create your views here.
from django.shortcuts import render

def chatbot_page(request):
    return render(request, "chatbot.html")
