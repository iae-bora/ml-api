FROM python:3.7-slim
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 8080
CMD ["gunicorn", "wsgi:app", "--bind", "0.0.0.0:8080", "--log-level=debug", "--workers=4"]