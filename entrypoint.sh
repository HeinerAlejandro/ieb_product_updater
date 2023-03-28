#!/bin/sh

python manage.py collectstatic --no-input
python manage.py spectacular --color --file ./schema.yaml

python manage.py makemigrations --no-input
python manage.py migrate --no-input

if [$IEB_DJ_DATA_FAKE==true]
  then
    python ./create_data_fake.py;
  fi

uvicorn --host $HOST --port $EXPOSE_PORT ieb_product_updater.asgi:application