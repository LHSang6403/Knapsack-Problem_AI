FROM python:latest

COPY ./code /usr/code

WORKDIR /usr/code

CMD CMD ["python3", "/usr/code/Brute_Force/main.py"]
