from django.shortcuts import render
from fikr_blog.models import Document


def docunent(request):
    documents = Document.objects.all()
    return render(request, 'documet.html', {'documents': documents})
