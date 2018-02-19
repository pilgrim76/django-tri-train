
$(function() {
    $('#btnCallProc1').click(function() {
        console.log("$('#btnCallProc1').click(function() - This is working so far");
        $.ajax({
            url: '/callProc1',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});

