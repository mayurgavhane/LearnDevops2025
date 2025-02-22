FROM python:slim
COPY . /pyapp
WORKDIR /pyapp
CMD python3 practice.py
