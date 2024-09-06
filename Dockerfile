FROM python:3.10-alpine

WORKDIR /CHAT-APP
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN rm -rf .git

EXPOSE 8000

CMD ["uvicorn","main:app"]
