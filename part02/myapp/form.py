from flask import Flask,request,render_template
app = Flask(__name__)

@app.route("/")
def show():
    message = "hello world"
    return render_template("form.html",message = message)

@app.route("/result",methods=["POST"])
def result():
    message = "This is paiza"
    airticle = request.form["article"] #formのテキストボックスのname属性に対応
    name = request.form["name"]
    return render_template("form.html",message=message,article=airticle,name=name)
