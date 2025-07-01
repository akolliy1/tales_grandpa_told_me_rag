from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from django.conf import settings
from .models import UploadedNote
from .rag_utils import process_document, ask_question

class UploadNoteView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        file = request.FILES['file']
        print(f"Received file: {file.name}")
        note = UploadedNote.objects.create(file=file)
        process_document(note.file.path)
        return Response({"message": "File processed and indexed."})

class AskQuestionView(APIView):
    def post(self, request):
        question = request.data.get("question")
        print(f"Received question: {question}")
        answer = ask_question(question)
        return Response({ "answer": answer })
    
# Django template-based UI view
def chat_ui(request):
    if request.method == "POST":
        question = request.POST.get("question")
        answer = ask_question(question)
        return render(request, "core/chat.html", {"question": question, "answer": answer})
    return render(request, "core/chat.html")
