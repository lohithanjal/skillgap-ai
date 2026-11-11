from django.contrib import admin

from .models import SkillAnalysis


@admin.register(SkillAnalysis)
class SkillAnalysisAdmin(admin.ModelAdmin):

    list_display = (
        "target_role",
        "match_percentage",
        "created_at",
    )

    search_fields = (
        "target_role",
        "current_skills",
    )

    ordering = (
        "-created_at",
    )