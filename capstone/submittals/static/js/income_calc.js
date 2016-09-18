/**
 * Created by Dizz on 9/15/16.
 */
'use strict';

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
            },
            error: function (rsp) {
                console.log(rsp);
            }
    })

    });