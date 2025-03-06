import openai
import os
from dotenv import load_dotenv
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LLMRequestSerializer
from django.views.generic import TemplateView
from django.conf import settings
from django.http import HttpResponse

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

class LLMAPIView(APIView):
    def post(self, request):
        try:
            serializer = LLMRequestSerializer(data=request.data)
            if serializer.is_valid():
                prompt = serializer.validated_data["prompt"]
                
                client = openai.OpenAI(api_key=OPENAI_API_KEY)
                
                # request to Open AI
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )
                return Response({"response": response.choices[0].message.content})
            return Response(serializer.errors, status=400)
        except Exception as e:
            print(f"{e}")
            
class ReactAppView(TemplateView):
    template_name = "index.html"
    
    def get(self, request, *args, **kwargs):
        # Specify React build directory
        build_path = os.path.join(settings.BASE_DIR, "frontend", "build")
        
        # Find and return index.html of React
        index_file = os.path.join(build_path, "index.html")
        if os.path.exists(index_file):
            with open(index_file, "r") as file:
                return HttpResponse(file.read(), content_type="text/html")
        else:
            return HttpResponse("React build files not found", status=404)