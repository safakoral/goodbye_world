FROM python:3.9.18-alpine
WORKDIR /app
COPY goodbye_world.py .
RUN pip install --no-cache-dir Flask
CMD ["python", "./goodbye_world.py"]