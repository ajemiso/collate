/*
 * Created by Dizz on 9/5/16.
 */

// dashboard page

$('.submittal-list').hide();

$( document ).ready(function () {

    $('.submittal-list').fadeIn();

});


// submittal page

$('.first-row').hide();
$('.section').hide();
$('.b2').hide();

$('.first-row').fadeIn();
$('.section').fadeIn(600);


$('#show-b2').click(function(evt) {
    $('.b2').slideToggle();

});




