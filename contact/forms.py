# contact/forms.py
from django import forms


class ContactForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )

    first_name = forms.CharField(
        required=True,
        max_length=60,
        widget=forms.TextInput(attrs={
            "id": "fname",
            "class": "form-control"
        })
    )
    last_name = forms.CharField(
        required=True,
        max_length=60,
        widget=forms.TextInput(attrs={
            "id": "lname",
            "class": "form-control"
        })

    )
    from_email = forms.EmailField(
        required=True,
        max_length=60,
        widget=forms.TextInput(attrs={
            "id": "email",
            "class": "form-control"
        })
    )

    subject = forms.CharField(
        required=True,
        max_length=60,
        widget=forms.TextInput(attrs={
            "id": "email",
            "class": "form-control"
        })
    )

    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            "id": "message",
            "cols": "30",
            "rows": "7",
            "class": "form-control",
            "placeholder": "Write your notes or questions here..."

        })
    )
