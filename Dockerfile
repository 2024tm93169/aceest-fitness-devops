# Minimal production-ready image for the Flask app + tests
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /

# Install runtime + test dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app (including tests)
COPY . .

EXPOSE 8080

# Default command runs the web app; CI will override the command to run tests
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
