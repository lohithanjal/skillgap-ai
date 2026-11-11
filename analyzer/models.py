from django.db import models


class SkillAnalysis(models.Model):

    # User information
    current_skills = models.TextField()

    target_role = models.CharField(max_length=200)

    job_description = models.TextField()

    # Resume information
    resume = models.FileField(
        upload_to="resumes/",
        blank=True,
        null=True
    )

    extracted_resume_text = models.TextField(
        blank=True,
        null=True
    )

    detected_resume_skills = models.TextField(
        blank=True,
        null=True
    )

    # Skill analysis
    matched_skills = models.TextField(blank=True)

    missing_skills = models.TextField(blank=True)

    partial_skills = models.TextField(blank=True)

    match_percentage = models.FloatField(default=0)

    # Advanced analysis
    category_scores = models.JSONField(default=dict)

    skill_priorities = models.JSONField(default=list)

    learning_roadmap = models.JSONField(default=list)

    recommended_projects = models.JSONField(default=list)

    interview_topics = models.JSONField(default=list)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.target_role