from django.contrib import admin
from django.db.models import Avg
from .models import Project, Evaluation

admin.site.register(Evaluation)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'average_score_display')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(avg_score=Avg('evaluation__value'))

    def average_score_display(self, obj):
        return round(obj.avg_score, 2) if obj.avg_score else 0
    average_score_display.short_description = 'Average Score'
    average_score_display.admin_order_field = 'avg_score'