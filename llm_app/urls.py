from django.urls import path
from .views import LLMAPIView

urlpatterns = [
    path('api/llm/', LLMAPIView.as_view(), name='llm_api'),
]