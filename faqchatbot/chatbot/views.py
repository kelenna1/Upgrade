from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import os
import requests
from dotenv import load_dotenv
from .models import FAQ
from .serializers import FAQSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class AskView(APIView):
    def post(self, request):
        question = request.data.get('question')
        if not question:
            return Response({"error": "Question is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try: 
            api_key = os.getenv('OPENROUTER_API_KEY')
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            }
            payload = {
                "model": "openai/gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": question},
                ],
            }

            response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
            response.raise_for_status()
            data= response.json()
            answer = data['choices'][0]['message']['content'].strip()

            # Save to database
            faq = FAQ.objects.create(question=question, answer=answer)
            serializer = FAQSerializer(faq)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
    def get(self, request):
        faqs = FAQ.objects.all().order_by('-created_at')
        serializer = FAQSerializer(faqs, many=True)
        return Response(serializer.data)
    
def index(request):
    return render(request, 'chatbot/index.html')


