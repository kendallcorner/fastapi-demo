FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY Pipfile* .
RUN pip install --upgrade pip && pip install pipenv
RUN pipenv install

# copy the code and install for real
COPY backend backend

# defines the fastapi entry point
ENV APP_MODULE=backend.__main__:app
