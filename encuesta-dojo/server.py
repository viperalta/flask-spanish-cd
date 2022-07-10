from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "secreto"

@app.route("/")
def raiz():
    return render_template("index.html")

@app.route("/process",methods=['POST'])
def process():
    session['info']=request.form
    print(request.form)
    return redirect("/result")

@app.route("/result")
def result():
    return render_template("result.html",info=session['info'])

if(__name__) == '__main__':
    app.run(debug=True)