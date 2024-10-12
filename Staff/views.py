from django.views.generic import TemplateView
from .models import Staff

class Staff_View(TemplateView):
    template_name = 'Staff List/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Staff'] = Staff.objects.all()
        return context