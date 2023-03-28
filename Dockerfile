FROM python:3.11-slim-bullseye

MAINTAINER heiner.enis@gmail.com

ENV PYTHONUNUNBUFFERED 1

WORKDIR /ieb_product_updater

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "./entrypoint.sh"]