import re

from pypdf import PdfReader

SKILL_CATALOG = {

    # -------------------------
    # PROGRAMMING
    # -------------------------

    "Python": {
        "aliases": ["python", "python3", "python 3"],
        "category": "Programming",
        "weight": 10,
        "level": "Critical",
        "days": 10,
        "project": "Build a Python automation tool",
        "interview": [
            "Python data types",
            "Functions",
            "OOP",
            "Exception handling",
            "Decorators",
            "Generators"
        ]
    },

    "Java": {
        "aliases": ["java"],
        "category": "Programming",
        "weight": 10,
        "level": "Critical",
        "days": 12,
        "project": "Build a Java REST API",
        "interview": [
            "OOP",
            "Collections",
            "Exception handling",
            "Multithreading"
        ]
    },

    "JavaScript": {
        "aliases": ["javascript", "js", "ecmascript"],
        "category": "Frontend",
        "weight": 8,
        "level": "High",
        "days": 10,
        "project": "Build an interactive JavaScript dashboard",
        "interview": [
            "Variables",
            "Functions",
            "DOM",
            "Events",
            "Promises",
            "Async/Await"
        ]
    },

    "C": {
        "aliases": ["c programming", "c language"],
        "category": "Programming",
        "weight": 7,
        "level": "Medium",
        "days": 8,
        "project": "Build a C console application",
        "interview": [
            "Pointers",
            "Arrays",
            "Functions",
            "Structures"
        ]
    },

    "C++": {
        "aliases": ["c++", "cpp"],
        "category": "Programming",
        "weight": 8,
        "level": "High",
        "days": 10,
        "project": "Build an OOP-based C++ application",
        "interview": [
            "OOP",
            "STL",
            "Pointers",
            "Inheritance"
        ]
    },

    # -------------------------
    # FRONTEND
    # -------------------------

    "HTML": {
        "aliases": ["html", "html5"],
        "category": "Frontend",
        "weight": 5,
        "level": "Medium",
        "days": 4,
        "project": "Build a responsive portfolio website",
        "interview": [
            "Semantic HTML",
            "Forms",
            "Tables",
            "Accessibility"
        ]
    },

    "CSS": {
        "aliases": ["css", "css3"],
        "category": "Frontend",
        "weight": 5,
        "level": "Medium",
        "days": 5,
        "project": "Build a responsive dashboard",
        "interview": [
            "Flexbox",
            "Grid",
            "Responsive design",
            "Positioning"
        ]
    },

    "React": {
        "aliases": ["react", "reactjs", "react.js"],
        "category": "Frontend",
        "weight": 8,
        "level": "High",
        "days": 12,
        "project": "Build a React job portal",
        "interview": [
            "Components",
            "Props",
            "State",
            "Hooks",
            "API integration"
        ]
    },

    "Angular": {
        "aliases": ["angular"],
        "category": "Frontend",
        "weight": 8,
        "level": "High",
        "days": 12,
        "project": "Build an Angular admin dashboard",
        "interview": [
            "Components",
            "Services",
            "Routing",
            "Forms"
        ]
    },

    # -------------------------
    # DATABASE
    # -------------------------

    "SQL": {
        "aliases": ["sql", "structured query language"],
        "category": "Database",
        "weight": 9,
        "level": "Critical",
        "days": 8,
        "project": "Build an SQL analytics project",
        "interview": [
            "Joins",
            "Subqueries",
            "GROUP BY",
            "HAVING",
            "Indexes",
            "Normalization"
        ]
    },

    "MySQL": {
        "aliases": ["mysql"],
        "category": "Database",
        "weight": 7,
        "level": "High",
        "days": 6,
        "project": "Build a MySQL-based ecommerce database",
        "interview": [
            "Joins",
            "Indexes",
            "Constraints",
            "Transactions"
        ]
    },

    "PostgreSQL": {
        "aliases": ["postgresql", "postgres"],
        "category": "Database",
        "weight": 7,
        "level": "High",
        "days": 6,
        "project": "Build a PostgreSQL-backed API",
        "interview": [
            "Indexes",
            "Transactions",
            "Constraints"
        ]
    },

    "MongoDB": {
        "aliases": ["mongodb", "mongo"],
        "category": "Database",
        "weight": 7,
        "level": "High",
        "days": 7,
        "project": "Build a MongoDB-based application",
        "interview": [
            "Documents",
            "Collections",
            "Queries",
            "Indexes"
        ]
    },

    # -------------------------
    # BACKEND
    # -------------------------

    "Django": {
        "aliases": ["django"],
        "category": "Backend",
        "weight": 10,
        "level": "Critical",
        "days": 10,
        "project": "Build a Django job portal",
        "interview": [
            "MVT architecture",
            "Models",
            "ORM",
            "Views",
            "URLs",
            "Forms",
            "Authentication"
        ]
    },

    "Flask": {
        "aliases": ["flask"],
        "category": "Backend",
        "weight": 7,
        "level": "High",
        "days": 7,
        "project": "Build a Flask REST API",
        "interview": [
            "Routes",
            "Blueprints",
            "REST APIs",
            "Authentication"
        ]
    },

    "FastAPI": {
        "aliases": ["fastapi", "fast api"],
        "category": "Backend",
        "weight": 8,
        "level": "High",
        "days": 7,
        "project": "Build a FastAPI backend",
        "interview": [
            "Routes",
            "Pydantic",
            "Dependency injection",
            "Authentication"
        ]
    },

    "REST API": {
        "aliases": [
            "rest api",
            "rest apis",
            "restful api",
            "restful apis",
            "rest service"
        ],
        "category": "Backend",
        "weight": 8,
        "level": "High",
        "days": 6,
        "project": "Build a REST API for an ecommerce system",
        "interview": [
            "HTTP methods",
            "Status codes",
            "JSON",
            "Authentication",
            "CRUD"
        ]
    },

    # -------------------------
    # VERSION CONTROL
    # -------------------------

    "Git": {
        "aliases": ["git"],
        "category": "Tools",
        "weight": 6,
        "level": "High",
        "days": 4,
        "project": "Manage a project using Git workflow",
        "interview": [
            "Commit",
            "Branch",
            "Merge",
            "Rebase",
            "Pull request"
        ]
    },

    "GitHub": {
        "aliases": ["github", "git hub"],
        "category": "Tools",
        "weight": 5,
        "level": "Medium",
        "days": 3,
        "project": "Create and maintain a professional GitHub portfolio",
        "interview": [
            "Repositories",
            "Branches",
            "Pull requests",
            "Issues"
        ]
    },

    # -------------------------
    # CLOUD / DEVOPS
    # -------------------------

    "Docker": {
        "aliases": ["docker", "docker containers", "containerization"],
        "category": "DevOps",
        "weight": 8,
        "level": "High",
        "days": 7,
        "project": "Dockerize a Django application",
        "interview": [
            "Images",
            "Containers",
            "Dockerfile",
            "Volumes",
            "Networks"
        ]
    },

    "Kubernetes": {
        "aliases": ["kubernetes", "k8s"],
        "category": "DevOps",
        "weight": 8,
        "level": "High",
        "days": 10,
        "project": "Deploy a containerized application on Kubernetes",
        "interview": [
            "Pods",
            "Deployments",
            "Services",
            "ConfigMaps"
        ]
    },

    "AWS": {
        "aliases": ["aws", "amazon web services"],
        "category": "Cloud",
        "weight": 8,
        "level": "High",
        "days": 10,
        "project": "Deploy a Django application on AWS",
        "interview": [
            "EC2",
            "S3",
            "IAM",
            "RDS"
        ]
    },

    "Azure": {
        "aliases": ["azure", "microsoft azure"],
        "category": "Cloud",
        "weight": 8,
        "level": "High",
        "days": 10,
        "project": "Deploy a web application on Azure",
        "interview": [
            "Virtual machines",
            "Storage",
            "IAM",
            "Databases"
        ]
    },

    "Linux": {
        "aliases": ["linux", "ubuntu", "unix"],
        "category": "DevOps",
        "weight": 6,
        "level": "Medium",
        "days": 5,
        "project": "Deploy a Linux-based web server",
        "interview": [
            "Commands",
            "Permissions",
            "Processes",
            "Networking"
        ]
    },

    # -------------------------
    # DATA / AI
    # -------------------------

    "Pandas": {
        "aliases": ["pandas"],
        "category": "Data",
        "weight": 7,
        "level": "High",
        "days": 6,
        "project": "Build a data analysis dashboard",
        "interview": [
            "DataFrame",
            "Series",
            "Filtering",
            "GroupBy"
        ]
    },

    "NumPy": {
        "aliases": ["numpy", "num py"],
        "category": "Data",
        "weight": 6,
        "level": "Medium",
        "days": 5,
        "project": "Build a numerical data analysis project",
        "interview": [
            "Arrays",
            "Indexing",
            "Broadcasting"
        ]
    },

    "Machine Learning": {
        "aliases": [
            "machine learning",
            "machine-learning",
            "ml"
        ],
        "category": "AI/ML",
        "weight": 10,
        "level": "Critical",
        "days": 15,
        "project": "Build a machine learning prediction system",
        "interview": [
            "Supervised learning",
            "Unsupervised learning",
            "Regression",
            "Classification",
            "Model evaluation"
        ]
    },

    "Deep Learning": {
        "aliases": [
            "deep learning",
            "deep-learning",
            "dl"
        ],
        "category": "AI/ML",
        "weight": 9,
        "level": "High",
        "days": 15,
        "project": "Build an image classification system",
        "interview": [
            "Neural networks",
            "CNN",
            "RNN",
            "Backpropagation"
        ]
    },

    "TensorFlow": {
        "aliases": ["tensorflow", "tensor flow"],
        "category": "AI/ML",
        "weight": 8,
        "level": "High",
        "days": 10,
        "project": "Build and train an image classifier",
        "interview": [
            "Models",
            "Layers",
            "Training",
            "Evaluation"
        ]
    },

    "PyTorch": {
        "aliases": ["pytorch", "py torch"],
        "category": "AI/ML",
        "weight": 8,
        "level": "High",
        "days": 10,
        "project": "Build a neural network using PyTorch",
        "interview": [
            "Tensors",
            "Models",
            "Training",
            "Autograd"
        ]
    },

    "Scikit-learn": {
        "aliases": [
            "scikit-learn",
            "scikit learn",
            "sklearn"
        ],
        "category": "AI/ML",
        "weight": 8,
        "level": "High",
        "days": 8,
        "project": "Build a classification system",
        "interview": [
            "Preprocessing",
            "Train-test split",
            "Classification",
            "Metrics"
        ]
    },

    # -------------------------
    # CS FUNDAMENTALS
    # -------------------------

    "Data Structures": {
        "aliases": [
            "data structures",
            "data structure",
            "dsa"
        ],
        "category": "CS Fundamentals",
        "weight": 9,
        "level": "Critical",
        "days": 15,
        "project": "Build data structure implementations",
        "interview": [
            "Arrays",
            "Linked lists",
            "Stacks",
            "Queues",
            "Trees",
            "Graphs"
        ]
    },

    "Algorithms": {
        "aliases": [
            "algorithms",
            "algorithm",
            "algorithmic problem solving"
        ],
        "category": "CS Fundamentals",
        "weight": 9,
        "level": "Critical",
        "days": 15,
        "project": "Build an algorithm visualization tool",
        "interview": [
            "Sorting",
            "Searching",
            "Recursion",
            "Complexity",
            "Dynamic programming"
        ]
    },

    "OOP": {
        "aliases": [
            "oop",
            "object oriented programming",
            "object-oriented programming"
        ],
        "category": "CS Fundamentals",
        "weight": 8,
        "level": "High",
        "days": 7,
        "project": "Build an OOP-based management system",
        "interview": [
            "Class",
            "Object",
            "Inheritance",
            "Polymorphism",
            "Encapsulation",
            "Abstraction"
        ]
    },
}

ROLE_SKILLS = {

    "Python Developer": [
        "Python",
        "SQL",
        "OOP",
        "Git",
        "REST API"
    ],

    "Django Developer": [
        "Python",
        "Django",
        "SQL",
        "HTML",
        "CSS",
        "Git",
        "REST API"
    ],

    "Backend Developer": [
        "Python",
        "SQL",
        "REST API",
        "Git",
        "OOP"
    ],

    "Full Stack Developer": [
        "Python",
        "Django",
        "HTML",
        "CSS",
        "JavaScript",
        "SQL",
        "Git",
        "REST API"
    ],

    "Frontend Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Git"
    ],

    "Data Analyst": [
        "Python",
        "SQL",
        "Pandas",
        "NumPy"
    ],

    "Data Scientist": [
        "Python",
        "SQL",
        "Pandas",
        "NumPy",
        "Machine Learning"
    ],

    "Machine Learning Engineer": [
        "Python",
        "NumPy",
        "Pandas",
        "Machine Learning",
        "Scikit-learn",
        "Deep Learning"
    ],

    "DevOps Engineer": [
        "Linux",
        "Git",
        "Docker",
        "Kubernetes",
        "AWS"
    ]

}

def clean_text(text):
    if not text:
        return ""

    return text.lower().replace("\n", " ")


def contains_skill(text, alias):

    text = clean_text(text)
    alias = alias.lower()

    pattern = r"(?<!\w)" + re.escape(alias) + r"(?!\w)"

    return re.search(pattern, text) is not None


def extract_skills(text):

    found = []

    for skill_name, data in SKILL_CATALOG.items():

        for alias in data["aliases"]:

            if contains_skill(text, alias):

                found.append(skill_name)

                break

    return found


def get_role_skills(target_role):

    role = clean_text(target_role)

    for role_name, skills in ROLE_SKILLS.items():

        if role_name in role:

            return skills

    return []


def get_required_skills(job_description, target_role):

    job_skills = extract_skills(job_description)

    role_skills = get_role_skills(target_role)

    combined = list(dict.fromkeys(
        role_skills + job_skills
    ))

    return combined


def compare_skills(current_skills, required_skills):

    current = set(current_skills)

    required = set(required_skills)

    matched = current.intersection(required)

    missing = required.difference(current)

    return (
        sorted(matched),
        sorted(missing)
    )


def calculate_weighted_score(
    matched_skills,
    required_skills
):

    if not required_skills:

        return 0

    total_weight = 0
    matched_weight = 0

    for skill in required_skills:

        weight = SKILL_CATALOG.get(
            skill,
            {}
        ).get(
            "weight",
            5
        )

        total_weight += weight

        if skill in matched_skills:

            matched_weight += weight

    if total_weight == 0:

        return 0

    return round(
        (matched_weight / total_weight) * 100,
        2
    )


def get_skill_priority(skill):

    data = SKILL_CATALOG.get(
        skill,
        {}
    )

    return {
        "skill": skill,
        "priority": data.get(
            "level",
            "Medium"
        ),
        "weight": data.get(
            "weight",
            5
        ),
        "category": data.get(
            "category",
            "Other"
        ),
    }


def create_priorities(missing_skills):

    priorities = []

    for skill in missing_skills:

        data = SKILL_CATALOG.get(
            skill,
            {}
        )

        priorities.append({

            "skill": skill,

            "priority": data.get(
                "level",
                "Medium"
            ),

            "category": data.get(
                "category",
                "Other"
            ),

            "weight": data.get(
                "weight",
                5
            ),

            "days": data.get(
                "days",
                5
            )

        })

    priority_order = {
        "Critical": 1,
        "High": 2,
        "Medium": 3
    }

    priorities.sort(
        key=lambda x: (
            priority_order.get(
                x["priority"],
                4
            ),
            -x["weight"]
        )
    )

    return priorities


def create_roadmap(missing_skills):

    roadmap = []

    for index, skill in enumerate(
        missing_skills,
        start=1
    ):

        data = SKILL_CATALOG.get(
            skill,
            {}
        )

        roadmap.append({

            "step": index,

            "skill": skill,

            "priority": data.get(
                "level",
                "Medium"
            ),

            "days": data.get(
                "days",
                5
            ),

            "category": data.get(
                "category",
                "Other"
            ),

            "action":
                f"Learn {skill} fundamentals and practice the important interview concepts.",

            "project":
                data.get(
                    "project",
                    f"Build a small project using {skill}."
                )

        })

    return roadmap


def get_projects(missing_skills):

    projects = []

    for skill in missing_skills:

        data = SKILL_CATALOG.get(
            skill,
            {}
        )

        project = data.get("project")

        if project and project not in projects:

            projects.append(project)

    return projects[:6]


def get_interview_topics(
    required_skills
):

    topics = []

    for skill in required_skills:

        data = SKILL_CATALOG.get(
            skill,
            {}
        )

        for topic in data.get(
            "interview",
            []
        ):

            if topic not in topics:

                topics.append(topic)

    return topics[:20]


def get_category_scores(
    matched_skills,
    required_skills
):

    categories = {}

    for skill in required_skills:

        data = SKILL_CATALOG.get(
            skill,
            {}
        )

        category = data.get(
            "category",
            "Other"
        )

        if category not in categories:

            categories[category] = {
                "required": 0,
                "matched": 0
            }

        categories[category]["required"] += 1

        if skill in matched_skills:

            categories[category]["matched"] += 1

    for category, data in categories.items():

        required = data["required"]

        matched = data["matched"]

        if required:

            data["score"] = round(
                (matched / required) * 100,
                2
            )

        else:

            data["score"] = 0

    return categories


def analyze(
    current_skills,
    target_role,
    job_description
):

    user_skills = extract_skills(
        current_skills
    )

    required_skills = get_required_skills(
        job_description,
        target_role
    )

    matched_skills, missing_skills = compare_skills(
        user_skills,
        required_skills
    )

    score = calculate_weighted_score(
        matched_skills,
        required_skills
    )

    priorities = create_priorities(
        missing_skills
    )

    roadmap = create_roadmap(
        missing_skills
    )

    projects = get_projects(
        missing_skills
    )

    interview_topics = get_interview_topics(
        required_skills
    )

    category_scores = get_category_scores(
        matched_skills,
        required_skills
    )

    return {

        "user_skills": user_skills,

        "required_skills": required_skills,

        "matched_skills": matched_skills,

        "missing_skills": missing_skills,

        "match_percentage": score,

        "skill_priorities": priorities,

        "learning_roadmap": roadmap,

        "recommended_projects": projects,

        "interview_topics": interview_topics,

        "category_scores": category_scores,

    }
    
def extract_resume_text(resume_file):
    """
    Extract text from an uploaded PDF resume.
    """

    try:

        reader = PdfReader(resume_file)

        text = []

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text.append(page_text)

        return "\n".join(text).strip()

    except Exception as e:

        print("Resume extraction error:", e)

        return ""
    
    
def recommend_job_roles(resume_text):
    """
    Analyze resume skills and recommend suitable job roles.
    """

    # Detect skills from resume
    resume_skills = extract_skills(resume_text)

    recommendations = []

    # Check resume against every job role
    for role, required_skills in ROLE_SKILLS.items():

        matched_skills = []

        for skill in required_skills:

            if skill in resume_skills:

                matched_skills.append(skill)

        # Calculate percentage
        if required_skills:

            score = (
                len(matched_skills)
                / len(required_skills)
            ) * 100

        else:

            score = 0

        # Find missing skills
        missing_skills = [
            skill
            for skill in required_skills
            if skill not in resume_skills
        ]

        recommendations.append({

            "role": role,

            "score": round(score),

            "matched_skills": matched_skills,

            "missing_skills": missing_skills,

        })

    # Highest score first
    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return {

        "resume_skills": resume_skills,

        "recommendations": recommendations

    }