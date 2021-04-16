from flask import Flask
app = Flask(__name__)

@app.route("/") 
def index():
    return render_template("index.html")


@app.route("/greet", methods=["POST"])
def greet():
    return render_template("greet.html", name=request.form.get("name", "world"))

 