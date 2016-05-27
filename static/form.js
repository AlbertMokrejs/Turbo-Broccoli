$(function() {
    $('#theButton').click(function() {
        var ClubName = $('#clubName').val();
        var Gmail = $('#email').val();
	var Name = $('#name').val();
	var Room = $('#room').val();
	var theDate = $('#date').val();
        console.log($('form').serialize());
	/*
        $.ajax({
            url: "/set_functions",
	        data: $('form').serialize(),
            type: 'POST',
            success: function(response){
            	if (response) {
            		location.reload(true);
            	}
            	else {
            		document.getElementById('Error').innerHTML = '<span style="color: red;">Error: Requested room is not available at that date</span>';
            	}
            }
        });
	*/
	console.log(ClubName);
	console.log(Gmail);
	console.log(Name);
	console.log(Room);
	console.log(theDate);
	if (clubName != "" && Gmail != "" && Name != "" && Room != "" && theDate != ""){

	    $.get("/set_functions", {club: ClubName, email: Gmail, name: Name, room: Room, date: theDate}, function(data){
		console.log(data)
		if (data == "true"){
		    location.reload(true);
		}else{
		    document.getElementById('Error').innerHTML = '<span style="color: red;">Requested reservation is not available</span>';
		}
	    });
	}
    });
});
