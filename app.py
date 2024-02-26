'''App logic and routes'''

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

app = Flask(__name__)

tasks = []


@app.route("/")
def index():
    '''Return the index.html template'''

    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    '''Append tasks'''

    task = request.form["task"]
    tasks.append(task)
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    '''Delete tasks'''

    tasks.pop(task_id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
