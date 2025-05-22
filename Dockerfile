FROM python:3.11-slim

RUN pip install fastapi uvicorn google-genai

WORKDIR /app
COPY . .
