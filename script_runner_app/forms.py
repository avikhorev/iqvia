from django.forms import ModelForm
from django.views.generic import ListView

from .models import ScriptInfo


# class PublisherListView(ListView):
#     model = ScriptInfo

# class ContactFormModelForm(ModelForm):
#     class Meta:
#         model = ScriptInfo
#         fields = ["name", "email", "subject", "message"]
