FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN pip install poetry && poetry install --no-root

RUN pip install flask openai 

# Expose the port your Flask app runs on  
EXPOSE 5000

COPY . /app

CMD ["poetry", "run", "python", "dragons/azure_openai_client.py"]
