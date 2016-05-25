$(function() {
    $('.button').click(function() {
        var ClubName = $('#clubName').val();
        var Gmail = $('#email').val();
	var Name = $('#name').val();
	var Room = $('#room').val();
	var Date = $('#date').val();
        $.ajax({
            url: '/set_functions',
	    data: {club: ClubName, email: Gmail, name: Name, room: Room, date: Data},
            type: 'POST',
            }
        });
    });
});
