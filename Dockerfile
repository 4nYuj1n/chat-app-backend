FROM python:3.10-alpine

WORKDIR /CHAT-APP
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN rm -rf .git

EXPOSE 8090

CMD ["uvicorn","main:app","--port","8090","--host","0.0.0.0"]
