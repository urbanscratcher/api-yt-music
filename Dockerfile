FROM python:3.9-alpine
WORKDIR .

COPY ./requirements.txt ./requirements.txt
COPY ./oauth.json ./oauth.json
RUN pip install --no-cache-dir --upgrade -r /requirements.txt
COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "5000"]


