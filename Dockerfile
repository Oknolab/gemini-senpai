FROM python:3.11-slim

RUN pip install google-genai slack_bolt

WORKDIR /app
COPY . .
