# BUILD STAGE

# Python 3.11.0a3 (https://hub.docker.com/layers/python/library/python/3.11.0a3/images/sha256-b7e4e0ec63345f7fe978e40fb32398fe27e227eb947e85726581bc94d4807eb7)
FROM python@sha256:b7e4e0ec63345f7fe978e40fb32398fe27e227eb947e85726581bc94d4807eb7 as builder

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt


# RUN STAGE

# Python 3.11.0a3-slim (https://hub.docker.com/layers/python/library/python/3.11.0a3-slim/images/sha256-4fe046d62b0d4c3ac1c9b564cad3aa1e95b484a6d19c8758e74bf525f3390d38)
FROM python@sha256:4fe046d62b0d4c3ac1c9b564cad3aa1e95b484a6d19c8758e74bf525f3390d38

WORKDIR /app

COPY --from=builder /usr/local /usr/local
COPY src  /app/src/
COPY LICENSE /app

LABEL author="Raphael Tholl raphael.tholl@ibm.com"

RUN groupadd -r appuser &&\
    useradd -r appuser -g appuser -s /sbin/nologin -c "Non-root user to run application" &&\
    chown -R appuser:appuser /app

VOLUME /app/src/output

USER appuser

ENTRYPOINT ["python3"]

CMD ["src/main.py"]