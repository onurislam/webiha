# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
CMD ".\ihaenv\Scripts\activate"
CMD [ "python3", "manage.py" , "runserver"]