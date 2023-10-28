from django.urls import path
from . import views

urlpatterns = [
    path("ai", views.chat_with_bot, name="aaa"),
    path("", views.AIchatbot, name="bbbb")
]
