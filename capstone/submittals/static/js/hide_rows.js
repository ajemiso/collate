/*
 * Created by Dizz on 9/5/16.
 */

// dashboard page

$('.submittal-list').hide();

$( document ).ready(function () {

    $('.submittal-list').fadeIn();

});


// submittal page


$('.submittal-list').hide();
$('.b2').hide();


$('.submittal-list').slideDown();



$('#show-b2').click(function(evt) {
    $('.b2').slideToggle();

});




