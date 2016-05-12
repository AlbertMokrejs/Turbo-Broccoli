import sqlite3, os.path
import base64
import marshal
import json


def checkGenerate(version):
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
            os.rename("Calendar.db","Archive.db")
   if not x:
      connect = sqlite3.connect("Calendar.db")
      curs = connect.cursor()
      TableList = [["testTable","field1","TEXT","field2","TEXT"],["testTable2","a","REAL","b","TEXT","c","TEXT","d","TEXT"],["version","v","TEXT"]]
      for q in TableList:
         makeTable(q[0],q[1:])
      insertValue("version",version)
      print "VERSION UP TO DATE"

def makeTable(name, arg):
   conn = sqlite3.connect("Calendar.db")
   c = conn.cursor()
   q = """CREATE TABLE %s(%s)""" % (name, "".join(str([x for x in arg])[1::][::-1][1::][::-1].split("'")))
   c.execute(q)
   conn.commit()
   
def makeTableJSON(a):
   result = json.loads(a)
   makeTable(result["name"],result["format"])

      
def insertValue(name, arg):
   conn = sqlite3.connect("Calendar.db")
   c = conn.cursor()
   q = """insert into %s values (%s);""" % (name, str([ str(x) for x in arg])[1::][::-1][1::][::-1])
   c.execute(q)
   conn.commit()
   
def insertValueJSON(a):
   result = json.loads(a)
   insertValue(result["name"],result["data"])


def findMatching(name, arg):
   conn = sqlite3.connect("Calendar.db")
   c = conn.cursor()
   q = """SELECT * FROM %s %s""" % (name, "".join("".join(str(["WHERE %s.%s = %s," % (name, x[0], x[1]) for x in arg])[1::][::-1][1::][::-1].split(", ")).split("'"))[::-1][1::][::-1] + ";")
   result = c.execute(q)
   return [r for r in result]
   
def findMatchingJSON(a):
   result = json.loads(a)
   return findMatching(result["name"],result["data"])
    
def test():
   checkGenerate("version0")
   insertValue("testTable",["a","b"])
   insertValue("testTable2",[1,"2","3","b"])
   insertValue("testTable2",[2,"3","4","b"])
   print findMatching("testTable",["field1","a"])
   print findMatching("testTable2",["a","1"])
   print findMatching("testTable2",["d","b"])
   
