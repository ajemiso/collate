/**
 * Created by Dizz on 9/15/16.
 */
'use strict';

$('.calc-btn').click(function(event) {

    var $data = {
        'b1_employer_name': $('#b1_employer_name').value(),
        'b1_hire_date': $('#b1_hire_date').value(),
        'b1_period_end_date': $('#b1_period_end_date').value(),
        'b1_income_amount': $('#b1_income_amount').value(),
        'b1_pay_frequency': $('#b1_pay_frequency').value(),

        'b2_employer_name': $('#b2_employer_name').value(),
        'b2_hire_date': $('#b2_hire_date').value(),
        'b2_period_end_date': $('#b2_period_end_date').value(),
        'b2_income_amount': $('#b2_income_amount').value(),
        'b2_pay_frequency': $('#b2_pay_frequency').value(),
        }

    $.ajax({

        url: '/calculate/',
        type: 'POST',
        data: $data,
        success: function (rsp) {
                console.log(rsp);
            },
            error: function (rsp) {
                console.log(rsp);
            }
    })

    });