Project Voting Platform

A  voting website built with Django and Docker.  



Project Purpose

- Build a web application using Git, Django, and Docker.  


Project Overview

- The admin can create projects with a title and detailed description.
- Users can browse the project list and view each project's detail page.
- Users can rate a project on a int scale from 1 to 5.
- After submitting a rating, users can view the average score of the project.
- The admin can sort projects by their average score.  


Tech Stack

- Python 3.11
- Django 5.2
- PostgreSQL (via Docker container)
- Nginx (frontend web server)
- Docker / Docker Compose  


Project Structure

website_pj/  
├── backend/  
│ ├── develop/     # Main Django app  
│ ├── mytestsite/  # Django project configuration  
│ ├── static/      # Static files  
│ ├── manage.py  
│ └── requirements.txt  
├── nginx/  
│ └── default.conf # Nginx configuration  
├── docker-compose.yml  
├── Dockerfile  
└── README.md  


How to Run
```
docker-compose up --build
docker-compose exec backend python manage.py migrate
```  


Admin Account

- ID : admin
- password : seo040302


Access

- User Page : http://localhost/project/
- Admin Page : http://localhost/admin/  


GitHub

- https://github.com/youleeSH/website_pj  


License

- MIT License