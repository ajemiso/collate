'use strict';

/**
 * Created by Dizz on 9/5/16.
 */

// set values on page load
$("#loader").hide();
$('#zestimate').hide();

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

/*
CALCULATE SUBMIT BUTTONS
 */

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$('#calc-btn-b1').click(function(event) {

    event.preventDefault();

    var $data = {
        'borrower': '1',
        'b1_employer_name': $('#b1_employer_name').val(),
        'b1_hire_date': $('#b1_hire_date').val(),
        'b1_period_end_date': $('#b1_period_end_date').val(),
        'b1_income_amount': $('#b1_income_amount').val(),
        'b1_pay_frequency': $('#b1_pay_frequency').val()

        }

    $.ajax({

        url: '/calculate/',
        type: 'POST',
        data: $data,
        success: function (rsp) {
                $('#b1_income_output').html(rsp['b1_income_output']);
                saveSubmit();
            },
            error: function (rsp) {
                console.log(rsp);
            }
    })

    });

$('#calc-btn-b2').click(function(event) {

    event.preventDefault();

    var $data = {

        'borrower': '2',
        'b2_employer_name': $('#b2_employer_name').val(),
        'b2_hire_date': $('#b2_hire_date').val(),
        'b2_period_end_date': $('#b2_period_end_date').val(),
        'b2_income_amount': $('#b2_income_amount').val(),
        'b2_pay_frequency': $('#b2_pay_frequency').val()
        }

    $.ajax({

        url: '/calculate/',
        type: 'POST',
        data: $data,
        success: function (rsp) {
                $('#b2_income_output').html(rsp['b2_income_output']);
                saveSubmit();
            },
            error: function (rsp) {
                console.log(rsp);
            }
    })

    });


/* *** APPRAISAL VALUE SCRIPTS *** */


// setup ajax request function
function requestAppraisalValue() {
    var $data = {
        'address': $('#address').val(),
        'city': $('#city').val(),
        'state': $('#state').val(),
        'zip': $('#zip').val(),
    }

    if ($('.zestimate').is(':empty')) {

        $.ajax({
            url: '/get-zestimate/',
            type: 'POST',
            data: $data,
            success: function(rsp) {
                console.log(rsp);
                $('.zestimate').html(rsp.zestimate);
                $('#appraisal-value').val(rsp.zestimate);
                localStorage.setItem('latt', rsp.latt);
                localStorage.setItem('long', rsp.long);

                $('.zestimate').slideDown(600);
                saveSubmit();
            },
            error: function(rsp) {
                console.log(rsp);
            }

        })

    }
}

//Event listener for any address related field (calls function above)
$('#zip').change(function (evt) {
    requestAppraisalValue();
});

// Event listener for dollar signs in income textarea inputs



function addDollarValue(field) {
    var dollarValue = field.value;
    if (dollarValue[0] !== '$' && dollarValue !== '') {
        $(field).val('$' + dollarValue);
        }
}

$('#b1_income_amount').keyup(function(evt) {
    addDollarValue(this);
    });

$('#b2_income_amount').keyup(function(evt) {
    addDollarValue(this);
});