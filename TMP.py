import sqlite3, os.path
import base64
import marshal
import json
import time 
import random 

global UID
#Inputs: String Version
#checks version of the database. 
#Archives databases if the version is wrong, and makes a new database if one doesn't exist. 
#TableList sets the format.
def checkGenerate(version):
   if not os.path.isfile("Calendar.db"):
      connect = sqlite3.connect("Calendar.db")
      curs = connect.cursor()
      TableList = [["Reservations","club TEXT","email TEXT","name TEXT","room REAL","date TEXT","timeS TEXT","timeE TEXT", "UID REAL"],["Users","user TEXT","email TEXT","password TEXT","reservations BLOB","UID REAL","Club TEXT","verS TEXT", "isver BOOL"],["version","v TEXT"]]
      for q in TableList: 
         makeTable(q[0],q[1:]) 
      insertValue("version",[version])
      print "VERSION UP TO DATE." 
   try: 
      result = runSQL(True, """SELECT * FROM version;""") 
      for r in result: 
         if r[0] != version:
            os.rename("Calendar.db","Archive.db") 
            checkGenerate(version) 
   except: 
      pass #Gonna Graduate. Seniors 2016!
   global UID
   UID = getUIDMax()

#Inputs: Bool doesReturn, string q
#runs SQL code in q
#if doesReturn, returns the output
def runSQL( doesReturn, q):
   conn = sqlite3.connect("Calendar.db")
   c = conn.cursor()
   print q
   if doesReturn:
      result = c.execute(q)
      conn.commit()
      return result
   else:
      c.execute(q)
      conn.commit()

#inputs: all strings
#makes a user account with these params if the email isn't taken
#returns if an account was made
def register(email, name, club, password):
   isTaken = len(findMatching("Users",{"email":email})) > 0
   if not isTaken:
      randstr = ""
      for x in xrange(15):
         randstr += "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"[random.randrange(len("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"))]
      insertValue("Users",[name,email,password,base64.b64encode(marshal.dumps([])),0,club,randstr,False])
      return True
   return False
   
def getVerS(email):
   return findMatching("Users",{"email":email})[0][-2]
   
def getisVer(email):
   return findMatching("Users",{"email":email})[0][-1]
   
def verifty(email,verS):
   runSQL(False, "UPDATE Users SET isVer = True WHERE email = '%s' AND verS = '%s';" % (email,verS))
   
   
def authen(email, name, club, password):
   isTaken = len(findMatching("Users",{"email":email})) > 0
   if not isTaken:
      return True
   return False   
   
#inputs: all strings
#checks if an account with this email and password exists
#returns a bool
def login(email,password):
   return findMatching("Users",{"email":email,"password":password})

def addReservation(club,email,name,room,date,timeS,timeE):
   isTaken = False
   if weekDay(date.split("/")) == 1:
      isTaken = len(findMatching("Reservations",{"date":date, "room":room})) > 0
   if weekDay(date.split("/")) == 0:
      isTaken = True
   if not isTaken:
      pushReservation(club,email,name,room,date,timeS,timeE,getUIDMax())
      return True
   return False
   
def findReservations(email):
   return findMatching("Reservations",{"email":email})

def getUIDMax():
   global UID
   try:
      UID += 1
   except:
      UID = 0
   return UID
   
def delRes(x):
   runSQL(False, "DELETE FROM Reservations WHERE Reservations.UID=%s;" % (int(x)))

def pushReservation(club,email,name,room,date,timeS,timeE,UID):
   insertValue("Reservations", [club,email,name,room,date,timeS,timeE,UID])

def getReservations():
   res = findMatching("Reservations",{})
   date = time.strftime("%Y/%m/%d").split("/")
   final = []
   print res
   for x in res:
      print x
      if int(x[4].split("/")[0]) > int(date[0]):
         final.append(x)
      elif int(x[4].split("/")[0]) == int(date[0]):
         if int(x[4].split("/")[1]) >= int(date[1]):
            final.append(x)
   counter = 0
   while counter < len(final) - 1:
      if checkDates(final[counter][4], final[counter + 1][4]):
         final[counter],final[counter + 1] = final[counter + 1],final[counter]
         counter = 0
      else:
         counter += 1
   print final
   return final
   
def checkDates(a,b):
   a = a.split("/")
   b = b.split("/")
   return a[0] > b[0] or (a[0] == b[0] and a[1] > b[1]) or (a[0] == b[0] and a[1] == b[1] and a[2] > b[2])

def makeTable(name, arg):
   runSQL(False, """CREATE TABLE %s(%s)""" % (name, "".join(str([x for x in arg])[1::][::-1][1::][::-1].split("'"))))
   
def makeTableJSON(a):
   result = json.loads(a)
   makeTable(result["name"],result["format"])

      
def insertValue(name, arg):
   runSQL(False, q = """insert into %s values (%s);""" % (name, str([ str(x) for x in arg])[1::][::-1][1::][::-1]))
   
def insertValueJSON(a):
   result = json.loads(a)
   insertValue(result["name"],result["data"])

def findMatching(name, arg):
   q = """SELECT * FROM %s""" % (name)
   print arg
   if len(arg.keys()) > 0:
      q += """ WHERE """
      for x in arg.keys():
         q += "%s.%s = '%s' AND " % (name, x, arg[x])
      q = q[::-1][4::][::-1]
   q += ";"
   print q
   result = runSQL(True, q)
   return [r for r in result]
   
def findMatchingJSON(a):
   result = json.loads(a)
   return findMatching(result["name"],result["data"])
    
 #http://stackoverflow.com/questions/9847213/which-day-of-week-given-a-date-python
def weekDay(a):
    year, month, day = int(a[0]),int(a[1]),int(a[2])
    offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    week   = [0,1,1,1,1,1,0]
    afterFeb = 1
    if month > 2: afterFeb = 0
    aux = year - 1700 - afterFeb
    dayOfWeek  = 5
    dayOfWeek += (aux + afterFeb) * 365                  
    dayOfWeek += aux / 4 - aux / 100 + (aux + 100) / 400     
    dayOfWeek += offset[month - 1] + (day - 1)               
    dayOfWeek %= 7
    return week[dayOfWeek]
   
def send_email( recipient, subject, body):
    import smtplib
    print "Starting send"
    gmail_user = "stuyclubcalendar@gmail.com"
    gmail_pwd = "clubsclubsclubs" #ORIGINAL CONTENT DO NOT STEAL (tm)
    FROM = "StuyClubs"
    TO = recipient
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    print "Trying to send"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    print "server"
    server.ehlo()
    print "ehlo?"
    server.starttls()
    print "server starting"
    server.login(gmail_user, gmail_pwd)
    print "logging in"
    server.sendmail(FROM, TO, message)
    print "sent da mail"
    server.close()
    print "close"
