from flask import Flask,render_template,session,redirect,request

app = Flask(__name__)
app.secret_key = "secreto"

@app.route("/")
def raiz():
    return render_template("index.html",filas=8,columnas=8,color='green')

@app.route("/<filas>")
def filas(filas):
    return render_template("index.html",filas=int(filas),columnas=8)

@app.route("/<filas>/<columnas>")
def filasycolumnas(filas,columnas):
    return render_template("index.html",filas=int(filas),columnas=int(columnas))

if(__name__) == '__main__':
    app.run(debug=True)