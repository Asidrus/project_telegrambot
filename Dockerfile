FROM python:3.10
ARG path=/app
ARG PROJECT='telegrambot'
WORKDIR $path/$PROJECT

RUN pip install "uvicorn[standard]"
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
CMD ["sh", "-c", "uvicorn main:app --reload --host 0.0.0.0 --port 443"]