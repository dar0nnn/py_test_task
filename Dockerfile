FROM python:3.6-alpine

RUN apk add mc

RUN /bin/sh -c "apk add --no-cache bash"

RUN mkdir -p /meetings/src/app

WORKDIR /meetings/src/app

COPY . /meetings/src/app
RUN \
 apk add --no-cache python3 postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

RUN chmod +x /meetings/src/app/entrypoint.sh

CMD ["/meetings/src/app/entrypoint.sh"]

EXPOSE 8000
