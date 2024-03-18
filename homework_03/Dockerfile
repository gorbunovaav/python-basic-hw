FROM python:3.9-buster

WORKDIR /var/app

RUN pip install "poetry==1.7.1"
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root

COPY app.py ./

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]



