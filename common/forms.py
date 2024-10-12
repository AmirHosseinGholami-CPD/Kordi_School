from django import forms
from .models import Common

class Common_Form(forms.ModelForm):
    class Meta:
        model = Common
        fields = ['email',]

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")

        # بررسی اینکه آیا فیلدهای ضروری پر شده‌اند
        if not email:
            raise forms.ValidationError("لطفاً فیلد ضروری مشترک شدن را پر کنید ...")