/**
 * Created by Dizz on 9/28/16. Contact Member Javascipt functions
 */

// change phone number(s) shown in contact field on keyUp

$('#b1_phone_number').keyup(function(evt) {
    $('#b1_phone_number_value').text(evt.target.value);

});

$('#b2_phone_number').keyup(function(evt) {
    $('#b2_phone_number_value').text(evt.target.value);

});

// send SMS message

$('#sms-btn').click(function(evt) {

    var $loan_number = $('#loan_number_field').val();
    var $b1_phone_number = $('#b1_phone_number').val();
    var $b2_phone_number = $('#b2_phone_number').val();
    var $sms_message = $('#sms_message').val();

    $data = {'loan_number': $loan_number, 'sender': '+14243512633', 'recipients': [$b1_phone_number, $b2_phone_number],
             'sms_message': $sms_message};

    $.ajax({
        url: '/sms/',
        data: $data,
        type: 'POST',
        success: function(rsp) {
            console.log(rsp);
        },
        error: function(rsp) {
            console.log(rsp);
        }
    });


});
