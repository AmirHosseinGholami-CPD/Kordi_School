from django import forms
from News.models import News
from Staff.models import Staff
from Service.models import Service
from Facilities.models import Facilities
from Student.models import Seven_Student_One, Seven_Student_Two, Eight_Student_One, Eight_Student_Two, Nine_Student_One, Nine_Student_Two
from Teacher.models import Seven_Teacher_One, Seven_Teacher_Two, Eight_Teacher_One, Eight_Teacher_Two, Nine_Teacher_One, Nine_Teacher_Two

class Seven_Student_One_Form(forms.ModelForm):
    class Meta:
        model = Seven_Student_One
        fields = ['name', 'username', 'password', 'father_name', 'father_Phone', 'Mother_Phone', 'born', 'photo']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        father_name = cleaned_data.get("father_name")
        father_phone = cleaned_data.get("father_Phone")
        mother_phone = cleaned_data.get("Mother_Phone")
        born = cleaned_data.get("born")
        photo = cleaned_data.get("photo")

        # بررسی اینکه آیا فیلدهای ضروری پر شده‌اند
        if not name or not username or not password or not father_name or not father_phone or not mother_phone or not born or not photo:
            raise forms.ValidationError("لطفاً تمامی فیلدهای ضروری هفتم یک را پر کنید ...")

class Seven_Student_Two_Form(forms.ModelForm):
    class Meta:
        model = Seven_Student_Two
        fields = ['name', 'username', 'password', 'father_name', 'father_Phone', 'Mother_Phone', 'born', 'photo']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        father_name = cleaned_data.get("father_name")
        father_phone = cleaned_data.get("father_Phone")
        mother_phone = cleaned_data.get("Mother_Phone")
        born = cleaned_data.get("born")
        photo = cleaned_data.get("photo")

        # بررسی اینکه آیا فیلدهای ضروری پر شده‌اند
        if not name or not username or not password or not father_name or not father_phone or not mother_phone or not born or not photo:
            raise forms.ValidationError("لطفاً تمامی فیلدهای ضروری هفتم دو را پر کنید ...")


class Eight_Student_One_Form(forms.ModelForm):
    class Meta:
        model = Eight_Student_One
        fields = ['name', 'username', 'password', 'father_name', 'father_Phone', 'Mother_Phone', 'born', 'photo']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        father_name = cleaned_data.get("father_name")
        father_phone = cleaned_data.get("father_Phone")
        mother_phone = cleaned_data.get("Mother_Phone")
        born = cleaned_data.get("born")
        photo = cleaned_data.get("photo")

        # بررسی اینکه آیا فیلدهای ضروری پر شده‌اند
        if not name or not username or not password or not father_name or not father_phone or not mother_phone or not born or not photo:
            raise forms.ValidationError("لطفاً تمامی فیلدهای ضروری هشتم یک را پر کنید ...")

class Eight_Student_Two_Form(forms.ModelForm):
    class Meta:
        model = Eight_Student_Two
        fields = ['name', 'username', 'password', 'father_name', 'father_Phone', 'Mother_Phone', 'born', 'photo']
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        father_name = cleaned_data.get("father_name")
        father_phone = cleaned_data.get("father_Phone")
        mother_phone = cleaned_data.get("Mother_Phone")
        born = cleaned_data.get("born")
        photo = cleaned_data.get("photo")

        # بررسی اینکه آیا فیلدهای ضروری پر شده‌اند
        if not name or not username or not password or not father_name or not father_phone or not mother_phone or not born or not photo:
            raise forms.ValidationError("لطفاً تمامی فیلدهای ضروری هشتم دو را پر کنید ...")

class Nine_Student_One_Form(forms.ModelForm):
    class Meta:
        model = Nine_Student_One
        fields = ['name', 'username', 'password', 'father_name', 'father_Phone', 'Mother_Phone', 'born', 'photo']
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        father_name = cleaned_data.get("father_name")
        father_phone = cleaned_data.get("father_Phone")
        mother_phone = cleaned_data.get("Mother_Phone")
        born = cleaned_data.get("born")
        photo = cleaned_data.get("photo")

        # بررسی اینکه آیا فیلدهای ضروری پر شده‌اند
        if not name or not username or not password or not father_name or not father_phone or not mother_phone or not born or not photo:
            raise forms.ValidationError("لطفاً تمامی فیلدهای ضروری نهم یک را پر کنید ...")

class Nine_Student_Two_Form(forms.ModelForm):
    class Meta:
        model = Nine_Student_Two
        fields = ['name', 'username', 'password', 'father_name', 'father_Phone', 'Mother_Phone', 'born', 'photo']
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        father_name = cleaned_data.get("father_name")
        father_phone = cleaned_data.get("father_Phone")
        mother_phone = cleaned_data.get("Mother_Phone")
        born = cleaned_data.get("born")
        photo = cleaned_data.get("photo")

        # بررسی اینکه آیا فیلدهای ضروری پر شده‌اند
        if not name or not username or not password or not father_name or not father_phone or not mother_phone or not born or not photo:
            raise forms.ValidationError("لطفاً تمامی فیلدهای ضروری نهم دو را پر کنید ...")



# Teacher:





class Seven_Teacher_One_Form(forms.ModelForm):
    class Meta:
        model = Seven_Teacher_One
        fields = ['name', 'username', 'password', 'course', 'phone_number', 'photo']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        course = cleaned_data.get("course")
        phone_number = cleaned_data.get("phone_number")
        photo = cleaned_data.get("photo")

        # بررسی اینکه آیا فیلدهای ضروری پر شده‌اند
        if not name or not username or not password or not course or not phone_number or not photo:
            raise forms.ValidationError("لطفاً تمامی فیلدهای ضروری هفتم یک را پر کنید ...")


class Seven_Teacher_Two_Form(forms.ModelForm):
    class Meta:
        model = Seven_Teacher_Two
        fields = ['name', 'username', 'password', 'course', 'phone_number', 'photo']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        course = cleaned_data.get("course")
        phone_number = cleaned_data.get("phone_number")
        photo = cleaned_data.get("photo")

        # بررسی اینکه آیا فیلدهای ضروری پر شده‌اند
        if not name or not username or not password or not course or not phone_number or not photo:
            raise forms.ValidationError("لطفاً تمامی فیلدهای ضروری هفتم دو را پر کنید ...")



class Eight_Teacher_One_Form(forms.ModelForm):
    class Meta:
        model = Eight_Teacher_One
        fields = ['name', 'username', 'password', 'course', 'phone_number', 'photo']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        course = cleaned_data.get("course")
        phone_number = cleaned_data.get("phone_number")
        photo = cleaned_data.get("photo")

        # بررسی اینکه آیا فیلدهای ضروری پر شده‌اند
        if not name or not username or not password or not course or not phone_number or not photo:
            raise forms.ValidationError("لطفاً تمامی فیلدهای ضروری هشتم یک را پر کنید ...")



class Eight_Teacher_Two_Form(forms.ModelForm):
    class Meta:
        model = Eight_Teacher_Two
        fields = ['name', 'username', 'password', 'course', 'phone_number', 'photo']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        course = cleaned_data.get("course")
        phone_number = cleaned_data.get("phone_number")
        photo = cleaned_data.get("photo")

        # بررسی اینکه آیا فیلدهای ضروری پر شده‌اند
        if not name or not username or not password or not course or not phone_number or not photo:
            raise forms.ValidationError("لطفاً تمامی فیلدهای ضروری هشتم دو را پر کنید ...")



class Nine_Teacher_One_Form(forms.ModelForm):
    class Meta:
        model = Nine_Teacher_One
        fields = ['name', 'username', 'password', 'course', 'phone_number', 'photo']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        course = cleaned_data.get("course")
        phone_number = cleaned_data.get("phone_number")
        photo = cleaned_data.get("photo")

        # بررسی اینکه آیا فیلدهای ضروری پر شده‌اند
        if not name or not username or not password or not course or not phone_number or not photo:
            raise forms.ValidationError("لطفاً تمامی فیلدهای ضروری نهم یک را پر کنید ...")


class Nine_Teacher_Two_Form(forms.ModelForm):
    class Meta:
        model = Nine_Teacher_Two
        fields = ['name', 'username', 'password', 'course', 'phone_number', 'photo']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        course = cleaned_data.get("course")
        phone_number = cleaned_data.get("phone_number")
        photo = cleaned_data.get("photo")

        # بررسی اینکه آیا فیلدهای ضروری پر شده‌اند
        if not name or not username or not password or not course or not phone_number or not photo:
            raise forms.ValidationError("لطفاً تمامی فیلدهای ضروری نهم دو را پر کنید ...")



class Staff_Form(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'username', 'password', 'staff', 'phone_number', 'photo']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        staff = cleaned_data.get("staff")
        phone_number = cleaned_data.get("phone_number")
        photo = cleaned_data.get("photo")

        # بررسی اینکه آیا فیلدهای ضروری پر شده‌اند
        if not name or not username or not password or not staff or not phone_number or not photo:
            raise forms.ValidationError("لطفاً تمامی فیلدهای کارکنان را پر کنید ...")



class News_Form(forms.ModelForm):
    class Meta:
        model = News
        fields = ['subject', 'description', 'photo']

    def clean(self):
        cleaned_data = super().clean()
        subject = cleaned_data.get("subject")
        description = cleaned_data.get("description")
        photo = cleaned_data.get("photo")

        # بررسی اینکه آیا فیلدهای ضروری پر شده‌اند
        if not subject or not description or not photo:
            raise forms.ValidationError("لطفاً تمامی فیلدهای ضروری  اخبار را پر کنید ...")


class Facilities_Form(forms.ModelForm):
    class Meta:
        model = Facilities
        fields = ['name', 'photo']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        photo = cleaned_data.get("photo")

        # بررسی اینکه آیا فیلدهای ضروری پر شده‌اند
        if not name or not photo:
            raise forms.ValidationError("لطفاً تمامی فیلدهای ضروری  امکانات را پر کنید ...")


class Service_Form(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service_name', 'service_description']

    def clean(self):
        cleaned_data = super().clean()
        service_name = cleaned_data.get("service_name")
        service_description = cleaned_data.get("service_description")

        # بررسی اینکه آیا فیلدهای ضروری پر شده‌اند
        if not service_name or not service_description:
            raise forms.ValidationError("لطفاً تمامی فیلدهای ضروری دوره را پر کنید ...")