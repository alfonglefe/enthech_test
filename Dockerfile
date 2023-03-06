FROM python:latest

WORKDIR /

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "./searcher.py", "enthec"]