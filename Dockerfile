FROM python:3.8-alpine


# https://stackoverflow.com/questions/59812009/what-is-the-use-of-pythonunbuffered-in-docker-file/59812588
ENV PYTHONUNBUFFERED 1

# RUN mkdir /code
WORKDIR /code


RUN apk add --update --no-cache postgresql-client jpeg-dev gettext redis mysql mysql-client
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev libffi-dev openssl-dev git mysql-client
RUN pip install --upgrade pip
#RUN pip install psycopg2-binary



# Adding environment variables
# COPY .env /code/

# Installing requirements
COPY requirements.txt /code/
RUN pip install --cache-dir /pip/cache -r requirements.txt
RUN apk del .tmp-build-deps
RUN rm -rf /pip/cache

# Setting entrypoint


COPY . /code/



# run entrypoint.sh
ENTRYPOINT ["python","mqtt.py"]