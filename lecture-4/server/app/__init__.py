from flask import Flask, render_template, request

from config import Config
from app.extensions import bootstrap, toolbar, db, migrate

from .forms import DemoForm, TaskForm
from .models import Task


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    # Расширения
    toolbar.init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)

    bootstrap.init_app(app)

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

    return app
