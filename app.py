from flask import Flask, jsonify, request

WHO = "Zain MEHR"  


def create_app():
    app = Flask(__name__)
    tasks = []  

    @app.get("/")
    def index():
        return jsonify(
            message="Bienvenue sur myapp",
            endpoints=["/health", "/who", "/tasks"],
        )

    @app.get("/health")
    def health():
        return jsonify(status="ok"), 200

    @app.get("/who")
    def who():
        return WHO

    @app.get("/tasks")
    def list_tasks():
        return jsonify(tasks)

    @app.post("/tasks")
    def add_task():
        data = request.get_json(silent=True) or {}
        title = str(data.get("title", "")).strip()
        if not title:
            return jsonify(error="Le champ 'title' est obligatoire"), 400
        task = {"id": len(tasks) + 1, "title": title}
        tasks.append(task)
        return jsonify(task), 201

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)