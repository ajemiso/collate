/**
 * Created by Dizz on 9/21/16.
 */



$('#search-box').keyup(function () {

    var value = $(this).val();

    $("table tr").each(function(index) {
        if (index != 0) {

            $row = $(this);

            var id = $row.find("td:first").text();

            if (id.indexOf(value) != 0) {
                $(this).hide();
            }
            else {
                $(this).show();
            }
        }
    });

});
