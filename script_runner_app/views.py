from django.http import FileResponse
from django.shortcuts import render
from django.views.generic import FormView

from django_q.tasks import async_task

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