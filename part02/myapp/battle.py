from flask import Flask,request,render_template
app = Flask(__name__)

players = ["勇者","戦士","魔法使い"]

@app.route("/")
def show():
    message = "新たなモンスターが現れた"
    return render_template("battle.html",message = message,players=players)

@app.route("/result",methods=["POST"])
def result():
    if request.method == "POST":
        name = request.form["name"]
        message = name + "はモンスターと戦った！"
    return render_template("battle.html",message=message,players = players)
