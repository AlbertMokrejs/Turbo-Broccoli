import sqlite3, os.path
import base64
import marshal
import json

def checkGenerate(version):
   if not os.path.isfile("Calendar.db"): #is it a file
      connect = sqlite3.connect("Calendar.db") #make it a file
      curs = connect.cursor() #connect to it
      TableList = [["Reservations","club TEXT","email TEXT","name TEXT","room REAL","date TEXT","timeS TEXT","timeE TEXT", "UID REAL"],["Users","user TEXT","email TEXT","password TEXT","reservations BLOB","UID REAL","Club TEXT"],["version","v TEXT"]]
      for q in TableList: #iterate list
         makeTable(q[0],q[1:]) #make a table
      insertValue("version",[version]) #put a version tag
      print "VERSION UP TO DATE." #print
   if os.path.isfile("Calendar.db"): #if its a file
      try: #make an attempt
         result = runSQL(True, """SELECT * FROM version;""") #get EVERYTHING
         for r in result: #iterate EVERYTHING
            if r[0] != version: #if version tag bad
               print "INVALID VERSION. \n WIPING AND UPDATING." #fuck it, do it again
               x = False #because variables
               os.rename("Calendar.db","Archive.db") #archive the file
               checkGenerate(version) #do it again, for real this time
      except: #if attempt fucked up
         pass #don't give a shit
         
def runSQL( doesReturn, q):
   conn = sqlite3.connect("Calendar.db")
   c = conn.cursor()
   if doesReturn:
      result = c.execute(q)
      conn.commit()
      return result
   else:
      c.execute(q)
      conn.commit()

def register(email, name, club, password):
   isTaken = len(findMatching("Users",{"email":email})) > 0
   if not isTaken:
      insertValue("Users",[name,email,password,base64.b64encode(marshal.dumps([])),0,club])
      return True
   return False
   
def login(email,password):
   return findMatching("Users",{"email":email,"password":password})

def addReservation(club,email,name,room,date,timeS,timeE):
   isTaken = False
   if weekDay(date.split("/")) == 1:
      isTaken = len(findMatching("Reservations",{"date":date, "room":room})) > 0
   if not isTaken:
      pushReservation(club,email,name,room,date,timeS,timeE,0)
      return True
   return False

def pushReservation(club,email,name,room,date,timeS,timeE,UID):
   insertValue("Reservations", [club,email,name,room,date,timeS,timeE,UID])

def getReservations():
   res = findMatching("Reservations",{})
   date=time.strftime("%Y/%m/%d").split("/")
   final = []
   for x in res:
      if int(x[4].split("/")[0]) > int(date[0]):
         final.push(x)
      elif int(x[4].split("/")[0]) == int(date[0]):
         if int(x[4].split("/")[1]) >= int(date[1]):
            final.push(x)
   counter = 0
   while counter < len(final) - 1:
      if int(final[4][counter]) > int(final[4][counter + 1]):
         tmp = final[counter]
         final[counter] = final[counter + 1]
         final[counter + 1] = tmp
         counter = 0
      else:
         counter += 1
   return final

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
   q = """SELECT * FROM %s WHERE """ % (name)
   for x in arg.keys():
      q += "%s.%s = '%s' AND " % (name, x, arg[x])
   q = q[::-1][4::][::-1] + ";"
   print q
   result = runSQL(True, q)
   return [r for r in result]
   
def findMatchingJSON(a):
   result = json.loads(a)
   return findMatching(result["name"],result["data"])
    
def test():
   checkGenerate("version0")
   insertValue("testTable",["a","b"])
   insertValue("testTableB",[1,"2","3","b"])
   insertValue("testTableB",[2,"3","4","b"])
   print findMatching("testTable",{})
   print findMatching("testTable",{"field1":"'a'"})
   print findMatching("testTableB",{"a":"1"})
   print findMatching("testTableB",{"d":"'b'"})
   


#http://stackoverflow.com/questions/9847213/which-day-of-week-given-a-date-python
def weekDay(year, month, day):
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
    return dayOfWeek, week[dayOfWeek]
   
