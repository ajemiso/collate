/**
 * Created by Dizz on 9/19/16.
 */

// DELETE submittal from dashboard

$('.delete-submit').click(function(event) {

        var $id = $(event.target).attr('id');

        $.ajax({
            url: "/dizz/submittals/api/submits/" + $id + "/",
            type: 'DELETE',
            success: function (rsp) {
                var $id = $(event.target).attr('id');
                $('#item-' + $id).fadeOut(200).slideUp(200);
                $('.message-bar').slideDown(300).delay(1500).slideUp(300);
            },
            error: function (rsp) {
                console.log(rsp)
            }

        })

});




