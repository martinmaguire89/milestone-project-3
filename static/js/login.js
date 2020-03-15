$('.message a').click(function(){
   $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
});

$('.datepicker').pickadate({
// Escape any “rule” characters with an exclamation mark (!).
format: 'You selecte!d: dddd, dd mmm, yyyy',
formatSubmit: 'yyyy/mm/dd',
hiddenPrefix: 'prefix__',
hiddenSuffix: '__suffix'
})