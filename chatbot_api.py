from django.http import JsonResponse
from appbot.chatbot_model import generate_response

def chatbot_view(request):
    user_input = request.GET.get("query", "")
    if not user_input:
        return JsonResponse({"error": "No input provided"})
    
    response = generate_response(user_input)
    return JsonResponse({"response": response})
