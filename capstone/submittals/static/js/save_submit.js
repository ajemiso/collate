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

/* Load submittal -- ***ADD BUTTON NEXT TO LOAN NUMBER FIELD TO RETRIEVE DATA***

$('#loan_number_form').submit(function(event) {
		var data = { 'loan_number': $('#loan_number_field').value() }

    $.ajax({
        url: "/load_loan_number/",
        type: 'POST',
        data: data,
        success: function (rsp) {
            console.log(rsp);
        },
        error: function (rsp) {
            console.log(rsp);
        }

    });

}); */

