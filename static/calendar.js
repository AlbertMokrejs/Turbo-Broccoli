var d = new Date();
var todayNum = d.getDate();
var monthNum = d.getMonth();
var thisYear = d.getYear();

function findMonth(num) {
    console.log(num);
    if (num == 0) {
	return "JANUARY";
    }
    else if (num == 1) {
	return "FEBRUARY";
    }
    else if (num == 2) {
	return "MARCH";
    }
    else if (num == 3) {
	return "APRIL";
    }
    else if (num == 4) {
	return "MAY";
    }
    else if (num == 5) {
	return "JUNE";
    }
    else if (num == 6) {
	return "JULY";
    }
    else if (num == 7) {
	return "AUGUST";
    }
    else if (num == 8) {
	return "SEPTEMBER";
    }
    else if (num == 9) {
	return "OCTOBER";
    }
    else if (num == 10) {
	return "NOVEMBER";
    }
    else if (num == 11) {
	return "DECEMBER";
    }
};

document.getElementById("mesa").caption.innerHTML = findMonth(monthNum);

/*
//find weekday of the first
function weekDay(year, month, day) {
    var offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334];
    var week   = [0,1,2,3,4,5,6];
    var afterFeb = 1;
    if (month > 2) {
	    afterFeb = 0;
    }
    var aux = year - 1700 - afterFeb;
    dayOfWeek  = 5;
    dayOfWeek += (aux + afterFeb) * 365;
    dayOfWeek += aux / 4 - aux / 100 + (aux + 100) / 400;
    dayOfWeek += offset[month - 1] + (day - 1);
    dayOfWeek %= 7;
    return week[dayOfWeek];
};

function fillCal(month) {
    //only works for 2016 right now
    var cal = [];
    for (var x = 0; x < 5; x++) {
	cal[x] = [];
	for (var y = 0; y < 7; y++) {
	    cal[x][y] = 0;
	}
    }
    //cal is a 5 row 7 column 2d array
    //months with 31 days
    if (monthNum == 0 || monthNum == 2 || monthNum == 4 || monthNum == 6 || monthNum == 7 || monthNum == 9 || monthNum == 11) { 
	i = 0; //day ctr
	while (i < 31) {
	    dayOfWeek = weekDay(thisYear,monthNum,i);	 
	    j = 0; //week ctr
	    while (dayOfweek < 7) {
		
	    }
	    i++;   
	}
    }
    //leap year
    else if (monthNum == 1 && thisYear%4 == 0) {
	i = 0;
	while (i < 29) {
	    i++;
	}
    }
    //regular february
    else if (monthNum == 1) {
	i = 0;
	while (i < 28) {
	    i++;
	}
    }
    //30 days
    else {
	i = 0;
	while (i < 30) {
	    i++;
	}
    }
    return 0;
};
*/