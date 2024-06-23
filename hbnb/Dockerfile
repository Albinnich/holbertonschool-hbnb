FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 5000

WORKDIR /app

RUN apk update \
    && apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . /app/

VOLUME /app/data

CMD ["gunicorn", "--bind", "0.0.0.0:" + ${PORT}, "app:app"]
