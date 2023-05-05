"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaae0bhp8u791gtka9g-a.oregon-postgres.render.com",
        database="todo_kdym",
        user="root",
        password="TFqy1wVEQKqkWjAFCeCGbWq1O880pHy1")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
