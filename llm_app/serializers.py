"""
Create an API in the Django REST Framework that sends requests 
from users to the LLM and returns responses.
"""

from rest_framework import serializers

class LLMRequestSerializer(serializers.Serializer):
    prompt = serializers.CharField()
    max_tokens = serializers.IntegerField(default=30)