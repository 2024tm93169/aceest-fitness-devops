from flask import Flask, jsonify, request

def create_app():
    app = Flask(__name__)
    workouts = []  # in-memory store for demo purposes

    @app.get("/")
    def index():
        return jsonify(
            message="ACEest Fitness API: use /api/health, /api/workouts (GET, POST)"
        ), 200

    @app.get("/api/health")
    def health():
        return jsonify(status="ok"), 200

    @app.post("/api/workouts")
    def add_workout():
        data = request.get_json(silent=True) or {}
        workout = data.get("workout")
        duration = data.get("duration")

        if not workout or duration is None:
            return jsonify(error="Fields 'workout' and 'duration' are required."), 400

        try:
            duration = int(duration)
        except (TypeError, ValueError):
            return jsonify(error="'duration' must be an integer."), 400

        entry = {"workout": workout, "duration": duration}
        workouts.append(entry)
        return jsonify(message=f"'{workout}' added successfully!", entry=entry, count=len(workouts)), 201

    @app.get("/api/workouts")
    def list_workouts():
        return jsonify(workouts=workouts, count=len(workouts)), 200

    return app

app = create_app()