import calendar
import string
import datetime

now = datetime.datetime.now()


#returns html code for the month of a given year. months start at january = 1
def tableHTML(year, month):
    mycal = calendar.HTMLCalendar(calendar.SUNDAY)
    #this is a string
    x = mycal.formatmonth(year,month)
    #print x
    #now its a list
    c = x.split("\n")
    #print c
    f = len(c)
    #print(f)
    c = c[2:len(c)-2]
    #print c
    str = "\n".join(c)
    return str

print(tableHTML(now.year, now.month))

