\# 🤖 SkillGap AI — AI Resume Career Advisor



SkillGap AI is a Django-based career intelligence platform that analyzes a user's resume and technical skills, recommends suitable job roles, identifies skill gaps, and generates a personalized learning roadmap.



\## 🚀 Features



\- 📄 Upload PDF resume

\- 🔍 Extract skills from resume

\- 💼 Recommend suitable job roles

\- 📊 Calculate job-role match percentage

\- ✅ Identify matched skills

\- ❌ Identify missing skills

\- 🎯 Analyze skill categories

\- 🔥 Prioritize important skill gaps

\- 📚 Generate personalized learning roadmap

\- 💻 Recommend projects for skill development

\- 🎤 Generate interview preparation topics

\- 📜 Maintain analysis history



\## 🔄 How It Works



```text

Upload Resume

&#x20;     ↓

Extract Resume Text

&#x20;     ↓

Detect Technical Skills

&#x20;     ↓

Compare Skills With Job Roles

&#x20;     ↓

Calculate Match Percentage

&#x20;     ↓

Recommend Suitable Roles

&#x20;     ↓

Identify Skill Gaps

&#x20;     ↓

Generate Learning Roadmap

&#x20;     ↓

Recommend Projects

&#x20;     ↓

Interview Preparation

```



\## 💼 Example Job Roles



SkillGap AI currently analyzes resumes against roles such as:



\- Python Developer

\- Django Developer

\- Backend Developer

\- Full Stack Developer

\- Frontend Developer

\- Data Analyst

\- Data Scientist

\- Machine Learning Engineer

\- DevOps Engineer



\## 🛠️ Technologies Used



\### Backend



\- Python

\- Django



\### Resume Processing



\- PyPDF



\### Frontend



\- HTML

\- CSS



\### Database



\- SQLite



\### Version Control



\- Git

\- GitHub



\## 📁 Project Structure



```text

skillgap-ai/

│

├── analyzer/

│   ├── migrations/

│   ├── static/

│   │   └── analyzer/

│   │       └── style.css

│   ├── templates/

│   │   └── analyzer/

│   │       ├── home.html

│   │       ├── result.html

│   │       └── history.html

│   ├── ai\_engine.py

│   ├── models.py

│   ├── urls.py

│   └── views.py

│

├── skill\_gap\_project/

│   ├── settings.py

│   ├── urls.py

│   ├── asgi.py

│   └── wsgi.py

│

├── manage.py

├── .gitignore

└── README.md

```



\## ⚙️ Installation



\### 1. Clone the repository



```bash

git clone https://github.com/lohithanjal/skillgap-ai.git

```



\### 2. Open the project



```bash

cd skillgap-ai

```



\### 3. Create a virtual environment



```bash

python -m venv venv

```



\### 4. Activate the virtual environment



\### Windows



```powershell

venv\\Scripts\\activate

```



\### 5. Install dependencies



```bash

pip install django pypdf

```



\### 6. Apply migrations



```bash

python manage.py migrate

```



\### 7. Start the development server



```bash

python manage.py runserver

```



\### 8. Open the application



```text

http://127.0.0.1:8000/

```



\## 📄 Resume Upload



The application accepts PDF resumes.



After uploading a resume, SkillGap AI extracts the resume text and detects supported technical skills.



The detected skills are then compared with the requirements of different job roles.



\## 📊 Job Recommendation



The system calculates a match percentage based on the skills detected in the resume.



For example:



```text

Python Developer       100%

Django Developer        86%

Backend Developer       80%

Full Stack Developer    75%

Data Analyst            50%

DevOps Engineer         20%

```



The system also displays:



\- Skills already available

\- Skills that are missing

\- Application recommendation



\## 🧠 Skill Gap Analysis



For a selected target role, SkillGap AI compares the user's current skills with the required skills.



Example:



```text

Target Role:

Django Developer



Matched Skills:

✓ Python

✓ Django

✓ SQL

✓ HTML

✓ Git



Missing Skills:

\+ REST API

\+ CSS

```



\## 📚 Personalized Learning Roadmap



Based on missing skills, the system creates a learning roadmap.



The roadmap helps users understand:



1\. What to learn

2\. Which skills are most important

3\. Estimated learning time

4\. Recommended projects



\## 🎤 Interview Preparation



The application also generates interview topics related to the required skills.



This helps users prepare for technical interviews after identifying their skill gaps.



\## 🔐 Privacy



Uploaded resumes and the local SQLite database are excluded from Git using `.gitignore`.



The following files/directories are not uploaded:



```text

venv/

db.sqlite3

media/

.env

\_\_pycache\_\_/

```



\## 🔮 Future Improvements



Planned improvements include:



\- 🤖 Semantic NLP-based resume analysis

\- 🧠 Embedding-based skill matching

\- 📌 Resume evidence snippets

\- 🎯 Skill confidence scores

\- 💼 Real-time job vacancy matching

\- 🔎 Job description analysis

\- 📈 Career readiness score

\- 👤 User authentication

\- 📊 Career progress dashboard

\- 🌐 REST API

\- 🐳 Docker support

\- ☁️ Cloud deployment

\- 🧪 Automated testing

\- 🔄 CI/CD pipeline



\## 👨‍💻 Author



\*\*Lohith Anjal\*\*



B.Tech — Computer Science Engineering



GitHub:



https://github.com/lohithanjal



\## ⭐ Project Goal



The goal of SkillGap AI is to help students and job seekers answer three important questions:



> \*\*What skills do I have?\*\*



> \*\*Which jobs am I suitable for?\*\*



> \*\*What should I learn next to become job-ready?\*\*



\---



⭐ If you find this project useful, consider giving it a star.

