from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os
import asyncio
import asyncpg
from asyncpg.pool import Pool
from asyncpg import Record
from typing import List, Dict
from contextlib import asynccontextmanager


class Course(BaseModel):
    title: str
    description: str
    instructor: str


async def create_db_pool(app: FastAPI):
    print("Creating db pool")
    host = os.getenv("DATABASE_HOST", "localhost")
    port = os.getenv("DATABASE_PORT", "5433")
    user = os.getenv("DATABASE_USER", "postgres")
    password = os.getenv("DATABASE_PASSWORD", "postgres")
    database = os.getenv("DATABASE_DB", "postgres")
    pool: Pool = await asyncpg.create_pool(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        min_size=5,
        max_size=1000,
    )
    app.state.pool = pool


async def init_db(app: FastAPI):
    async with app.state.pool.acquire() as connection:
        await connection.execute(
            """
            CREATE TABLE IF NOT EXISTS courses (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                instructor TEXT NOT NULL
            )
            """
        )


async def destroy_db_pool(app: FastAPI):
    print("Destroying db pool")
    pool: Pool = app.state.pool
    await pool.close()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_pool(app)
    await init_db(app)
    yield
    await destroy_db_pool(app)


app = FastAPI(lifespan=lifespan)


@app.get("/courses")
async def list_courses():
    async with app.state.pool.acquire() as connection:
        course_query = "SELECT * FROM courses"
        results: List[Record] = await connection.fetch(course_query)
        results_as_dict: List[Dict] = [dict(course) for course in results]
    return results_as_dict


@app.post("/courses")
async def create_course(input: Course):
    async with app.state.pool.acquire() as connection:
        new_course_id = await connection.fetchval(
            """
            INSERT INTO courses(title, description, instructor) 
            VALUES($1, $2, $3) RETURNING id
            """,
            input.title,
            input.description,
            input.instructor,
        )
    return {"id": new_course_id}


@app.put("/courses/{course_id}")
async def update_course(course_id: int, input: Course):
    async with app.state.pool.acquire() as connection:
        await connection.execute(
            """
            UPDATE courses 
            SET title = $1, description = $2, instructor = $3 
            WHERE id = $4
            """,
            input.title,
            input.description,
            input.instructor,
            course_id,
        )
    return {"status": "success"}


@app.delete("/courses/{course_id}")
async def delete_course(course_id: int):
    async with app.state.pool.acquire() as connection:
        await connection.execute("DELETE FROM courses WHERE id = $1", course_id)
    return {"status": "success"}


if __name__ == "__main__":
    uvicorn.run(
        "main_async_pg:app",
        host="0.0.0.0",
        port=3003,
        reload=False,
        workers=8,
    )
