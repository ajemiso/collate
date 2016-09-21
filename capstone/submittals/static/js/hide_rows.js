/*
 * Created by Dizz on 9/5/16.
 */

// dashboard page
'use strict';


$('.drop-down').hide().slideToggle();

$('.submittal-list').hide().fadeIn(700);

// get length of table
var $table_length = $('.submittal-list tr').length;
















// submittal page

$('.title').hide().slideToggle(500);


$('.fade-in-body').hide().fadeIn(700);

$('.b2').hide();

// if box was already checked, re-check it & show b2 fields

if (localStorage.boxchecked === 'y') {
    $('#show-b2').prop('checked', true)
    $('.b2').slideDown();

}

// changes checkbox "checked" value

$('#show-b2').change(function(event) {
    if (this.checked) {
        localStorage.boxchecked = 'y';
        $('.b2').slideDown();
    } else {
        localStorage.boxchecked = 'n';
        $('.b2').slideUp();
    }


});


/* $('#show-b2').click(function(evt) {
    $('.b2').slideToggle();

}); */




