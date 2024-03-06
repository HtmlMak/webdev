from flask import Flask, render_template, request, send_file
from config import Config
from app.extensions import bootstrap, db, migrate, cors
import requests

import matplotlib.pyplot as plt
import io
from .forms import DemoForm, TaskForm
from .models import Task


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    # Расширения
    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)
    cors.init_app(app)

    @app.route("/", methods=["GET", "POST"])
    def index():
        form = DemoForm()

        if request.method == "GET":
            return render_template("index.html", form=form)
        elif request.method == "POST":
            first_name = ""
            last_name = ""

            if form.validate_on_submit():
                first_name = form.first_name.data
                last_name = form.last_name.data

            return render_template(
                "index.html", first_name=first_name, last_name=last_name, form=form
            )
        else:
            return

    @app.route("/post", methods=["GET", "POST"])
    def post():
        form = TaskForm()
        tasks = Task.query.all()

        if request.method == "POST":
            if form.validate_on_submit():
                newTask = Task(
                    title=form.title.data,
                    content=form.content.data,
                    isDone=form.isDone.data,
                )

                db.session.add(newTask)
                db.session.commit()
                form = TaskForm(formdata=None)
                tasks = Task.query.all()

        return render_template("index.html", form=form, tasks=tasks)

    @app.route("/table")
    def table():
        data = [{"name": "Alice", "age": 20}, {"name": "Bob", "age": 30}]

        return render_template("table.html", table=data)

    @app.route("/table-row-data")
    def table_row_data():
        data = [
            { "id": 1, "name": "Oli Bob", "age": "12", "col": "red" },
            { "id": 2, "name": "Mary May", "age": "1", "col": "blue" },
            { "id": 3, "name": "Christine Lobowski", "age": "42", "col": "green" },
            { "id": 4, "name": "Brendon Philips", "age": "125", "col": "orange" },
            { "id": 5, "name": "Margret Marmajuke", "age": "16", "col": "yellow" }
        ]

        return data

    from app.chart import bp as chartApp 
    app.register_blueprint(chartApp, url_prefix='/chart')   

    from app.api import bp as apiApp 
    app.register_blueprint(apiApp, url_prefix='/api')   

    return app 
