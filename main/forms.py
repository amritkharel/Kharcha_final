from django.db.models import fields
from .models import Kharcha
from django.forms import ModelForm


class KharchaCreationForm(ModelForm):
    class Meta:
        model = Kharcha
        fields = ['description', 'amount']