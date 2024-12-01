FROM python:3.8-slim

RUN pip install uv

WORKDIR /app
COPY requirements.lock ./
RUN uv pip install --no-cache --system -r requirements.lock

COPY static ./static
COPY templates ./templates
COPY app.py ./app.py
COPY dbconnect.py ./dbconnect.py


CMD ["uv", "run", "python", "app.py"]