FROM python:latest

RUN mkdir /src
WORKDIR /src
ENV PYTHONPATH "${PYTHONPATH}:/src/"
ENV PATH "/src/scripts:${PATH}"
COPY requirements.txt /src
RUN pip install -r requirements.txt
COPY . /src
RUN chmod +x /src/scripts/*
ENTRYPOINT ["docker-entrypoint.sh"]