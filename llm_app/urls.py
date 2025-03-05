from django.urls import path
from .views import LLMAPIView, ReactAppView


urlpatterns = [
    path("", ReactAppView.as_view(), name="react-app"),
    path('api/llm/', LLMAPIView.as_view(), name='llm_api'),
]