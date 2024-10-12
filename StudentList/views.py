from django.views.generic import TemplateView
from Student.models import (
    Seven_Student_One, Seven_Student_Two, Eight_Student_One,
    Eight_Student_Two, Nine_Student_One, Nine_Student_Two
)

# Student List View

class Student_Seven_One_List(TemplateView):
    template_name = 'Student List/Seven One.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_seven_one'] = Seven_Student_One.objects.all()
        return context


class Student_Seven_Two_List(TemplateView):
    template_name = 'Student List/Seven Two.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_seven_two'] = Seven_Student_Two.objects.all()
        return context


class Student_Eight_One_List(TemplateView):
    template_name = 'Student List/Eight One.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_eight_one'] = Eight_Student_One.objects.all()
        return context


class Student_Eight_Two_List(TemplateView):
    template_name = 'Student List/Eight Two.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_eight_two'] = Eight_Student_Two.objects.all()
        return context


class Student_Nine_One_List(TemplateView):
    template_name = 'Student List/Nine One.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_nine_one'] = Nine_Student_One.objects.all()
        return context


class Student_Nine_Two_List(TemplateView):
    template_name = 'Student List/Nine Two.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_nine_two'] = Nine_Student_Two.objects.all()
        return context