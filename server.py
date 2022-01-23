from flask import Flask, render_template,request, redirect,session
import random
app = Flask(__name__)

app.secret_key="numero_secreto"

winners = []

@app.route("/", methods=["GET"])
def showGame():
    if 'random' not in session:
        session["random"] = 12
    if 'contador-intentos' not in session:
        session['contador-intentos']=0
    return render_template('index.html')

@app.route("/guess", methods = ["POST"])
def guessNumber():
    if(request.form["guess-number"].isdigit()):
        guess = int(request.form["guess-number"])
        if('guess-message' in session 
            and session["guess-message"]=="You Guessed it!"):
            return redirect("/")
        if 'contador-intentos' in session:
            if(session['contador-intentos']>=5):
                return redirect("/")
            session['contador-intentos']+=1
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

@app.route("/register", methods=["POST"])
def registerUser():
    user = request.form["username"]
    winners.append({"username":user,"attempts":session['contador-intentos']})
    session.clear()
    return redirect("/winners")

@app.route("/winners",methods=["GET"])
def showWinners():
    return render_template('winnerTable.html', winners=winners)

if(__name__=="__main__"):
    app.run(debug=True)
