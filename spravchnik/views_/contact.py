from django.shortcuts import render, redirect
from user.models import Contact
from user.forms import ContactForm


def contact_create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
        return render(request, 'contact.html', {"form": form})
