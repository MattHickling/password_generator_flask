$(document).ready(function() {
  $('#password-form').submit(function(event) {
    event.preventDefault();
    var form = $(this);
    var url = form.attr('action');
    var data = {
      min_length: $('#min-length').val(),
      has_numbers: $('#has-numbers').is(':checked'),
      has_specials: $('#has-specials').is(':checked')
    };
    
    $.ajax({
      type: 'POST',
      url: '/result', // change the URL to '/result'
      data: data, // you don't need to stringify the data
      success: function(result) {
        $('#password').html(result);
    },
    
      error: function() {
        alert('Error generating password');
      }
    });
    
  });
});
