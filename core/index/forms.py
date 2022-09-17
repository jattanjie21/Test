from django.forms import ModelForm
from .models import *


class SliderForm(ModelForm):
    class Meta:
        model  = Slider
        fields = '__all__'


class WhatWeDoForm(ModelForm):
    class Meta:
        model  = WhatWeDo
        fields = '__all__'


class AboutUsForm(ModelForm):
    class Meta:
        model  = AboutUs
        fields = '__all__'