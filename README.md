Project Voting Platform

Django와 Docker를 이용한 투표 웹사이트  



프로젝트 목적

- Git, Django, Docker를 이용하여 web site 구축하기  


프로젝트 개요

- 관리자는 project 주제와 상세 내용을 입력할 수 있습니다
- 사용자는 프로젝트 리스트에서 원하는 프로젝트를 선택하여 상세 페이지 확인 가능
- 사용자는 해당 프로젝트를 int 1~5점으로 평가할 수 있습니다
- 사용자는 평가 후 평균 점수를 확인할 수 있습니다.
- 관리자는 평균 점수 기준으로 프로젝트를 정렬해서 볼 수 있습니다  


기술 스택

- Python 3.11
- Django 5.2
- PostgreSQL : Docker 컨테이너 사용
- Nginx : 프론트 웹서버
- Docker / Docker Compose  


폴더 구조

website_pj/  
├── backend/  
│ ├── develop/ # 주요 Django 앱  
│ ├── mytestsite/ # Django 프로젝트 설정  
│ ├── static/ # 정적 파일  
│ ├── manage.py  
│ └── requirements.txt  
├── nginx/  
│ └── default.conf # Nginx 설정  
├── docker-compose.yml  
├── Dockerfile  
└── README.md  


실행 방법

docker-compose up --build
docker-compose exec backend python manage.py migrate  


관리자 계정

ID : admin
password : seo040302


접속

사용자 : http://localhost/project/
관리자 페이지 : http://localhost/admin/  


GitHub

https://github.com/youleeSH/website_pj  


라이선스

MIT License