from django.conf import settings
from django.form.models import ModelForm


class UserForm(ModelForm):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

