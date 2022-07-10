from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "secreto"

@app.route("/")
def raiz():
    #counter = session['counter']
    #print(session['counter'])
    
    if 'counter' not in session:
        print("no hay contador")
        counter=1
        session['counter']=1
    else:
        counter=session['counter']+1
        session['counter']=counter
    return render_template("index.html",counter=counter)

@app.route("/destroy_session")
def destroy():
    session.clear()
    return redirect("/")

@app.route("/incrementar_en_dos")
def incrDos():
    session['counter']=session['counter']+1
    return redirect("/")



if(__name__) == '__main__':
    app.run(debug=True)