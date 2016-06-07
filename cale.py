
from datetime import date

def firstDay(d):
    #code to get number
    ret = d
    if ret <6:
        ret += 1
        return ret
    else:
        return 0

    

def fillCal(month):
    ret = ""
    cal = []
    for x in range(5):
        cal.append([])
        for n in range(7):
            cal[x].append([])
    first = 3 #this would be the weekday calculator function
    i = 1
    j = 0
    dayOfWeek = first
    if month == 0 or month == 2 or month == 4 or month == 6 or month == 7 or month == 9 or month == 11:
        limit = 31
    elif month == 1 and curYear%4 == 0:
        limit = 29
    elif month == 1:
        limit = 28
    else:
        limit = 30
    while j < 5:
        #print "\n\nnew week\n"
        while dayOfWeek < 7:                
            if i > limit + 1:
                return cal
            else:
                #print("i="+str(i))
                #print( "day="+str(dayOfWeek))
                cal[j][dayOfWeek] = i
                dayOfWeek += 1
                i += 1
        j += 1
        dayOfWeek = 0
    return cal

print(fillCal(5))
print(firstDay(0))
print(firstDay(6))
