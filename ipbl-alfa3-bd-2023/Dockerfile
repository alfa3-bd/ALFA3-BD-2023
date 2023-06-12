FROM python:3.9

COPY . .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# gunicorn
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]

# docker logout

# docker build -t alfa3-bd:1.0.0 .

# docker tag alfa3-bd:1.0.0 projetoalfa/alfa3-bd:1.0.0

# docker login 

# docker push projetoalfa/alfa3-bd:1.0.0