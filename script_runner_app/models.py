import os
import time
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.http import FileResponse, HttpResponseNotFound
from django_q.tasks import async_task
from python_on_whales import docker
from python_on_whales.exceptions import DockerException

# class ParamType(models.Model):
# id = models.AutoField(primary_key=True)
#     param_name = models.CharField(max_length=100)
#     allowed_values = models.TextField(null=True)

# class ParamValue(models.Model):
# id = models.AutoField(primary_key=True)
#     param_type = models.ForeignKey(ParamType, on_delete=models.CASCADE)
#     param_value = models.CharField(max_length=100)

class ScriptInfo(models.Model):
    class Meta:
        verbose_name = "Script"
    id = models.AutoField(primary_key=True)
    script_name = models.CharField(max_length=64)
    docker_image = models.CharField(max_length=100)
    output_folder = models.FilePathField(path='RESULTS', allow_files=False, allow_folders=True)
    def __str__(self):
        return self.script_name

class Run(models.Model):
    class Meta:
        verbose_name = "Run"
    id = models.AutoField(primary_key=True)
    script = models.ForeignKey(ScriptInfo, on_delete=models.CASCADE)
    param1 = models.CharField(max_length=100, blank=True, null=True)
    param2 = models.CharField(max_length=100, blank=True, null=True)
    result_file = models.CharField(max_length=256, blank=True, null=True)

    def download_result(self):
        filename = self.result_file
        if filename is None:
            return HttpResponseNotFound()
        else:
            return FileResponse(open(filename, 'rb'))

    # subject = models.CharField(max_length=64)
    # message = models.TextField()
    # created_on = models.DateTimeField(auto_now=True)
    # params = models.ManyToManyField(ParamValue)


def launch_run_async(run):
    out_folder =  os.path.abspath(run.script.output_folder)
    out_file = time.strftime(run.script.script_name + "_%Y%m%d-%H%M%S.xlsx")
    result_file_path =  os.path.join( out_folder, out_file  )
    # try:    
    docker.run(
        run.script.docker_image , [f"/results/{out_file}", run.param1, run.param2],
        volumes=[(out_folder, "/results")],
    )
    run.result_file = result_file_path
    print(f"DONE !!!")
    # send e-mail to user here
    # except DockerException as e:
    #     run.result_file = 'ERROR'
    #     # send e-mail to tech support team
    #     print(f"Exit code {e.return_code} while running {e.docker_command}")
    run.save()

@receiver(post_save, sender=Run)
def launch_run(sender, instance, created, **kwargs):
    if not created: return
    async_task(launch_run_async, instance)