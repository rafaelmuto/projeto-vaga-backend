FROM python:3

WORKDIR /usr/src/app

COPY ./app .
COPY ./app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD ["flask", "run"]