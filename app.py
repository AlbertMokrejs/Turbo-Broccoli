from flask import Flask, render_template, request, redirect, url_for, session
import TMP
import datetime
import calendar
now = datetime.datetime.now()

app = Flask(__name__)
TMP.checkGenerate("1")
app.secret_key= 'asidh19201o231l2k3j'


month1 = {}
month2 = {}
month3 = {}
current_month = 0


#home route, subject to change what it loads
@app.route("/", methods = ["GET", "POST"])
def start():
    current_month = now.month()
    check_cal(current_month)
    session["username"] = "mli6@stuy.edu"
    print(session)
    if  session != {}:
        print("the court is in session")
        Username = session['username']
        return render_template("home.html", cal1 = month1, cal2 = month2, cal3 = month3)
    else:
        print("the court is not in session")
        return render_template("home.html", cal1 = month1, cal2 = month2, cal3 = month3)


    
#route to register a user
@app.route("/register", methods = ["GET","POST"])
def register():
    if request.method == "POST":
        if str(request.form["button"]) == "Register":
            email = str(request.form["uemail"])
            name = str(request.form["uname"])
            cname = str(request.form["clubname"])
            password1 = str(request.form["password1"])
            passwordcheck = str(request.form["passwordcheck"])
            if password1 == passwordcheck:
                if (TMP.register(email,name,cname,password1)):
                    print("1")
                    TMP.send_email(email, "Stuyvesant Club Calender Authentication", "Hello, " + name + "\nThank you for signing up to Stuyvesant's new club room reservation system.\nIf you could enter the following code to the authentication page, then you'll be all set to use the system!\nCode: " + TMP.getVerS(email)) #send the auth email here
                    return redirect("/authenticate/" + email + "")
                else:
                    print("email taken")
                    return render_template("register.html", text = "The email is already taken")
            else:
                print("passwords do not match")
                return render_template("register.html", text = "Passwords do not match")
        else:
            return redirect(url_for('start'))
    else:
        return render_template("register.html")
    
    

    
#route to authenticate a user
@app.route("/authenticate")
@app.route("/authenticate/<username>", methods = ["GET", "POST"])
def auth(username):
    if request.method == "POST":
        print("form submitted")
        print(str(request.form["authenValue"]))
        if str(request.form["authenValue"]) == TMP.getVerS(username):
            print("checking validity")
            TMP.verifty(username, str(request.form["authenValue"]))
            session["username"] = username
            return redirect(url_for('start'))
    else:
        return render_template("authentication.html", username = username)
    
            
#route to login, subject to change
@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "POST":
        if str(request.form["button"]) == "Login":
            email = str(request.form["umail"])
            password = str(request.form["password"])
            if(TMP.login(email,password)):
                session["username"] = email
                return redirect(url_for('start'))
            else:
                return render_template("login.html", text = "Email/Password do not match")
    else:
        if TMP.getisVer(str(request.form["umail"])):
            return render_template("login.html")
        else:
            return redirect("/authenticate/" + email + "")


        
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
        res_id = int(float(res_id))
        print(res_id)
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
    print(TMP.getReservations())
    return TMP.getReservations()



#overall route to change something backend without reloading page
@app.route("/set_functions", methods = ["GET"])
def set_res():
    clubt = request.args.get("club")
    emailt = request.args.get("email")
    namet =request.args.get("name")
    roomt = int(float(request.args.get("room")))
    datet = request.args.get("date")
    if(TMP.addReservation(clubt, emailt, namet, roomt, datet, "3:35", "4;30")):
        print(TMP.getReservations())
        return "true"
    else:
        return "false"


TMP.addReservation("Derry's Club", "mli6@stuy.edu", "Derry", "355", "2016/06/09", "3:35", "5:00")
TMP.addReservation("Derry's Club", "mli6@stuy.edu", "Derry", "375", "2016/06/08", "3:35", "5:00") 
TMP.addReservation("Derry's Club", "mli6@stuy.edu", "Derry", "515", "2016/10/08", "3:35", "5:00")
TMP.addReservation("Derry's Club", "mli6@stuy.edu", "Derry", "555", "2017/06/08", "3:35", "5:00")
TMP.addReservation("NotDerry's Club", "mli8@stuy.edu", "NotDerry", "755", "2016/06/09", "3:35", "5:00")


def check_cal(original_month):
    if original_month < now.month():
        current_month = now.month
        generate_cal()
        

def generate_cal():
    hold_1 = calendar.Calendar(calendar.SUNDAY).monthdayscalendar(2016,now.month)
    hold_2 = calendar.Calendar(calendar.SUNDAY).monthdayscalendar(2016,now.month + 1)
    hold_3 = calendar.Calendar(calendar.SUNDAY).monthdayscalendar(2016,now.month + 2)
    hold_res = parsed_res()
    counter = 0
    for x in range(5):
        for y in range(7):
            list1 = [[hold_1[x][y]]]
            list2 = [[hold_2[x][y]]]
            list3 = [[hold_3[x][y]]]
            for z in hold_res:
                if z[2] == counter:
                    if z[3] == now.month:
                        list1.append([z[1],z[0]])
                    elif z[3] == now.month + 1:
                        list2.append([z[1],z[0]])
                    elif z[3] == now.month + 2:
                        list3.append([z[1],z[0]])
            month1[counter] = list1
            month2[counter] = list2
            month3[counter] = list3
            counter = counter + 1

    
def parsed_res():
    list_len = len(TMP.getReservations())
    res_list = [[0 for x in range(5)] for y in range(list_len)]
    check = 0
    for x in TMP.getReservations():
        hold_club = x[0]
        hold_room = x[3]
        hold_date = x[4]
        hold_splits = hold_date.split("/")
        res_list[check][0] = hold_club
        res_list[check][1] = hold_room
        res_list[check][2] = int(hold_splits[2])
        res_list[check][3] = int(hold_splits[1])
        res_list[check][4] = hold_splits[0]
        check = check + 1

    for x in res_list:
        if x[3] > (now.month + 3):
            res_list.remove(x)
        elif x[4] > now.year:
            res_list.remove(x)
    return res_list

generate_cal()

print(month1)

print(current_month)
      
    
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
