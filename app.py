 
from flask import Flask, render_template, request, redirect, url_for, session
import TMP
app = Flask(__name__)
TMP.checkGenerate("1")
print("run?")

#home route, subject to change what it loads
@app.route("/", methods = ["GET", "POST"])
def start():
    print(session)
    if  session != {}:
        print("the court is in session")
        Username = session['username']
        return render_template("home.html", Username = Username)
    else:
        print("the court is not in session")
        return render_template("home.html")

#route to register a user
@app.route("/register", methods = ["GET","POST"])
def register():
    print("reg.1")
    print(request.method)
    if request.method == "POST":
        print("reg.2")
        if str(request.form["button"]) == "Register":
            print("reg.2.1")
            email = str(request.form["uemail"])
            name = str(request.form["uname"])
            cname = str(request.form["clubname"])
            password1 = str(request.form["password1"])
            passwordcheck = str(request.form["passwordcheck"])
            if password1 == passwordcheck:
                print("reg.2.1.1")
                print(email +","+name+","+cname+","+password1+","+passwordcheck)
                if (TMP.register(email,name,cname,password1)):
                    print("reg.2.1.1.1")
                    session["username"] = email
                    #return render_template("register.html", text = "yay")
                
                    return redirect(url_for('start'))
                else:
                    print("reg.2.1.1.2")
                    return render_template("register.html", text = "The email is already taken")
            else:
                print("reg.2.1.2")
                return render_template("register.html", text = "Passwords do not match")
        else:
            print("reg.2.2")
            return redirect(url_for('start'))
    else:
        print("reg.3")
        return render_template("register.html")

    
#route to login, subject to change
@app.route("/login", methods = ["GET","POST"])
def login():
    print("log.1")
    if request.method == "POST":
        print("log.2")
        if str(request.form["button"]) == "Login":
            print("log.2.1")
            email = str(request.form["umail"])
            password = str(request.form["password"])
            print(email)
            print(password)
            if(TMP.login(email,password)):
                print("log.2.1.1")
                session["username"] = email
                #return render_template("login.html", text = "yay")
                return redirect(url_for('start'))
            else:
                print("log.2.1.2")
                return render_template("login.html", text = "Email/Password do not match")
    else:
        print("log.3")
        return render_template("login.html")

#route to show person reservations
@app.route("/reservations", methods = ["GET","POST"])
def reservations():
    if session != {}:
            email = session['username']
            reservations = TMP.findReservations(email)
            return render_template("reservations.html", reservations = reservations)
    else:
        return redirect(url_for('start'))
@app.route("/reservations/<res_id>", methods = ["GET", "POST"])
def delete_res(res_id):
    if session != {}:
        TMP.delRes(res_id)
        return redirect(url_for('reservations'))
    else:
        return redirect(url_for('start'))

    

@app.route("/logout", methods = ["GET", "POST"])
def logout():
    session.clear()
    return redirect(url_for('start'))

    
#overall route to pass something to backend from front without reloading page
@app.route("/get_functions", methods = ["GET","POST"])
def get_res():
    return TMP.getReservations();

#overall route to change something backend without reloading page
@app.route("/set_functions", methods = ["GET"])
def set_res():
    clubt = request.args.get("club");
    emailt = request.args.get("email");
    namet =request.args.get("name");
    roomt = request.args.get("room");
    datet = request.args.get("date");
    print clubt;
    print emailt;
    print namet;
    print roomt;
    print datet;
    if(TMP.addReservation(clubt, emailt, namet, roomt, datet, "3:35", "4;30")):
        print(TMP.getReservations());
        return "true"
    else:
        return "false"


    print(session)
print(TMP.getReservations());

if __name__ == "__main__":
    app.secret_key= 'asidh19201o231l2k3j'
    app.debug = True;
    app.run(host="0.0.0.0", port=8000)
