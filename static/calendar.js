var d = new Date();
var todayNum = d.getDate();
var monthNum = d.getMonth();

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