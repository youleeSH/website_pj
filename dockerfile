FROM python:3.11-slim

WORKDIR /app

COPY ./backend /app

RUN pip install --upgrade pip
COPY ./backend/requirements.txt .
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["gunicorn", "mytestsite.wsgi:application", "--bind", "0.0.0.0:8000"]
