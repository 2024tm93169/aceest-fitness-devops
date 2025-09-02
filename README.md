# ACEest Fitness & Gym – DevOps Assignment Solution

A minimal Flask API inspired by the provided sample application. It lets you add workouts and list them, plus includes unit tests, Docker packaging, and a GitHub Actions CI workflow that builds the Docker image and executes tests *inside the image*.

## Project Structure

```text
.
├── app.py
├── requirements.txt
├── Dockerfile
├── tests/
│   └── test_app.py
└── .github/
    └── workflows/
        └── ci.yml
```

## Run locally (no Docker)

1. **Python 3.11+** recommended
2. Create a virtual env and install deps:
   ```bash
   python -m venv .venv
   . .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Start the app:
   ```bash
   gunicorn -b 0.0.0.0:8080 app:app
   ```
   The API will be available at `http://localhost:8080`.

### API quickstart

```bash
# Health
curl http://localhost:8080/api/health

# Add workout
curl -X POST http://localhost:8080/api/workouts \
     -H "Content-Type: application/json" \
     -d '{"workout":"run","duration":30}'

# List workouts
curl http://localhost:8080/api/workouts
```

## Run tests locally

```bash
pytest -q
```

## Run with Docker

```bash
docker build -t aceest-fitness:dev .
docker run --rm -p 8080:8080 aceest-fitness:dev
```

## CI/CD with GitHub Actions

The workflow at `.github/workflows/ci.yml`:
- builds the Docker image from this repo, and
- runs `pytest` **inside the built image** to validate functionality.

This satisfies the assignment’s automated build and automated testing requirements on every `push` and `pull_request`.

## Git & GitHub setup (one-time)

```bash
git init
git add .
git commit -m "Initial commit: Flask app, tests, Dockerfile, CI workflow"
git branch -M main
# create an empty public repo on GitHub named e.g. aceest-fitness-devops
git remote add origin https://github.com/<your-username>/aceest-fitness-devops.git
git push -u origin main
```

## Notes

- This demo uses an in-memory list for workouts to keep things simple. In a real app you'd use a database.
- The API mirrors the functionality of adding and viewing workouts from the desktop sample, adapted to HTTP endpoints.