from flask import Flask,render_template

app=Flask(__name__)

player = "勇者"

#メニューを表示
@app.route("/")
def menu():
    return render_template("menu.html",player=player)

@app.route("/walk")
def walk():
    message = player + "は荒野を歩いていた"
    return render_template("action.html",player=player,message=message)

@app.route("/attack")
def fight():
    message = player + "は立派に戦い抜いた"
    return render_template("action.html",player=player,message=message)
