FROM  python:3.7-alpine
LABEL  NAME K-AMOS
ENV PYTHONUNBUFFERED 1 
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN mkdir /app
WORKDIR /app+
COPY ./app /app
EXPOSE 80 3500 8000
RUN adduser -D user 
USER user  

