from django.forms import ModelForm

from .models import ScriptInfo


class ContactFormModelForm(ModelForm):
    class Meta:
        model = ScriptInfo
        fields = ["name", "email", "subject", "message"]
