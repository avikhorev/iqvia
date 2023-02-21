from django.contrib import admin

from .models import ScriptInfo, Run

class ScriptInfoAdmin(admin.ModelAdmin):
    list_display = ("script_name", "docker_image", "output_folder")

class RunAdmin(admin.ModelAdmin):
    list_display = ("get_script_name", "param1", "param2", "result_file")

    @admin.display(description='script_name')
    def get_script_name(self, obj):
        return obj.script.script_name

admin.site.register(ScriptInfo, ScriptInfoAdmin)
admin.site.register(Run, RunAdmin)
