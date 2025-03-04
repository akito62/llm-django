import openai
import os
from dotenv import load_dotenv
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LLMRequestSerializer

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

class LLMAPIView(APIView):
    def post(self, request):
        try:
            serializer = LLMRequestSerializer(data=request.data)
            if serializer.is_valid():
                prompt = serializer.validated_data["prompt"]
                print(prompt)
                print("prompt↑")
                max_tokens = serializer.validated_data["max_tokens"]
                print(max_tokens)
                print("max_tokens↑")
                
                client = openai.OpenAI(api_key=OPENAI_API_KEY)
                
                # request to Open AI
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=max_tokens
                )
                return Response({"response": response.choices[0].message.content})
            return Response(serializer.errors, status=400)
        except Exception as e:
            print(f"例外発生！！⭐️: {e}")