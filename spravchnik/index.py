from django.shortcuts import render





def index2(request):
    return render(request, 'post.html')


def contact(request):
    return render(request, 'contact.html')
