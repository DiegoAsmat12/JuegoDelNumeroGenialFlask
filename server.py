from flask import Flask, render_template,request, redirect,session
import random
app = Flask(__name__)

app.secret_key="numero_secreto"

@app.route("/", methods=["GET"])
def showGame():
    if 'random' not in session:
        session["random"] = random.randint(1,100)

    if 'contador-intentos' not in session:
        session['contador-intentos']=0
    return render_template('index.html')

@app.route("/guess", methods = ["POST"])
def guessNumber():
    guess = int(request.form["guess-number"])
    if(session["guess-message"]=="You Guessed it!"):
        return redirect("/")
    if(guess-session["random"]>0):
        session["guess-message"]="Too High"
    elif(guess-session["random"]<0):
        session["guess-message"]="Too Low"
    else:
        session["guess-message"]="You Guessed it!"
    return redirect("/")

@app.route("/reset",methods=["POST"])
def resetGame():
    session.clear()
    return redirect("/")
if(__name__=="__main__"):
    app.run(debug=True)
