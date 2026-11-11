from django.shortcuts import render

from .ai_engine import (
    analyze,
    extract_resume_text,
    recommend_job_roles,
)
from .models import SkillAnalysis


def home(request):

    if request.method == "POST":

        current_skills = request.POST.get(
            "current_skills",
            ""
        )

        target_role = request.POST.get(
            "target_role",
            ""
        )

        job_description = request.POST.get(
            "job_description",
            ""
        )

        resume_file = request.FILES.get(
            "resume"
        )

        # --------------------------------
        # Resume information
        # --------------------------------

        resume_text = ""

        detected_resume_skills = []

        job_recommendations = []

        if resume_file:

            resume_text = extract_resume_text(
                resume_file
            )

            if resume_text:

                career_result = recommend_job_roles(
                    resume_text
                )

                detected_resume_skills = (
                    career_result["resume_skills"]
                )

                job_recommendations = (
                    career_result["recommendations"]
                )

        # --------------------------------
        # Combine manual skills + resume skills
        # --------------------------------

        combined_skills = current_skills

        if detected_resume_skills:

            resume_skill_text = ", ".join(
                detected_resume_skills
            )

            if combined_skills:

                combined_skills += (
                    ", " + resume_skill_text
                )

            else:

                combined_skills = resume_skill_text

        # --------------------------------
        # Existing skill analysis
        # --------------------------------

        result = analyze(
            combined_skills,
            target_role,
            job_description
        )

        # --------------------------------
        # Save analysis
        # --------------------------------

        analysis = SkillAnalysis.objects.create(

            current_skills=combined_skills,

            target_role=target_role,

            job_description=job_description,

            resume=resume_file,

            extracted_resume_text=resume_text,

            detected_resume_skills=", ".join(
                detected_resume_skills
            ),

            matched_skills=", ".join(
                result["matched_skills"]
            ),

            missing_skills=", ".join(
                result["missing_skills"]
            ),

            match_percentage=result[
                "match_percentage"
            ],

            category_scores=result[
                "category_scores"
            ],

            skill_priorities=result[
                "skill_priorities"
            ],

            learning_roadmap=result[
                "learning_roadmap"
            ],

            recommended_projects=result[
                "recommended_projects"
            ],

            interview_topics=result[
                "interview_topics"
            ]
        )

        # --------------------------------
        # Result page
        # --------------------------------

        return render(
            request,
            "analyzer/result.html",
            {
                "analysis": analysis,

                "result": result,

                "job_recommendations":
                    job_recommendations,
            }
        )

    return render(
        request,
        "analyzer/home.html"
    )


def history(request):

    analyses = SkillAnalysis.objects.all().order_by(
        "-created_at"
    )

    return render(
        request,
        "analyzer/history.html",
        {
            "analyses": analyses
        }
    )