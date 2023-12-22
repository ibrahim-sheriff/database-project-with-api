from contextlib import asynccontextmanager
from datetime import datetime

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from json2html import json2html

from database import create_tables, select_query


@asynccontextmanager
async def lifespan(app: FastAPI):
    # execute code on App startup

    # create database tables
    create_tables()

    yield

    # execute code on App shutdown
    pass


# FastAPI app initialization
app = FastAPI(title="Shipblu Analytics", lifespan=lifespan)


@app.get("/health")
async def health():
    return str(datetime.now())


@app.get("/hello-world")
async def hello_world():
    return "Hello World"


@app.get("/courses")
async def get_courses():
    query = "SELECT * FROM courses"
    result = select_query(query)

    html_table = json2html.convert(json=result)

    return HTMLResponse(content=html_table, status_code=200)


@app.get("/courses/{course_id}")
async def get_course(course_id):
    query = f"SELECT * FROM courses WHERE id = {course_id}"
    result = select_query(query)

    html_table = json2html.convert(json=result)

    return HTMLResponse(content=html_table, status_code=200)


@app.get("/students")
async def get_students():
    query = "SELECT * FROM students"
    result = select_query(query)

    html_table = json2html.convert(json=result)

    return HTMLResponse(content=html_table, status_code=200)


@app.get("/students/{student_id}")
async def get_student(student_id: str):
    query = f"SELECT * FROM students WHERE id = {student_id}"
    result = select_query(query)
    
    html_table = json2html.convert(json=result)

    return HTMLResponse(content=html_table, status_code=200)


@app.get("/sections")
async def get_sections():
    query = """
        SELECT
            ST.id AS student_id,
            CONCAT(ST.first_name, ' ', ST.last_name) AS student_name,
            SC.id AS section_id,
            SC.year AS section_year,
            CS.id AS course_id,
            CS.name AS course_name,
            STSC.grade AS course_grade
        FROM student_sections STSC
        INNER JOIN students ST ON STSC.student_id = ST.id
        INNER JOIN sections SC ON STSC.section_id = SC.id
        INNER JOIN courses CS ON SC.course_id = CS.id
    """
    result = select_query(query)

    html_table = json2html.convert(json=result)

    return HTMLResponse(content=html_table, status_code=200)
