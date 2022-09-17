from .models import Inventory

from django.forms import ModelForm


class InventoryForm(ModelForm):
    class Meta:
        model  = Inventory
        fields = '__all__'