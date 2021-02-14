FROM python:3.6.10-slim-stretch

# make user and upgrade pip
RUN groupadd -r sentiment && \
    useradd -r -m -g sentiment sentiment && \
    pip install -U pip

# Copy requirements and installl
COPY --chown=sentiment:sentiment ./requirements/requirements.txt /app/requirements.txt
COPY --chown=sentiment:sentiment ./src/api /app/api

WORKDIR /app

# install requirements
RUN pip install -r /app/requirements.txt && \
    rm -rf /app/requirements.txt

USER sentiment

# super hack to get model in the Docker image
RUN python3 -c "from transformers import pipeline; pipeline('sentiment-analysis')"

EXPOSE 5000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "5000"]