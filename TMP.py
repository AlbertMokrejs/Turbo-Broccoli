import sqlite3, os.path
import base64
import marshal

#Checks if there is a database. Makes one if there isn't.
#Updates if VERSION doesn't match the current version.
#
def checkGenerate(version):
   #Checks if there is a database file.
   x = os.path.isfile("Calendar.db")
   if x:
      connect = sqlite3.connect("Calendar.db")
      curs = connect.cursor()
      q = """SELECT * FROM version;"""
      result = curs.execute(q)
      for r in result:
         if r[0] != version:
            print "INVALID VERSION. \n WIPING AND UPDATING."
            x = False
            os.remove("Calendar.db")
   if not x:
      #Makes tables.
      connect = sqlite3.connect("Calendar.db")
      curs = connect.cursor()
      List = [["testTable","field1","TEXT","field2","TEXT"],["testTable2","a","REAL","b","TEXT","c","TEXT","d","TEXT"],["version","v","TEXT"]]
      for q in List:
         makeTable(q[0],q[1:])
         insertValue("version",version)
      print "VERSION UP TO DATE"

def makeTable(name, arg):
   conn = sqlite3.connect("Calendar.db")
   c = conn.cursor()
   q = """CREATE TABLE %s(%s)""" % (name, "".join(str([x for x in arg])[1::][::-1][1::][::-1].split("'")))
   c.execute(q)
   conn.commit()
      
def insertValue(name, arg):
   conn = sqlite3.connect("Calendar.db")
   c = conn.cursor()
   q = """insert into %s values (%s);""" % (name, str([ str(x) for x in arg])[1::][::-1][1::][::-1])
   c.execute(q)
   conn.commit()

def findMatching(name, arg):
   conn = sqlite3.connect("Calendar.db")
   c = conn.cursor()
   q = """SELECT * FROM %s %s""" % (name, "".join("".join(str(["WHERE %s.%s = %s," % (name, x[0], x[1]) for x in arg])[1::][::-1][1::][::-1].split(", ")).split("'"))[::-1][1::][::-1] + ";")
   result = c.execute(q)
   return [r for r in result]
    
def test():
   checkGenerate("version0")
   insertValue("testTable",["a","b"])
   insertValue("testTable2",["1","2","3","b"])
   insertValue("testTable2",["2","3","4","b"])
   findMatching("testTable",["field1","a"])
