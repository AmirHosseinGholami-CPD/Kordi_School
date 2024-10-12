from django.views.generic import TemplateView
from .forms import Contact_Form
from django.shortcuts import redirect, render

class ContactView(TemplateView):
    template_name = 'Contact Page/Contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        contact = Contact_Form(request.POST, request.FILES)

        if contact.is_valid():
            contact.save()
            return redirect("Contact Page")
        else:
            return self.render_to_response(self.get_context_data(contact=contact))

        return self.render_to_response(self.get_context_data(contact=contact))