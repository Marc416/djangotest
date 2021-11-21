FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/Marc416/djangotest.git

WORKDIR /home/djangotest/pragmatic/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-c0c=*q#336=l4_g^k#7%ndslat)ndp=@ie-aw!ja-$c%!6+ghx" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]