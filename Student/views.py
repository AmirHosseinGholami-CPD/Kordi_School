from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Student.models import (
    Seven_Student_One, Seven_Student_Two, Eight_Student_One,
    Eight_Student_Two, Nine_Student_One, Nine_Student_Two
)
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

# دیکشنری‌های دروس و نگاشت نام فارسی
SUBJECT_MAPPINGS = {
    'Seven_One': {
        Seven_One_Fizik: 'فیزیک', Seven_One_Shimi: 'شیمی', Seven_One_Zist: 'زیست', Seven_One_Math: 'ریاضی',
        Seven_One_Farsi: 'فارسی', Seven_One_Emla: 'املا', Seven_One_Negaresh: 'نگارش', Seven_One_English: 'انگلیسی',
        Seven_One_Arabic: 'عربی', Seven_One_Quran: 'قرآن', Seven_One_Maref: 'معارف', Seven_One_Kar_Fan: 'کار و فناوری',
        Seven_One_Computer: 'کامپیوتر', Seven_One_Motaleat: 'مطالعات', Seven_One_Tafakor: 'تفکر و پژوهش',
        Seven_One_Farhang_Honar: 'فرهنگ و هنر', Seven_One_Varzesh: 'ورزش'
    },

    'Seven_Two': {
        Seven_Two_Fizik: 'فیزیک', Seven_Two_Shimi: 'شیمی', Seven_Two_Zist: 'زیست', Seven_Two_Math: 'ریاضی',
        Seven_Two_Farsi: 'فارسی', Seven_Two_Emla: 'املا', Seven_Two_Negaresh: 'نگارش', Seven_Two_English: 'انگلیسی',
        Seven_Two_Arabic: 'عربی', Seven_Two_Quran: 'قرآن', Seven_Two_Maref: 'معارف', Seven_Two_Kar_Fan: 'کار و فناوری',
        Seven_Two_Computer: 'کامپیوتر', Seven_Two_Motaleat: 'مطالعات', Seven_Two_Tafakor: 'تفکر و پژوهش',
        Seven_Two_Farhang_Honar: 'فرهنگ و هنر', Seven_Two_Varzesh: 'ورزش'
    },

    'Eight_One': {
        Eight_One_Fizik: 'فیزیک', Eight_One_Shimi: 'شیمی', Eight_One_Zist: 'زیست', Eight_One_Math: 'ریاضی',
        Eight_One_Farsi: 'فارسی', Eight_One_Emla: 'املا', Eight_One_Negaresh: 'نگارش', Eight_One_English: 'انگلیسی',
        Eight_One_Arabic: 'عربی', Eight_One_Quran: 'قرآن', Eight_One_Maref: 'معارف', Eight_One_Kar_Fan: 'کار و فناوری',
        Eight_One_Computer: 'کامپیوتر', Eight_One_Motaleat: 'مطالعات', Eight_One_Tafakor: 'تفکر و پژوهش',
        Eight_One_Farhang_Honar: 'فرهنگ و هنر', Eight_One_Varzesh: 'ورزش'
    },

    'Eight_Two': {
        Eight_Two_Fizik: 'فیزیک', Eight_Two_Shimi: 'شیمی', Eight_Two_Zist: 'زیست', Eight_Two_Math: 'ریاضی',
        Eight_Two_Farsi: 'فارسی', Eight_Two_Emla: 'املا', Eight_Two_Negaresh: 'نگارش', Eight_Two_English: 'انگلیسی',
        Eight_Two_Arabic: 'عربی', Eight_Two_Quran: 'قرآن', Eight_Two_Maref: 'معارف', Eight_Two_Kar_Fan: 'کار و فناوری',
        Eight_Two_Computer: 'کامپیوتر', Eight_Two_Motaleat: 'مطالعات', Eight_Two_Tafakor: 'تفکر و پژوهش',
        Eight_Two_Farhang_Honar: 'فرهنگ و هنر', Eight_Two_Varzesh: 'ورزش'
    },

    'Nine_One': {
        Nine_One_Fizik: 'فیزیک', Nine_One_Shimi: 'شیمی', Nine_One_Zist: 'زیست', Nine_One_Math: 'ریاضی',
        Nine_One_Farsi: 'فارسی', Nine_One_Emla: 'املا', Nine_One_Negaresh: 'نگارش', Nine_One_English: 'انگلیسی',
        Nine_One_Arabic: 'عربی', Nine_One_Quran: 'قرآن', Nine_One_Maref: 'معارف', Nine_One_Kar_Fan: 'کار و فناوری',
        Nine_One_Computer: 'کامپیوتر', Nine_One_Motaleat: 'مطالعات', Nine_One_Amadegi: 'آمادگی دفاعی',
        Nine_One_Farhang_Honar: 'فرهنگ و هنر', Nine_One_Varzesh: 'ورزش'
    },

    'Nine_Two': {
        Nine_Two_Fizik: 'فیزیک', Nine_Two_Shimi: 'شیمی', Nine_Two_Zist: 'زیست', Nine_Two_Math: 'ریاضی',
        Nine_Two_Farsi: 'فارسی', Nine_Two_Emla: 'املا', Nine_Two_Negaresh: 'نگارش', Nine_Two_English: 'انگلیسی',
        Nine_Two_Arabic: 'عربی', Nine_Two_Quran: 'قرآن', Nine_Two_Maref: 'معارف', Nine_Two_Kar_Fan: 'کار و فناوری',
        Nine_Two_Computer: 'کامپیوتر', Nine_Two_Motaleat: 'مطالعات', Nine_Two_Amadegi: 'آمادگی دفاعی',
        Nine_Two_Farhang_Honar: 'فرهنگ و هنر', Nine_Two_Varzesh: 'ورزش'
    },
}

STUDENT_MODEL_MAPPINGS = {
    Seven_Student_One: SUBJECT_MAPPINGS['Seven_One'],
    Seven_Student_Two: SUBJECT_MAPPINGS['Seven_Two'],
    Eight_Student_One: SUBJECT_MAPPINGS['Eight_One'],
    Eight_Student_Two: SUBJECT_MAPPINGS['Eight_Two'],
    Nine_Student_One: SUBJECT_MAPPINGS['Nine_One'],
    Nine_Student_Two: SUBJECT_MAPPINGS['Nine_Two'],
}


@method_decorator(login_required, name='dispatch')
class Student_Score_Mehr(View):

    def get_user_data(self, user):
        # جستجوی اطلاعات دانش‌آموز در مدل‌های مختلف
        for student_model, subjects in STUDENT_MODEL_MAPPINGS.items():
            if student_model.objects.filter(username=user.username).exists():
                student_data = student_model.objects.get(username=user.username)
                return student_data, subjects
        return None, {}

    def get_subject_scores(self, student_name, subject_models):
        # جمع‌آوری نمرات دانش‌آموز از مدل‌های مختلف و فیلتر کردن بر اساس ماه "مهر"
        subject_scores = []
        for model, subject_name in subject_models.items():
            scores = model.objects.filter(name=student_name, month='مهر')
            for score in scores:
                subject_scores.append({
                    'subject': subject_name,  # نام درس به فارسی
                    'name': score.name,
                    'month': score.month,
                    'score': score.score
                })
        return subject_scores

    def get(self, request, *args, **kwargs):
        user = request.user
        student_data, subject_models = self.get_user_data(user)

        if student_data:
            subject_scores = self.get_subject_scores(student_data.name, subject_models)
            
            # آماده‌سازی اطلاعات برای قالب
            context = {
                'user_info': {
                    'name': student_data.name,
                    'photo': student_data.photo.url if student_data.photo else None,
                    'scores': subject_scores
                }
            }
            return render(request, 'Student Page/Score/Mehr.html', context)
        else:
            return render(request, 'user_info.html', {'error': 'کاربر یافت نشد'})






@method_decorator(login_required, name='dispatch')
class Student_Score_Aban(View):

    def get_user_data(self, user):
        # جستجوی اطلاعات دانش‌آموز در مدل‌های مختلف
        for student_model, subjects in STUDENT_MODEL_MAPPINGS.items():
            if student_model.objects.filter(username=user.username).exists():
                student_data = student_model.objects.get(username=user.username)
                return student_data, subjects
        return None, {}

    def get_subject_scores(self, student_name, subject_models):
        # جمع‌آوری نمرات دانش‌آموز از مدل‌های مختلف و فیلتر کردن بر اساس ماه "مهر"
        subject_scores = []
        for model, subject_name in subject_models.items():
            scores = model.objects.filter(name=student_name, month='آبان')
            for score in scores:
                subject_scores.append({
                    'subject': subject_name,  # نام درس به فارسی
                    'name': score.name,
                    'month': score.month,
                    'score': score.score
                })
        return subject_scores

    def get(self, request, *args, **kwargs):
        user = request.user
        student_data, subject_models = self.get_user_data(user)

        if student_data:
            subject_scores = self.get_subject_scores(student_data.name, subject_models)
            
            # آماده‌سازی اطلاعات برای قالب
            context = {
                'user_info': {
                    'name': student_data.name,
                    'photo': student_data.photo.url if student_data.photo else None,
                    'scores': subject_scores
                }
            }
            return render(request, 'Student Page/Score/Aban.html', context)
        else:
            return render(request, 'user_info.html', {'error': 'کاربر یافت نشد'})



@method_decorator(login_required, name='dispatch')
class Student_Score_Azar(View):

    def get_user_data(self, user):
        # جستجوی اطلاعات دانش‌آموز در مدل‌های مختلف
        for student_model, subjects in STUDENT_MODEL_MAPPINGS.items():
            if student_model.objects.filter(username=user.username).exists():
                student_data = student_model.objects.get(username=user.username)
                return student_data, subjects
        return None, {}

    def get_subject_scores(self, student_name, subject_models):
        # جمع‌آوری نمرات دانش‌آموز از مدل‌های مختلف و فیلتر کردن بر اساس ماه "مهر"
        subject_scores = []
        for model, subject_name in subject_models.items():
            scores = model.objects.filter(name=student_name, month='آذر')
            for score in scores:
                subject_scores.append({
                    'subject': subject_name,  # نام درس به فارسی
                    'name': score.name,
                    'month': score.month,
                    'score': score.score
                })
        return subject_scores

    def get(self, request, *args, **kwargs):
        user = request.user
        student_data, subject_models = self.get_user_data(user)

        if student_data:
            subject_scores = self.get_subject_scores(student_data.name, subject_models)
            
            # آماده‌سازی اطلاعات برای قالب
            context = {
                'user_info': {
                    'name': student_data.name,
                    'photo': student_data.photo.url if student_data.photo else None,
                    'scores': subject_scores
                }
            }
            return render(request, 'Student Page/Score/Azar.html', context)
        else:
            return render(request, 'user_info.html', {'error': 'کاربر یافت نشد'})

@method_decorator(login_required, name='dispatch')
class Student_Score_Dey(View):

    def get_user_data(self, user):
        # جستجوی اطلاعات دانش‌آموز در مدل‌های مختلف
        for student_model, subjects in STUDENT_MODEL_MAPPINGS.items():
            if student_model.objects.filter(username=user.username).exists():
                student_data = student_model.objects.get(username=user.username)
                return student_data, subjects
        return None, {}

    def get_subject_scores(self, student_name, subject_models):
        # جمع‌آوری نمرات دانش‌آموز از مدل‌های مختلف و فیلتر کردن بر اساس ماه "مهر"
        subject_scores = []
        for model, subject_name in subject_models.items():
            scores = model.objects.filter(name=student_name, month='دی')
            for score in scores:
                subject_scores.append({
                    'subject': subject_name,  # نام درس به فارسی
                    'name': score.name,
                    'month': score.month,
                    'score': score.score
                })
        return subject_scores

    def get(self, request, *args, **kwargs):
        user = request.user
        student_data, subject_models = self.get_user_data(user)

        if student_data:
            subject_scores = self.get_subject_scores(student_data.name, subject_models)
            
            # آماده‌سازی اطلاعات برای قالب
            context = {
                'user_info': {
                    'name': student_data.name,
                    'photo': student_data.photo.url if student_data.photo else None,
                    'scores': subject_scores
                }
            }
            return render(request, 'Student Page/Score/Dey.html', context)
        else:
            return render(request, 'user_info.html', {'error': 'کاربر یافت نشد'})




@method_decorator(login_required, name='dispatch')
class Student_Score_Bahman(View):

    def get_user_data(self, user):
        # جستجوی اطلاعات دانش‌آموز در مدل‌های مختلف
        for student_model, subjects in STUDENT_MODEL_MAPPINGS.items():
            if student_model.objects.filter(username=user.username).exists():
                student_data = student_model.objects.get(username=user.username)
                return student_data, subjects
        return None, {}

    def get_subject_scores(self, student_name, subject_models):
        # جمع‌آوری نمرات دانش‌آموز از مدل‌های مختلف و فیلتر کردن بر اساس ماه "مهر"
        subject_scores = []
        for model, subject_name in subject_models.items():
            scores = model.objects.filter(name=student_name, month='بهمن')
            for score in scores:
                subject_scores.append({
                    'subject': subject_name,  # نام درس به فارسی
                    'name': score.name,
                    'month': score.month,
                    'score': score.score
                })
        return subject_scores

    def get(self, request, *args, **kwargs):
        user = request.user
        student_data, subject_models = self.get_user_data(user)

        if student_data:
            subject_scores = self.get_subject_scores(student_data.name, subject_models)
            
            # آماده‌سازی اطلاعات برای قالب
            context = {
                'user_info': {
                    'name': student_data.name,
                    'photo': student_data.photo.url if student_data.photo else None,
                    'scores': subject_scores
                }
            }
            return render(request, 'Student Page/Score/Bahman.html', context)
        else:
            return render(request, 'user_info.html', {'error': 'کاربر یافت نشد'})




@method_decorator(login_required, name='dispatch')
class Student_Score_Esfand(View):

    def get_user_data(self, user):
        # جستجوی اطلاعات دانش‌آموز در مدل‌های مختلف
        for student_model, subjects in STUDENT_MODEL_MAPPINGS.items():
            if student_model.objects.filter(username=user.username).exists():
                student_data = student_model.objects.get(username=user.username)
                return student_data, subjects
        return None, {}

    def get_subject_scores(self, student_name, subject_models):
        # جمع‌آوری نمرات دانش‌آموز از مدل‌های مختلف و فیلتر کردن بر اساس ماه "مهر"
        subject_scores = []
        for model, subject_name in subject_models.items():
            scores = model.objects.filter(name=student_name, month='اسفند')
            for score in scores:
                subject_scores.append({
                    'subject': subject_name,  # نام درس به فارسی
                    'name': score.name,
                    'month': score.month,
                    'score': score.score
                })
        return subject_scores

    def get(self, request, *args, **kwargs):
        user = request.user
        student_data, subject_models = self.get_user_data(user)

        if student_data:
            subject_scores = self.get_subject_scores(student_data.name, subject_models)
            
            # آماده‌سازی اطلاعات برای قالب
            context = {
                'user_info': {
                    'name': student_data.name,
                    'photo': student_data.photo.url if student_data.photo else None,
                    'scores': subject_scores
                }
            }
            return render(request, 'Student Page/Score/Esfand.html', context)
        else:
            return render(request, 'user_info.html', {'error': 'کاربر یافت نشد'})





@method_decorator(login_required, name='dispatch')
class Student_Score_Farvardin(View):

    def get_user_data(self, user):
        # جستجوی اطلاعات دانش‌آموز در مدل‌های مختلف
        for student_model, subjects in STUDENT_MODEL_MAPPINGS.items():
            if student_model.objects.filter(username=user.username).exists():
                student_data = student_model.objects.get(username=user.username)
                return student_data, subjects
        return None, {}

    def get_subject_scores(self, student_name, subject_models):
        # جمع‌آوری نمرات دانش‌آموز از مدل‌های مختلف و فیلتر کردن بر اساس ماه "مهر"
        subject_scores = []
        for model, subject_name in subject_models.items():
            scores = model.objects.filter(name=student_name, month='فروردین')
            for score in scores:
                subject_scores.append({
                    'subject': subject_name,  # نام درس به فارسی
                    'name': score.name,
                    'month': score.month,
                    'score': score.score
                })
        return subject_scores

    def get(self, request, *args, **kwargs):
        user = request.user
        student_data, subject_models = self.get_user_data(user)

        if student_data:
            subject_scores = self.get_subject_scores(student_data.name, subject_models)
            
            # آماده‌سازی اطلاعات برای قالب
            context = {
                'user_info': {
                    'name': student_data.name,
                    'photo': student_data.photo.url if student_data.photo else None,
                    'scores': subject_scores
                }
            }
            return render(request, 'Student Page/Score/Farvardin.html', context)
        else:
            return render(request, 'user_info.html', {'error': 'کاربر یافت نشد'})




@method_decorator(login_required, name='dispatch')
class Student_Score_Ordibeheshet(View):

    def get_user_data(self, user):
        # جستجوی اطلاعات دانش‌آموز در مدل‌های مختلف
        for student_model, subjects in STUDENT_MODEL_MAPPINGS.items():
            if student_model.objects.filter(username=user.username).exists():
                student_data = student_model.objects.get(username=user.username)
                return student_data, subjects
        return None, {}

    def get_subject_scores(self, student_name, subject_models):
        # جمع‌آوری نمرات دانش‌آموز از مدل‌های مختلف و فیلتر کردن بر اساس ماه "مهر"
        subject_scores = []
        for model, subject_name in subject_models.items():
            scores = model.objects.filter(name=student_name, month='اردیبهشت')
            for score in scores:
                subject_scores.append({
                    'subject': subject_name,  # نام درس به فارسی
                    'name': score.name,
                    'month': score.month,
                    'score': score.score
                })
        return subject_scores

    def get(self, request, *args, **kwargs):
        user = request.user
        student_data, subject_models = self.get_user_data(user)

        if student_data:
            subject_scores = self.get_subject_scores(student_data.name, subject_models)
            
            # آماده‌سازی اطلاعات برای قالب
            context = {
                'user_info': {
                    'name': student_data.name,
                    'photo': student_data.photo.url if student_data.photo else None,
                    'scores': subject_scores
                }
            }
            return render(request, 'Student Page/Score/Ordibeheshet.html', context)
        else:
            return render(request, 'user_info.html', {'error': 'کاربر یافت نشد'})



@method_decorator(login_required, name='dispatch')
class Student_Score_Khordad(View):

    def get_user_data(self, user):
        # جستجوی اطلاعات دانش‌آموز در مدل‌های مختلف
        for student_model, subjects in STUDENT_MODEL_MAPPINGS.items():
            if student_model.objects.filter(username=user.username).exists():
                student_data = student_model.objects.get(username=user.username)
                return student_data, subjects
        return None, {}

    def get_subject_scores(self, student_name, subject_models):
        # جمع‌آوری نمرات دانش‌آموز از مدل‌های مختلف و فیلتر کردن بر اساس ماه "مهر"
        subject_scores = []
        for model, subject_name in subject_models.items():
            scores = model.objects.filter(name=student_name, month='خرداد')
            for score in scores:
                subject_scores.append({
                    'subject': subject_name,  # نام درس به فارسی
                    'name': score.name,
                    'month': score.month,
                    'score': score.score
                })
        return subject_scores

    def get(self, request, *args, **kwargs):
        user = request.user
        student_data, subject_models = self.get_user_data(user)

        if student_data:
            subject_scores = self.get_subject_scores(student_data.name, subject_models)
            
            # آماده‌سازی اطلاعات برای قالب
            context = {
                'user_info': {
                    'name': student_data.name,
                    'photo': student_data.photo.url if student_data.photo else None,
                    'scores': subject_scores
                }
            }
            return render(request, 'Student Page/Score/Khordad.html', context)
        else:
            return render(request, 'user_info.html', {'error': 'کاربر یافت نشد'})