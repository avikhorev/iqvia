from django.urls import path

from .views import runs_list, download_result

app_name = "script_runner"
urlpatterns = [
    path('', runs_list),
    path('runs/', runs_list),
    path('download_result/<int:run_id>/', download_result),
]