import aiosqlite
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os
import asyncio

app = FastAPI()

PATH = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(PATH, "courses_async.db")


class Course(BaseModel):
    title: str
    description: str
    instructor: str


async def init_db():
    async with aiosqlite.connect(DB) as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                instructor TEXT NOT NULL
            )
            """
        )
        await db.commit()


@app.get("/courses")
async def list_courses():
    async with aiosqlite.connect(DB) as db:
        async with db.execute("SELECT * FROM courses") as cursor:
            courses = await cursor.fetchall()
    return [
        {
            "id": course[0],
            "title": course[1],
            "description": course[2],
            "instructor": course[3],
        }
        for course in courses
    ]


@app.post("/courses")
async def create_course(input: Course):
    async with aiosqlite.connect(DB) as db:
        async with db.execute(
            f"INSERT INTO courses (title, description, instructor) "
            f"VALUES ('{input.title}', '{input.description}', "
            f"'{input.instructor}')"
        ) as cursor:
            last_row_id = cursor.lastrowid
        await db.commit()
    return {"id": last_row_id}


@app.put("/courses/{course_id}")
async def update_course(course_id: int, input: Course):
    async with aiosqlite.connect(DB) as db:
        await db.execute(
            f"UPDATE courses SET title='{input.title}', "
            f"description='{input.description}', "
            f"instructor='{input.instructor}' WHERE id={course_id}"
        )
        await db.commit()
    return {"status": "success"}


@app.delete("/courses/{course_id}")
async def delete_course(course_id: int):
    async with aiosqlite.connect(DB) as db:
        await db.execute(f"DELETE FROM courses WHERE id={course_id}")
        await db.commit()
    return {"status": "success"}


if __name__ == "__main__":
    asyncio.run(init_db())
    uvicorn.run("main_async:app", host="0.0.0.0", port=3001, reload=False)
