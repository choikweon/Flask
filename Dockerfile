FROM python
ADD microblog /microblog
WORKDIR /microblog

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN gunicorn -b :5000 --access-logfile - --error-logfile - microblog:app

EXPOSE 5000
