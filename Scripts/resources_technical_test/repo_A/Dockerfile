FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1
RUN mkdir /app
COPY ./main.py /app
COPY ./requirements.txt /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3", "/app/main.py" ]