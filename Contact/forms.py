from django import forms
from .models import Contact

class Contact_Form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'last_name', 'email', 'phone', 'message']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        last_name = cleaned_data.get("last_name")
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")
        message = cleaned_data.get("message")

        # بررسی اینکه آیا فیلدهای ضروری پر شده‌اند
        if not name or not last_name or not email or not phone or not message:
            raise forms.ValidationError("لطفاً تمامی فیلدهای ضروری تماس با ما را پر کنید ...")