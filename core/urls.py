
from django.urls import path
from .views import UploadNoteView, AskQuestionView, chat_ui

urlpatterns = [
    path('upload-note/', UploadNoteView.as_view()),
    path('ask-question/', AskQuestionView.as_view()),
    path('chat/', chat_ui, name='chat-ui'),
]