FROM python:3.6-alpine as app

RUN apk add mc

RUN /bin/sh -c "apk add --no-cache bash"

RUN mkdir -p /meetings/src

WORKDIR /meetings/src

COPY . /meetings/src

RUN set -e; \
    apk add --no-cache python3 postgresql-libs && \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
		python3-dev \
		musl-dev \
		postgresql-dev\
	; \
	python3 -m pip install -r requirements.txt --no-cache-dir; \
	apk del .build-deps;

RUN chmod +x /meetings/src/entrypoint.sh

CMD ["/meetings/src/entrypoint.sh"]

EXPOSE 8000