from flask import Flask,request,render_template
app = Flask(__name__)

@app.route("/")
def show():
    message = "hello world"
    return render_template("form.html",message = message)

@app.route("/result",methods=["GET","POST"])
def result():
    message = "This is paiza"
    if request.method == "POST":
        airticle = request.form["article"] #formのテキストボックスのname属性に対応
        name = request.form["name"]
    else:
        airticle = request.args.get("article")#データを取り出そう方法がPOSTと異なるので分離
        name = request.args.get("name")
    return render_template("form.html",message=message,article=airticle,name=name)
