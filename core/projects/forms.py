from django.forms.models import ModelForm
from .models import Projects


class ProjectForm(ModelForm):
    class Meta:
        model  = Projects
        fields = '__all__'