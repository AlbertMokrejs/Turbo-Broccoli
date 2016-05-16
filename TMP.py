import sqlite3, os.path
import base64
import marshal
import json


def checkGenerate(version):
   if not os.path.isfile("Calendar.db"):
      connect = sqlite3.connect("Calendar.db")
      curs = connect.cursor()
      TableList = [["Reservations","club TEXT","email TEXT","name TEXT","room REAL","date TEXT","timeS TEXT","timeE TEXT", "UID REAL"],["Users","user TEXT","email TEXT","password TEXT","reservations BLOB","UID REAL"],["version","v TEXT"]]
      for q in TableList:
         makeTable(q[0],q[1:])
      insertValue("version",[version])
      print "VERSION UP TO DATE."
   if os.path.isfile("Calendar.db"):
      try:
         result = runSQL(True, """SELECT * FROM version;""")
         for r in result:
            if r[0] != version:
               print "INVALID VERSION. \n WIPING AND UPDATING."
               x = False
               os.rename("Calendar.db","Archive.db")
               checkGenerate(version)
      except:
         pass
   
         
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
   
def addReservation(club,email,name,room,date,timeS,timeE):
   isTaken = len(findMatching("Reservations",{"date":date, "room":room})) > 0
   if not isTaken:
      pushReservation(club,email,name,room,date,timeS,timeE,0)
      return True
   return False

def pushReservation(club,email,name,room,date,timeS,timeE,UID):
   insertValue("Reservations", [club,email,name,room,date,timeS,timeE,UID])


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
   q = """SELECT * FROM %s """ % (name)
   for x in arg.keys():
      q += "WHERE %s.%s = %s," % (name, x, arg[x])
   q = q[::-1][1::][::-1] + ";"
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


   
