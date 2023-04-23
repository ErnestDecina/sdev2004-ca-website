FROM python:3.11.3-alpine

WORKDIR /srv/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]