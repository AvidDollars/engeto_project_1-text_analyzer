FROM python:3.10-slim
WORKDIR /app
COPY *.py /app
COPY data /app/data
COPY utils /app/utils
COPY requirements.txt /app
RUN pip install -r requirements.txt
ENTRYPOINT [ "python3", "main.py" ]
