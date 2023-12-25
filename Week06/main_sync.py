import sqlite3
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

PATH = os.path.dirname(os.path.realpath(__file__))
DB = os.path.join(PATH, "courses_sync.db")


def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            instructor TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


@app.route("/courses")
def list_courses():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT * FROM courses")
    courses = c.fetchall()
    conn.close()
    return jsonify(
        [
            {
                "id": course[0],
                "title": course[1],
                "description": course[2],
                "instructor": course[3],
            }
            for course in courses
        ]
    )


@app.route("/courses", methods=["POST"])
def create_course():
    title = request.json["title"]
    description = request.json["description"]
    instructor = request.json["instructor"]
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(
        f"INSERT INTO courses (title, description, instructor) "
        f"VALUES ('{title}', '{description}', '{instructor}')"
    )
    conn.commit()
    last_row_id = c.lastrowid
    conn.close()
    return jsonify({"id": last_row_id})


@app.route("/courses/<int:course_id>", methods=["PUT"])
def update_course(course_id: int):
    title = request.json["title"]
    description = request.json["description"]
    instructor = request.json["instructor"]
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(
        f"UPDATE courses SET title='{title}', description='{description}', "
        f"instructor='{instructor}' WHERE id={course_id}"
    )
    conn.commit()
    conn.close()
    return jsonify({"status": "success"})


@app.route("/courses/<int:course_id>", methods=["DELETE"])
def delete_course(course_id: int):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(f"DELETE FROM courses WHERE id={course_id}")
    conn.commit()
    conn.close()
    return jsonify({"status": "success"})


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=3000, debug=False)
