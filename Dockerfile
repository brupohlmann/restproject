FROM python:3.6.5


# Creating workspace
ENV WORKSPACE=/usr/src/app
RUN mkdir -p $WORKSPACE
WORKDIR $WORKSPACE


# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev

# Project dependency
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . $WORKSPACE


RUN python manage.py collectstatic --noinput


RUN chmod +x cmd.sh

CMD ["./cmd.sh"]