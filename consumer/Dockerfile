FROM python:3.12.4-slim@sha256:e3ae8cf03c4f0abbfef13a8147478a7cd92798a94fa729a36a185d9106cbae32

WORKDIR /app
RUN pip install requests
COPY app.py app.py
CMD [ "python", "app.py" ]