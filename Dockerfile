FROM python:3.9.18-alpine
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir Flask
EXPOSE 5000
CMD ["python", "bye.py"]