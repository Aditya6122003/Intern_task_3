from django.urls import path
from .views import chatbot_page
from .chatbot_api import chatbot_view

urlpatterns = [
    path("chatbot/", chatbot_view, name="chatbot_api"),  # Chatbot API
    path("chat/", chatbot_page, name="chatbot_page"),  # Chatbot UI
]
