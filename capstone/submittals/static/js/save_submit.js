'use strict';

/**
 * Created by Dizz on 9/5/16.
 */

// set values on page load
$("#loader").hide();

$(document).ajaxStart(function() {
    $("#loader").show(500);
});

$(document).ajaxComplete(function(){
    $("#loader").hide();

    });

// Save submittal function

function saveSubmit() {
    var $data = $('input, textarea, select').serialize();

    $.ajax({
        url: "/save/",
        type: 'POST',
        data: $data,
        success: function (rsp) {
            console.log(rsp);
            $('.message-bar').slideDown(300).delay(1500).slideUp(300);
        },
        error: function (rsp) {
            console.log(rsp);
        }

    });

}

// Save submittal event binding

$('.save-btn').click(function(event) {

    saveSubmit();

});



