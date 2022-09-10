FROM python:3.9

WORKDIR /code

COPY ./ /code/

RUN apt-get install default-libmysqlclient-dev
RUN pip install -r /code/requirement.txt
RUN pip install pydantic[email]

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9090"]
