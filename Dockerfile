FROM tiangolo/uwsgi-nginx-flask:flask

RUN pip install sqlalchemy flask_cors

COPY ./bookflask.py /app/main.py
COPY ./models.py ./database.py ./hshb.db ./uwsgi.ini /app/
COPY ./templates/ /app/templates/
COPY ./static/ /app/static/
