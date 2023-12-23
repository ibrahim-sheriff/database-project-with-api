from pathlib import Path

import sqlalchemy as db

DB_USER = "ibrahimsherif"
DB_PASSWORD = "123456"
DB_HOST = "localhost:3306"
DB_NAME = "aast_collage"
DATABASE_CONNECTION = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}" # noqa

engine = db.create_engine(DATABASE_CONNECTION)


def create_tables():
    create_query = Path("./sql/create.sql").read_text()
    insert_query = Path("./sql/insert.sql").read_text()

    try:
        with engine.begin() as conn:

            queries = create_query.split(";")[:-1]
            for query in queries:
                conn.execute(db.text(query))

            queries = insert_query.split(";")[:-1]
            for query in queries:
                conn.execute(db.text(query))

    except Exception as ex:
        print(ex)


def select_query(query: str):
    try:
        with engine.begin() as conn:
            result = conn.execute(db.text(query))
            result = result.fetchall()

            return_list = []
            for row in result:
                return_list.append(row._asdict())

    except Exception as ex:
        print(ex)

    return return_list


def insert_update_query(query: str, params: dict):
    try:
        with engine.begin() as conn:
            conn.execute(db.text(query), params)

    except Exception as ex:
        print(ex)
