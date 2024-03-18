from django import forms
from user.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'id': "name",
                       "placeholder": "name"}
            ),
            'body': forms.TextInput(
                attrs={'class': 'form-control', 'id': "body",
                       "placeholder": "body"}
            )
        }
