FROM python:3.7.4
ADD . /code
WORKDIR /code
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
CMD ["python", "rfmp_comp_bot"]
