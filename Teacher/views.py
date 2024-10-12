from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.views import View
from SevenOneBook.models import (
    Fizik as Seven_One_Fizik, Shimi as Seven_One_Shimi,
    Zist as Seven_One_Zist, Math as Seven_One_Math,
    Farsi as Seven_One_Farsi, Emla as Seven_One_Emla,
    Negaresh as Seven_One_Negaresh, English as Seven_One_English,
    Arabic as Seven_One_Arabic, Quran as Seven_One_Quran,
    Maref as Seven_One_Maref, Kar_Fan as Seven_One_Kar_Fan,
    Computer as Seven_One_Computer, Motaleat as Seven_One_Motaleat,
    Tafakor as Seven_One_Tafakor, Farhang_Honar as Seven_One_Farhang_Honar, 
    Varzesh as Seven_One_Varzesh
)
from SevenTwoBook.models import (
    Fizik as Seven_Two_Fizik, Shimi as Seven_Two_Shimi,
    Zist as Seven_Two_Zist, Math as Seven_Two_Math,
    Farsi as Seven_Two_Farsi, Emla as Seven_Two_Emla,
    Negaresh as Seven_Two_Negaresh, English as Seven_Two_English,
    Arabic as Seven_Two_Arabic, Quran as Seven_Two_Quran,
    Maref as Seven_Two_Maref, Kar_Fan as Seven_Two_Kar_Fan,
    Computer as Seven_Two_Computer, Motaleat as Seven_Two_Motaleat,
    Tafakor as Seven_Two_Tafakor, Farhang_Honar as Seven_Two_Farhang_Honar, 
    Varzesh as Seven_Two_Varzesh
)
from EightOneBook.models import (
    Fizik as Eight_One_Fizik, Shimi as Eight_One_Shimi,
    Zist as Eight_One_Zist, Math as Eight_One_Math,
    Farsi as Eight_One_Farsi, Emla as Eight_One_Emla,
    Negaresh as Eight_One_Negaresh, English as Eight_One_English,
    Arabic as Eight_One_Arabic, Quran as Eight_One_Quran,
    Maref as Eight_One_Maref, Kar_Fan as Eight_One_Kar_Fan,
    Computer as Eight_One_Computer, Motaleat as Eight_One_Motaleat,
    Tafakor as Eight_One_Tafakor, Farhang_Honar as Eight_One_Farhang_Honar, 
    Varzesh as Eight_One_Varzesh
)
from EightTwoBook.models import (
    Fizik as Eight_Two_Fizik, Shimi as Eight_Two_Shimi,
    Zist as Eight_Two_Zist, Math as Eight_Two_Math,
    Farsi as Eight_Two_Farsi, Emla as Eight_Two_Emla,
    Negaresh as Eight_Two_Negaresh, English as Eight_Two_English,
    Arabic as Eight_Two_Arabic, Quran as Eight_Two_Quran,
    Maref as Eight_Two_Maref, Kar_Fan as Eight_Two_Kar_Fan,
    Computer as Eight_Two_Computer, Motaleat as Eight_Two_Motaleat,
    Tafakor as Eight_Two_Tafakor, Farhang_Honar as Eight_Two_Farhang_Honar, 
    Varzesh as Eight_Two_Varzesh
)
from NineOneBook.models import (
    Fizik as Nine_One_Fizik, Shimi as Nine_One_Shimi,
    Zist as Nine_One_Zist, Math as Nine_One_Math,
    Farsi as Nine_One_Farsi, Emla as Nine_One_Emla,
    Negaresh as Nine_One_Negaresh, English as Nine_One_English,
    Arabic as Nine_One_Arabic, Quran as Nine_One_Quran,
    Maref as Nine_One_Maref, Kar_Fan as Nine_One_Kar_Fan,
    Computer as Nine_One_Computer, Motaleat as Nine_One_Motaleat,
    Amadegi as Nine_One_Amadegi, Farhang_Honar as Nine_One_Farhang_Honar, 
    Varzesh as Nine_One_Varzesh
)
from NineTwoBook.models import (
    Fizik as Nine_Two_Fizik, Shimi as Nine_Two_Shimi,
    Zist as Nine_Two_Zist, Math as Nine_Two_Math,
    Farsi as Nine_Two_Farsi, Emla as Nine_Two_Emla,
    Negaresh as Nine_Two_Negaresh, English as Nine_Two_English,
    Arabic as Nine_Two_Arabic, Quran as Nine_Two_Quran,
    Maref as Nine_Two_Maref, Kar_Fan as Nine_Two_Kar_Fan,
    Computer as Nine_Two_Computer, Motaleat as Nine_Two_Motaleat,
    Amadegi as Nine_Two_Amadegi, Farhang_Honar as Nine_Two_Farhang_Honar, 
    Varzesh as Nine_Two_Varzesh
)
from django.http import HttpResponseForbidden
from .models import (
    Seven_Teacher_One, Seven_Teacher_Two, Eight_Teacher_One, 
    Eight_Teacher_Two, Nine_Teacher_One, Nine_Teacher_Two
)
from Student.models import (
    Seven_Student_One, Seven_Student_Two, Eight_Student_One,
    Eight_Student_Two, Nine_Student_One, Nine_Student_Two
)
from absence.models import (
    Seven_One_Absence, Seven_Two_Absence, Eight_One_Absence,
    Eight_Two_Absence, Nine_One_Absence, Nine_Two_Absence
)
import logging

# تنظیمات لاگینگ
logger = logging.getLogger(__name__)
@method_decorator(login_required, name='dispatch')
class UserPanelView(TemplateView):
    template_name = 'Teacher Page/Score.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.user.username
        
        # چاپ نام کاربری معلم در لاگ
        logger.info(f"Requested username: {username}")

        # لیست جداول مدل
        tables = [
            Seven_Teacher_One,
            Seven_Teacher_Two,
            Eight_Teacher_One,
            Eight_Teacher_Two,
            Nine_Teacher_One,
            Nine_Teacher_Two
        ]

        teachers = []
        for table in tables:
            try:
                teacher = table.objects.get(username=username)
                teachers.append(teacher)
            except table.DoesNotExist:
                continue

        if not teachers:
            # اگر معلم پیدا نشد، پیام خطا را نشان می‌دهد
            return render(self.request, 'error.html', {'message': 'Teacher information not available'})

        context['teacher'] = teachers[0]
        context['classes'] = []

        for teacher in teachers:
            if isinstance(teacher, Seven_Teacher_One):
                context['classes'].append('هفتم یک')
            elif isinstance(teacher, Seven_Teacher_Two):
                context['classes'].append('هفتم دو')
            elif isinstance(teacher, Eight_Teacher_One):
                context['classes'].append('هشتم یک')
            elif isinstance(teacher, Eight_Teacher_Two):
                context['classes'].append('هشتم دو')
            elif isinstance(teacher, Nine_Teacher_One):
                context['classes'].append('نهم یک')
            elif isinstance(teacher, Nine_Teacher_Two):
                context['classes'].append('نهم دو')

        selected_class = self.request.POST.get('class')
        if selected_class:
            student_models = {
                'هفتم یک': Seven_Student_One,
                'هفتم دو': Seven_Student_Two,
                'هشتم یک': Eight_Student_One,
                'هشتم دو': Eight_Student_Two,
                'نهم یک': Nine_Student_One,
                'نهم دو': Nine_Student_Two
            }
            
            student_model = student_models.get(selected_class)
            
            if student_model:
                context['students'] = student_model.objects.all()

                 # چک کردن course معلم برای کلاس هفتم دو

                course_model_mapping_seven_one = {
                    'فیزیک': Seven_One_Fizik,
                    'شیمی': Seven_One_Shimi,
                    'زیست': Seven_One_Zist,
                    'ریاضی': Seven_One_Math,
                    'ادبیات': Seven_One_Farsi,
                    'املا': Seven_One_Emla,
                    'نگارش': Seven_One_Negaresh,
                    'انگلیسی': Seven_One_English,
                    'عربی': Seven_One_Arabic,
                    'قرآن': Seven_One_Quran,
                    'معارف': Seven_One_Maref,
                    'کار و فن': Seven_One_Kar_Fan,
                    'رایانه': Seven_One_Computer,
                    'مطالعات': Seven_One_Motaleat,
                    'تفکر': Seven_One_Tafakor,
                    'فرهنگ و هنر': Seven_One_Farhang_Honar,
                    'ورزش': Seven_One_Varzesh,
                }

                if selected_class == 'هفتم یک':
                    course_model = course_model_mapping_seven_one.get(teacher.course)
                    if course_model:
                        context['course_records'] = course_model.objects.all()

                course_model_mapping_seven_two = {
                    'فیزیک': Seven_Two_Fizik,
                    'شیمی': Seven_Two_Shimi,
                    'زیست': Seven_Two_Zist,
                    'ریاضی': Seven_Two_Math,
                    'ادبیات': Seven_Two_Farsi,
                    'املا': Seven_Two_Emla,
                    'نگارش': Seven_Two_Negaresh,
                    'انگلیسی': Seven_Two_English,
                    'عربی': Seven_Two_Arabic,
                    'قرآن': Seven_Two_Quran,
                    'معارف': Seven_Two_Maref,
                    'کار و فن': Seven_Two_Kar_Fan,
                    'رایانه': Seven_Two_Computer,
                    'مطالعات': Seven_Two_Motaleat,
                    'تفکر': Seven_Two_Tafakor,
                    'فرهنگ و هنر': Seven_Two_Farhang_Honar,
                    'ورزش': Seven_Two_Varzesh,
                }

                if selected_class == 'هفتم دو':
                    course_model = course_model_mapping_seven_two.get(teacher.course)
                    if course_model:
                        context['course_records'] = course_model.objects.all()

                course_model_mapping_eight_one = {
                    'فیزیک': Eight_One_Fizik,
                    'شیمی': Eight_One_Shimi,
                    'زیست': Eight_One_Zist,
                    'ریاضی': Eight_One_Math,
                    'ادبیات': Eight_One_Farsi,
                    'املا': Eight_One_Emla,
                    'نگارش': Eight_One_Negaresh,
                    'انگلیسی': Eight_One_English,
                    'عربی': Eight_One_Arabic,
                    'قرآن': Eight_One_Quran,
                    'معارف': Eight_One_Maref,
                    'کار و فن': Eight_One_Kar_Fan,
                    'رایانه': Eight_One_Computer,
                    'مطالعات': Eight_One_Motaleat,
                    'تفکر': Eight_One_Tafakor,
                    'فرهنگ و هنر': Eight_One_Farhang_Honar,
                    'ورزش': Eight_One_Varzesh,
                }

                if selected_class == 'هشتم یک':
                    course_model = course_model_mapping_eight_one.get(teacher.course)
                    if course_model:
                        context['course_records'] = course_model.objects.all()

                course_model_mapping_eight_two = {
                    'فیزیک': Eight_Two_Fizik,
                    'شیمی': Eight_Two_Shimi,
                    'زیست': Eight_Two_Zist,
                    'ریاضی': Eight_Two_Math,
                    'ادبیات': Eight_Two_Farsi,
                    'املا': Eight_Two_Emla,
                    'نگارش': Eight_Two_Negaresh,
                    'انگلیسی': Eight_Two_English,
                    'عربی': Eight_Two_Arabic,
                    'قرآن': Eight_Two_Quran,
                    'معارف': Eight_Two_Maref,
                    'کار و فن': Eight_Two_Kar_Fan,
                    'رایانه': Eight_Two_Computer,
                    'مطالعات': Eight_Two_Motaleat,
                    'تفکر': Eight_Two_Tafakor,
                    'فرهنگ و هنر': Eight_Two_Farhang_Honar,
                    'ورزش': Eight_Two_Varzesh,
                }

                if selected_class == 'هشتم دو':
                    course_model = course_model_mapping_eight_two.get(teacher.course)
                    if course_model:
                        context['course_records'] = course_model.objects.all()

                course_model_mapping_nine_one = {
                    'فیزیک': Nine_One_Fizik,
                    'شیمی': Nine_One_Shimi,
                    'زیست': Nine_One_Zist,
                    'ریاضی': Nine_One_Math,
                    'ادبیات': Nine_One_Farsi,
                    'املا': Nine_One_Emla,
                    'نگارش': Nine_One_Negaresh,
                    'انگلیسی': Nine_One_English,
                    'عربی': Nine_One_Arabic,
                    'قرآن': Nine_One_Quran,
                    'معارف': Nine_One_Maref,
                    'کار و فن': Nine_One_Kar_Fan,
                    'رایانه': Nine_One_Computer,
                    'مطالعات': Nine_One_Motaleat,
                    'آمادگی': Nine_One_Amadegi,
                    'فرهنگ و هنر': Nine_One_Farhang_Honar,
                    'ورزش': Nine_One_Varzesh,
                }

                if selected_class == 'نهم یک':
                    course_model = course_model_mapping_nine_one.get(teacher.course)
                    if course_model:
                        context['course_records'] = course_model.objects.all()

                course_model_mapping_nine_two = {
                    'فیزیک': Nine_Two_Fizik,
                    'شیمی': Nine_Two_Shimi,
                    'زیست': Nine_Two_Zist,
                    'ریاضی': Nine_Two_Math,
                    'ادبیات': Nine_Two_Farsi,
                    'املا': Nine_Two_Emla,
                    'نگارش': Nine_Two_Negaresh,
                    'انگلیسی': Nine_Two_English,
                    'عربی': Nine_Two_Arabic,
                    'قرآن': Nine_Two_Quran,
                    'معارف': Nine_Two_Maref,
                    'کار و فن': Nine_Two_Kar_Fan,
                    'رایانه': Nine_Two_Computer,
                    'مطالعات': Nine_Two_Motaleat,
                    'آمادگی': Nine_Two_Amadegi,
                    'فرهنگ و هنر': Nine_Two_Farhang_Honar,
                    'ورزش': Nine_Two_Varzesh,
                }

                if selected_class == 'نهم دو':
                    course_model = course_model_mapping_nine_two.get(teacher.course)
                    if course_model:
                        context['course_records'] = course_model.objects.all()

            else:
                context['students'] = []
        else:
            context['students'] = []

        logger.debug(f"Selected class: {selected_class}")
        context['selected_class'] = self.request.POST.get('class', '')
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        # دریافت اطلاعات فرم
        selected_class = request.POST.get('class')
        selected_student_name = request.POST.get('student')
        selected_month = request.POST.get('month')
        score = request.POST.get('score')

        if selected_class and selected_student_name and selected_month and score:
            # انتخاب مدل دانش‌آموز بر اساس کلاس انتخابی
            student_models = {
                'هفتم یک': Seven_Student_One,
                'هفتم دو': Seven_Student_Two,
                'هشتم یک': Eight_Student_One,
                'هشتم دو': Eight_Student_Two,
                'نهم یک': Nine_Student_One,
                'نهم دو': Nine_Student_Two
            }
            student_model = student_models.get(selected_class)
            student = student_model.objects.filter(name=selected_student_name).first() if student_model else None

            if student:
                # انتخاب مدل معلم بر اساس نام کاربری کاربر وارد شده
                teacher = None
                teacher_models = [
                    Seven_Teacher_One,
                    Seven_Teacher_Two,
                    Eight_Teacher_One,
                    Eight_Teacher_Two,
                    Nine_Teacher_One,
                    Nine_Teacher_Two
                ]
                for model in teacher_models:
                    try:
                        teacher = model.objects.get(username=request.user.username)
                        break
                    except model.DoesNotExist:
                        continue

                if teacher:
                    # ذخیره اطلاعات بر اساس course معلم
                    if selected_class in ['هفتم یک']:
                        if teacher.course == 'فیزیک':
                            Seven_One_Fizik.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'شیمی':
                            Seven_One_Shimi.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'زیست':
                            Seven_One_Zist.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'ریاضی':
                            Seven_One_Math.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'ادبیات':
                            Seven_One_Farsi.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'املا':
                            Seven_One_Emla.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'نگارش':
                            Seven_One_Negaresh.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'انگلیسی':
                            Seven_One_English.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'عربی':
                            Seven_One_Arabic.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'قرآن':
                            Seven_One_Quran.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'معارف':
                            Seven_One_Maref.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'کار و فن':
                            Seven_One_Kar_Fan.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'رایانه':
                            Seven_One_Computer.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'مطالعات':
                            Seven_One_Motaleat.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'تفکر':
                            Seven_One_Tafakor.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'فرهنگ و هنر':
                            Seven_One_Farhang_Honar.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'ورزش':
                            Seven_One_Varzesh.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )








                    if selected_class in ['هفتم دو']:
                        if teacher.course == 'فیزیک':
                            Seven_Two_Fizik.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'شیمی':
                            Seven_Two_Shimi.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'زیست':
                            Seven_Two_Zist.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'ریاضی':
                            Seven_Two_Math.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'ادبیات':
                            Seven_Two_Farsi.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'املا':
                            Seven_Two_Emla.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'نگارش':
                            Seven_Two_Negaresh.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'انگلیسی':
                            Seven_Two_English.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'عربی':
                            Seven_Two_Arabic.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'قرآن':
                            Seven_Two_Quran.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'معارف':
                            Seven_Two_Maref.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'کار و فن':
                            Seven_Two_Kar_Fan.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'رایانه':
                            Seven_Two_Computer.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'مطالعات':
                            Seven_Two_Motaleat.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'تفکر':
                            Seven_Two_Tafakor.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'فرهنگ و هنر':
                            Seven_Two_Farhang_Honar.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'ورزش':
                            Seven_Two_Varzesh.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )










                    if selected_class in ['هشتم یک']:
                        if teacher.course == 'فیزیک':
                            Eight_One_Fizik.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'شیمی':
                            Eight_One_Shimi.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'زیست':
                            Eight_One_Zist.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'ریاضی':
                            Eight_One_Math.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'ادبیات':
                            Eight_One_Farsi.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'املا':
                            Eight_One_Emla.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'نگارش':
                            Eight_One_Negaresh.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'انگلیسی':
                            Eight_One_English.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'عربی':
                            Eight_One_Arabic.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'قرآن':
                            Eight_One_Quran.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'معارف':
                            Eight_One_Maref.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'کار و فن':
                            Eight_One_Kar_Fan.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'رایانه':
                            Eight_One_Computer.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'مطالعات':
                            Eight_One_Motaleat.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'تفکر':
                            Eight_One_Tafakor.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'فرهنگ و هنر':
                            Eight_One_Farhang_Honar.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'ورزش':
                            Eight_One_Varzesh.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )


                    



                    if selected_class in ['هشتم دو']:
                        if teacher.course == 'فیزیک':
                            Eight_Two_Fizik.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'شیمی':
                            Eight_Two_Shimi.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'زیست':
                            Eight_Two_Zist.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'ریاضی':
                            Eight_Two_Math.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'ادبیات':
                            Eight_Two_Farsi.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'املا':
                            Eight_Two_Emla.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'نگارش':
                            Eight_Two_Negaresh.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'انگلیسی':
                            Eight_Two_English.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'عربی':
                            Eight_Two_Arabic.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'قرآن':
                            Eight_Two_Quran.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'معارف':
                            Eight_Two_Maref.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'کار و فن':
                            Eight_Two_Kar_Fan.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'رایانه':
                            Eight_Two_Computer.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'مطالعات':
                            Eight_Two_Motaleat.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'تفکر':
                            Eight_Two_Tafakor.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'فرهنگ و هنر':
                            Eight_Two_Farhang_Honar.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'ورزش':
                            Eight_Two_Varzesh.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )




                    if selected_class in ['نهم یک']:
                        if teacher.course == 'فیزیک':
                            Nine_One_Fizik.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'شیمی':
                            Nine_One_Shimi.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'زیست':
                            Nine_One_Zist.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'ریاضی':
                            Nine_One_Math.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'ادبیات':
                            Nine_One_Farsi.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'املا':
                            Nine_One_Emla.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'نگارش':
                            Nine_One_Negaresh.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'انگلیسی':
                            Nine_One_English.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'عربی':
                            Nine_One_Arabic.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'قرآن':
                            Nine_One_Quran.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'معارف':
                            Nine_One_Maref.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'کار و فن':
                            Nine_One_Kar_Fan.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'رایانه':
                            Nine_One_Computer.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'مطالعات':
                            Nine_One_Motaleat.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'آمادگی':
                            Nine_One_Amadegi.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'فرهنگ و هنر':
                            Nine_One_Farhang_Honar.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'ورزش':
                            Nine_One_Varzesh.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )




                    

                    if selected_class in ['نهم دو']:
                        if teacher.course == 'فیزیک':
                            Nine_Two_Fizik.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'شیمی':
                            Nine_Two_Shimi.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'زیست':
                            Nine_Two_Zist.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'ریاضی':
                            Nine_Two_Math.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'ادبیات':
                            Nine_Two_Farsi.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'املا':
                            Nine_Two_Emla.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'نگارش':
                            Nine_Two_Negaresh.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'انگلیسی':
                            Nine_Two_English.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'عربی':
                            Nine_Two_Arabic.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'قرآن':
                            Nine_Two_Quran.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'معارف':
                            Nine_Two_Maref.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'کار و فن':
                            Nine_Two_Kar_Fan.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'رایانه':
                            Nine_Two_Computer.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'مطالعات':
                            Nine_Two_Motaleat.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'آمادگی':
                            Nine_Two_Amadegi.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'فرهنگ و هنر':
                            Nine_Two_Farhang_Honar.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )
                        elif teacher.course == 'ورزش':
                            Nine_Two_Varzesh.objects.create(
                                name=student.name,
                                month=selected_month,
                                score=score
                            )


                    return render(request, self.template_name, context)

        # اگر داده‌های فرم معتبر نباشند یا مشکلی پیش بیاید
        return render(request, self.template_name, context)


class DeleteStudentView(View):
    # دیکشنری که مدل‌ها را برای هر کلاس و درس نگه می‌دارد
    class_dict = {
        'هفتم یک': {
            'فیزیک': Seven_One_Fizik,
            'شیمی': Seven_One_Shimi,
            'زیست': Seven_One_Zist,
            'ریاضی': Seven_One_Math,
            'ادبیات': Seven_One_Farsi,
            'املا': Seven_One_Emla,
            'نگارش': Seven_One_Negaresh,
            'انگلیسی': Seven_One_English,
            'عربی': Seven_One_Arabic,
            'قرآن': Seven_One_Quran,
            'معارف': Seven_One_Maref,
            'کار و فن': Seven_One_Kar_Fan,
            'رایانه': Seven_One_Computer,
            'مطالعات': Seven_One_Motaleat,
            'تفکر': Seven_One_Tafakor,
            'فرهنگ و هنر': Seven_One_Farhang_Honar,
            'ورزش': Seven_One_Varzesh,
        },
        'هفتم دو': {
            'فیزیک': Seven_Two_Fizik,
            'شیمی': Seven_Two_Shimi,
            'زیست': Seven_Two_Zist,
            'ریاضی': Seven_Two_Math,
            'ادبیات': Seven_Two_Farsi,
            'املا': Seven_Two_Emla,
            'نگارش': Seven_Two_Negaresh,
            'انگلیسی': Seven_Two_English,
            'عربی': Seven_Two_Arabic,
            'قرآن': Seven_Two_Quran,
            'معارف': Seven_Two_Maref,
            'کار و فن': Seven_Two_Kar_Fan,
            'رایانه': Seven_Two_Computer,
            'مطالعات': Seven_Two_Motaleat,
            'تفکر': Seven_Two_Tafakor,
            'فرهنگ و هنر': Seven_Two_Farhang_Honar,
            'ورزش': Seven_Two_Varzesh,
        },
        'هشتم یک': {
            'فیزیک': Eight_One_Fizik,
            'شیمی': Eight_One_Shimi,
            'زیست': Eight_One_Zist,
            'ریاضی': Eight_One_Math,
            'ادبیات': Eight_One_Farsi,
            'املا': Eight_One_Emla,
            'نگارش': Eight_One_Negaresh,
            'انگلیسی': Eight_One_English,
            'عربی': Eight_One_Arabic,
            'قرآن': Eight_One_Quran,
            'معارف': Eight_One_Maref,
            'کار و فن': Eight_One_Kar_Fan,
            'رایانه': Eight_One_Computer,
            'مطالعات': Eight_One_Motaleat,
            'تفکر': Eight_One_Tafakor,
            'فرهنگ و هنر': Eight_One_Farhang_Honar,
            'ورزش': Eight_One_Varzesh,
        },
        'هشتم دو': {
            'فیزیک': Eight_Two_Fizik,
            'شیمی': Eight_Two_Shimi,
            'زیست': Eight_Two_Zist,
            'ریاضی': Eight_Two_Math,
            'ادبیات': Eight_Two_Farsi,
            'املا': Eight_Two_Emla,
            'نگارش': Eight_Two_Negaresh,
            'انگلیسی': Eight_Two_English,
            'عربی': Eight_Two_Arabic,
            'قرآن': Eight_Two_Quran,
            'معارف': Eight_Two_Maref,
            'کار و فن': Eight_Two_Kar_Fan,
            'رایانه': Eight_Two_Computer,
            'مطالعات': Eight_Two_Motaleat,
            'تفکر': Eight_Two_Tafakor,
            'فرهنگ و هنر': Eight_Two_Farhang_Honar,
            'ورزش': Eight_Two_Varzesh,
        },
        'نهم یک': {
            'فیزیک': Nine_One_Fizik,
            'شیمی': Nine_One_Shimi,
            'زیست': Nine_One_Zist,
            'ریاضی': Nine_One_Math,
            'ادبیات': Nine_One_Farsi,
            'املا': Nine_One_Emla,
            'نگارش': Nine_One_Negaresh,
            'انگلیسی': Nine_One_English,
            'عربی': Nine_One_Arabic,
            'قرآن': Nine_One_Quran,
            'معارف': Nine_One_Maref,
            'کار و فن': Nine_One_Kar_Fan,
            'رایانه': Nine_One_Computer,
            'مطالعات': Nine_One_Motaleat,
            'آمادگی': Nine_One_Amadegi,
            'فرهنگ و هنر': Nine_One_Farhang_Honar,
            'ورزش': Nine_One_Varzesh,
        },
        'نهم دو': {
            'فیزیک': Nine_Two_Fizik,
            'شیمی': Nine_Two_Shimi,
            'زیست': Nine_Two_Zist,
            'ریاضی': Nine_Two_Math,
            'ادبیات': Nine_Two_Farsi,
            'املا': Nine_Two_Emla,
            'نگارش': Nine_Two_Negaresh,
            'انگلیسی': Nine_Two_English,
            'عربی': Nine_Two_Arabic,
            'قرآن': Nine_Two_Quran,
            'معارف': Nine_Two_Maref,
            'کار و فن': Nine_Two_Kar_Fan,
            'رایانه': Nine_Two_Computer,
            'مطالعات': Nine_Two_Motaleat,
            'آمادگی': Nine_Two_Amadegi,
            'فرهنگ و هنر': Nine_Two_Farhang_Honar,
            'ورزش': Nine_Two_Varzesh,
        },
        
        # می‌توانید همینطور برای کلاس‌های دیگر نیز دیکشنری اضافه کنید
    }

    def post(self, request, student_id, selected_class):
        teacher = None
        teacher_models = [
            Seven_Teacher_One,
            Seven_Teacher_Two,
            Eight_Teacher_One,
            Eight_Teacher_Two,
            Nine_Teacher_One,
            Nine_Teacher_Two
        ]
        for model in teacher_models:
            try:
                teacher = model.objects.get(username=request.user.username)
                break
            except model.DoesNotExist:
                continue

        if not teacher:
            return redirect('teacher')

        # پیدا کردن مدل مناسب بر اساس selected_class و course
        model_class = self.class_dict.get(selected_class, {}).get(teacher.course)
        if model_class:
            record = get_object_or_404(model_class, id=student_id)
            record.delete()
            return redirect('teacher')  # آدرس موفقیت یا صفحه دیگری که می‌خواهید بعد از حذف نشان داده شود

        return redirect('error_page')  # آدرس صفحه خطا



@method_decorator(login_required, name='dispatch')
class UserPanelAbsenceView(TemplateView): 
    template_name = 'Teacher Page/absence.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.user.username
        
        # چاپ نام کاربری معلم در لاگ
        logger.info(f"Requested username: {username}")

        # لیست جداول مدل
        tables = [
            Seven_Teacher_One,
            Seven_Teacher_Two,
            Eight_Teacher_One,
            Eight_Teacher_Two,
            Nine_Teacher_One,
            Nine_Teacher_Two
        ]

        teachers = []
        for table in tables:
            try:
                teacher = table.objects.get(username=username)
                teachers.append(teacher)
            except table.DoesNotExist:
                continue

        if not teachers:
            # اگر معلم پیدا نشد، پیام خطا را نشان می‌دهد
            return render(self.request, 'error.html', {'message': 'Teacher information not available'})

        context['teacher'] = teachers[0]
        context['classes'] = []

        for teacher in teachers:
            if isinstance(teacher, Seven_Teacher_One):
                context['classes'].append('هفتم یک')
            elif isinstance(teacher, Seven_Teacher_Two):
                context['classes'].append('هفتم دو')
            elif isinstance(teacher, Eight_Teacher_One):
                context['classes'].append('هشتم یک')
            elif isinstance(teacher, Eight_Teacher_Two):
                context['classes'].append('هشتم دو')
            elif isinstance(teacher, Nine_Teacher_One):
                context['classes'].append('نهم یک')
            elif isinstance(teacher, Nine_Teacher_Two):
                context['classes'].append('نهم دو')

        selected_class = self.request.POST.get('class')
        if selected_class:
            student_models = {
                'هفتم یک': Seven_Student_One,
                'هفتم دو': Seven_Student_Two,
                'هشتم یک': Eight_Student_One,
                'هشتم دو': Eight_Student_Two,
                'نهم یک': Nine_Student_One,
                'نهم دو': Nine_Student_Two
            }
            
            student_model = student_models.get(selected_class)
            
            if student_model:
                context['students'] = student_model.objects.all()

                 # چک کردن course معلم برای کلاس هفتم دو
                if selected_class == 'هفتم یک':
                    context['course_records'] = Seven_One_Absence.objects.all()

                if selected_class == 'هفتم دو':
                    context['course_records'] = Seven_Two_Absence.objects.all()

                if selected_class == 'هشتم یک':
                    context['course_records'] = Eight_One_Absence.objects.all()
                    
                if selected_class == 'هشتم دو':
                    context['course_records'] = Eight_Two_Absence.objects.all()

                if selected_class == 'نهم یک':
                    context['course_records'] = Nine_One_Absence.objects.all()
                    
                if selected_class == 'نهم دو':
                    context['course_records'] = Nine_Two_Absence.objects.all()
            else:
                context['students'] = []
        else:
            context['students'] = []

        logger.debug(f"Selected class: {selected_class}")
        context['selected_class'] = self.request.POST.get('class', '')
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        # دریافت اطلاعات فرم
        selected_class = request.POST.get('class')
        selected_student_name = request.POST.get('student')
        selected_day = request.POST.get('day')

        if selected_class and selected_student_name and selected_day:
            # انتخاب مدل دانش‌آموز بر اساس کلاس انتخابی
            student_models = {
                'هفتم یک': Seven_Student_One,
                'هفتم دو': Seven_Student_Two,
                'هشتم یک': Eight_Student_One,
                'هشتم دو': Eight_Student_Two,
                'نهم یک': Nine_Student_One,
                'نهم دو': Nine_Student_Two
            }
            student_model = student_models.get(selected_class)
            student = student_model.objects.filter(name=selected_student_name).first() if student_model else None

            if student:
                # انتخاب مدل معلم بر اساس نام کاربری کاربر وارد شده
                teacher = None
                teacher_models = [
                    Seven_Teacher_One,
                    Seven_Teacher_Two,
                    Eight_Teacher_One,
                    Eight_Teacher_Two,
                    Nine_Teacher_One,
                    Nine_Teacher_Two
                ]
                for model in teacher_models:
                    try:
                        teacher = model.objects.get(username=request.user.username)
                        break
                    except model.DoesNotExist:
                        continue

                if teacher:
                    # ذخیره اطلاعات بر اساس course معلم
                    if selected_class in ['هفتم یک']:
                        Seven_One_Absence.objects.create(
                            name=student.name,
                            day=selected_day,
                            lessone=teacher.course
                        )
                    if selected_class in ['هفتم دو']:
                        Seven_Two_Absence.objects.create(
                            name=student.name,
                            day=selected_day,
                            lessone=teacher.course
                        )
                    if selected_class in ['هشتم یک']:
                        Eight_One_Absence.objects.create(
                            name=student.name,
                            day=selected_day,
                            lessone=teacher.course
                        )
                    if selected_class in ['هشتم دو']:
                        Eight_Two_Absence.objects.create(
                            name=student.name,
                            day=selected_day,
                            lessone=teacher.course
                        )
                    if selected_class in ['نهم یک']:
                        Nine_One_Absence.objects.create(
                            name=student.name,
                            day=selected_day,
                            lessone=teacher.course
                        )
                    if selected_class in ['نهم دو']:
                        Nine_Two_Absence.objects.create(
                            name=student.name,
                            day=selected_day,
                            lessone=teacher.course
                        )


                    return render(request, self.template_name, context)

        # اگر داده‌های فرم معتبر نباشند یا مشکلی پیش بیاید
        return render(request, self.template_name, context)


class DeleteStudentAbsenceView(View):
    def post(self, request, student_id, selected_class):
        # پیدا کردن معلم با توجه به نام کاربری
        teacher = None
        teacher_models = [
            Seven_Teacher_One,
            Seven_Teacher_Two,
            Eight_Teacher_One,
            Eight_Teacher_Two,
            Nine_Teacher_One,
            Nine_Teacher_Two
        ]
        for model in teacher_models:
            try:
                teacher = model.objects.get(username=request.user.username)
                break
            except model.DoesNotExist:
                continue

        if not teacher:
            # اگر معلم پیدا نشود، می‌توانید یک خطای مناسب برگردانید یا ریدایرکت کنید
            return redirect('teacher_absence')

        # چک کردن کلاس و course معلم
        if selected_class == 'هفتم یک':
             record = get_object_or_404(Seven_One_Absence, id=student_id)
        elif selected_class == 'هفتم دو':
             record = get_object_or_404(Seven_Two_Absence, id=student_id)
        elif selected_class == 'هشتم یک':
             record = get_object_or_404(Eight_One_Absence, id=student_id)
        elif selected_class == 'هشتم دو':
            record = get_object_or_404(Eight_Two_Absence, id=student_id)
        elif selected_class == 'نهم یک':
             record = get_object_or_404(Nine_One_Absence, id=student_id)
        elif selected_class == 'نهم دو':
            record = get_object_or_404(Nine_Two_Absence, id=student_id)
        else:
            # کلاس‌های دیگر را در صورت نیاز اضافه کنید
            return redirect('teacher_absence')

        # حذف رکورد
        record.delete()

        return redirect('teacher_absence')