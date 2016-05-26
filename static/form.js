$(function() {
    $('#theButton').click(function() {
        var ClubName = $('#clubName').val();
        var Gmail = $('#email').val();
	    var Name = $('#name').val();
	    var Room = $('#room').val();
	    var theDate = $('#date').val();
        console.log($('form').serialize());
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
    });
});
