import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chatbot_project.settings import OPENAI_API_KEY

@csrf_exempt
def chat(request):
    if request.method=='POST':
        user_message = request.POST.get('message', '')

        # Appel API OpenAI
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "content-type": "application/json",
        } 
        data = {
            "model":"gpt-4o-mini",
            "messages": [
                {"role": "user", "content": user_message}
            ],
            "max_tokens":1000,
        }

        response = requests.post(url, headers=headers, json=data)
        print("++++++++++++++++++++++", response.status_code)
        if response.status_code == 200:
            chat_response = response.json()['choices'][0]['message']['content']
            return JsonResponse({'response': chat_response})
        else:
            return HttpResponse({"error": "erreur lors de l'appel à l'API OpenAI"}, status=500)
    return render(request, 'chatbot/chat.html')


