from flask import request, send_file
import requests, io
import matplotlib.pyplot as plt
from app.chart import bp


@bp.route("/plot")
def plot():
    width = request.args.get("width", type=int, default=800)
    labels = request.args.getlist("labels", None)

    dataset = (
        ("Frogs", 15),
        ("Hogs", 30),
        ("Dogs", 60),
        ("Logs", 90),
    )

    if labels and len(labels):
        dataset = [x for x in dataset if x[0] in labels]

    fig, ax = plt.subplots()
    fig.set_size_inches((width / 96), 5)
    ax.pie([x[1] for x in dataset], labels=[x[0] for x in dataset])
    img = io.BytesIO()
    plt.savefig(img)

    img.seek(0)
    plt.close()

    return send_file(img, mimetype="image/png")


@bp.route("/proxy")
def proxy_chart():
    r = requests.get(
        "https://echarts.apache.org/examples/data/asset/data/les-miserables.json"
    )

    return r.json()
