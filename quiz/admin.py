from django.contrib import admin
from .models import Question

# Register your models here.


# admin.site.register(Category)
# admin.site.register([Question])
from import_export import resources


class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question


from import_export.admin import ImportExportModelAdmin


class QuestionAdmin(ImportExportModelAdmin):
    resource_classes = [QuestionResource]


admin.site.register(Question, QuestionAdmin)
