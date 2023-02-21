from django.http import FileResponse
from django.shortcuts import render
from django.views.generic import FormView

from django_q.tasks import async_task

from .tasks import long_task


from django.forms import ModelForm
from django.views.generic import ListView
from django.views.generic import CreateView

from .models import ScriptInfo, Run


def runs_list(request):
    runs = Run.objects.all()
    context = {
        "runs": runs,
    }
    print(f'{context=}')
    return render(request, "runs_list.html", context)

def download_result(request, run_id):
    run = Run.objects.get(pk=run_id)
    return run.download_result()


# class ScriptInfoCreateView(CreateView):
#     form_class = ScriptInfo
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)


# class ScriptInfoListView(ListView):
#     model = ScriptInfo


# class ScriptInfoView(FormView):
#     form_class = ScriptInfoListView
#     template_name = "contact_form/contact_form.html"
#     success_url = "/"

#     def form_valid(self, form):
#         form.save()
#         self.send_email(form.cleaned_data)

#         return super().form_valid(form)

#     def send_email(self, valid_data):
#         email = valid_data["email"]
#         subject = "Contact form sent from website"
#         message = (
#             f"You have received a contact form.\n"
#             f"Email: {valid_data['email']}\n"
#             f"Name: {valid_data['name']}\n"
#             f"Subject: {valid_data['subject']}\n"
#             f"{valid_data['message']}\n"
#         )
#         async_task(long_task, email, subject, message)
