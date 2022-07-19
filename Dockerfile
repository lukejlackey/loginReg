FROM python:3.7-alpine

EXPOSE 5000/tcp

WORKDIR /flask_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY application/ /flask_app/application/

COPY app.py .

CMD [ "python", "./app.py" ]