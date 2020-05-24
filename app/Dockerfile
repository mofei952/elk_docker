FROM python:3.7-alpine

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

COPY app.py /code/app.py
COPY requirements.txt /code/requirements.txt

WORKDIR /code

#RUN apk add --no-cache gcc musl-dev linux-headers

RUN pip install -r requirements.txt

EXPOSE 5000/TCP
CMD ["flask", "run"]