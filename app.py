 
from flask import Flask, render_template, request, redirect, url_for, session
import TMP
app = Flask(__name__)
TMP.checkGenerate("0")
print("run?")

#home route, subject to change what it loads
@app.route("/")
def start():
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
                return redirect(url_for('start', email=email))
            else:
                print("log.2.1.2")
                return render_template("login.html", text = "Email/Password do not match")
    else:
        print("log.3")
        return render_template("login.html")
    


#overall route to pass something to backend from front without reloading page
@app.route("/get_functions")
def get_functions():
    return null;

#overall route to change something backend without reloading page
@app.route("/set_functions")
def set_functions():
    return null;



TMP.addReservation("club1","club1@gmail.com","CLUB1","111","2016/7/15","3:40","4:00")
TMP.addReservation("club2","club2@gmail.com","CLUB2","112","2016/8/15","3:40","4:00")
TMP.addReservation("club3","club3@gmail.com","CLUB3","113","2015/7/15","3:40","4:00")
print(TMP.getReservations())

if __name__ == "__main__":
    app.secret_key= 'asidh19201o231l2k3j'
    app.debug = True;
    app.run(host="0.0.0.0", port=8000)
