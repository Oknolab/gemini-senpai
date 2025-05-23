FROM python:3.11-slim

RUN pip install fastapi uvicorn google-genai slack_bolt

WORKDIR /app
COPY . .
