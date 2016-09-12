/**
 * Created by Dizz on 9/5/16.
 */

function saveSubmit() {
    $data = $('input, textarea, select').serialize();

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








