from django.forms import ModelForm
from .models import *


class ContactForm(ModelForm):
    class Meta:
        model  = Contact
        fields = '__all__'


class FooterForm(ModelForm):
    class Meta:
        model  = Footer
        fields = '__all__'


class FaqsForm(ModelForm):
    class Meta:
        model  = Faqs
        fields = '__all__'


class CareerForm(ModelForm):
    class Meta:
        model   = Careers
        fields  = '__all__'


class TestimonialsForm(ModelForm):
    class Meta:
        model  = Testimonials
        fields = '__all__'


class TeamsForm(ModelForm):
    class Meta:
        model  = Team
        fields = '__all__'