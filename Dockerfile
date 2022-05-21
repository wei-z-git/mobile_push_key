FROM python:3.9

RUN pip install fastapi uvicorn requests python-multipart -i https://mirrors.aliyun.com/pypi/simple/

EXPOSE 80

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]