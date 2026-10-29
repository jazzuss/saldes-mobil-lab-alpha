FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml ./
COPY src/ ./src/
RUN pip install --no-cache-dir -e ".[api]"

COPY data/ ./data/
COPY outputs/modell.joblib outputs/matvarden.json ./outputs/

RUN useradd --uid 1000 saldes
USER 1000

EXPOSE 8000
CMD ["uvicorn", "churn.api:app", "--host", "0.0.0.0", "--port", "8000"]