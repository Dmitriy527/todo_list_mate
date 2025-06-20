from django.contrib import admin
from .models import Tag, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("content",)
    list_filter = ("tags",)


admin.site.register(Tag)
