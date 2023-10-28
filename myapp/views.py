from django.http import JsonResponse
import json
from django.shortcuts import render, HttpResponse
from .chat_bot import find_ans
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def AIchatbot(request):
    return HttpResponse("hello world")


@csrf_exempt
def chat_with_bot(request):
    if request.method == "POST":

        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

        # Now, you can access the 'text' key from the JSON data
        user_query = data.get('text')

        if not user_query:
            return JsonResponse({"error": "Invalid input format"}, status=400)
        else:
            predefined_answer = find_ans(user_query)
            return JsonResponse({"response": predefined_answer["answer"]}, status=200)

    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
