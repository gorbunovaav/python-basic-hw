FROM tiangolo/uwsgi-nginx-flask:python3.12

RUN pip install --upgrade pip "poetry==1.8.3" \
    && poetry config virtualenvs.create false --local

COPY ./prestart.sh ./prestart.sh
    
COPY poetry.lock pyproject.toml ./
    
RUN poetry install
    
COPY ./app/ ./

# FROM python:3.12

# WORKDIR /app

# RUN pip install --upgrade pip "poetry==1.8.4" \
#     && poetry config virtualenvs.create false --local

# COPY poetry.lock pyproject.toml ./ 




# COPY ./app/ ./

# COPY ./entrypoint.sh ./

# RUN chmod +x ./entrypoint.sh

# CMD ["flask", "run"]



# COPY ./prestart.sh ./prestart.sh

# COPY poetry.lock pyproject.toml ./

# RUN poetry install

# COPY ./app/ ./