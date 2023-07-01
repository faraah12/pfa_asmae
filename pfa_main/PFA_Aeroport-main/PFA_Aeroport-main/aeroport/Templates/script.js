$(document).ready(function() {
    $('#book-flight-button').click(function(event) {
      event.preventDefault(); // Prevent the default form submission
  
      // Collect the form data
      var departure = $('#departure').val();
      var destination = $('#destination').val();
      var date = $('#date').val();
      var airline = $('#airline').val();
  
      // Create the payload object
      var data = {
        departure: departure,
        destination: destination,
        date: date,
        airline: airline
      };
  
      // Send the AJAX request
      $.ajax({
        url: '/flight/book/', // Update with the appropriate URL mapping
        type: 'POST',
        data: data,
        success: function(response) {
          // Handle the successful booking response
          $('#confirmation-message').text(response.message);
          $('#confirmation-message').show();
        },
        error: function(xhr, errmsg, err) {
          // Handle the error response
          console.log(xhr.status + ': ' + xhr.responseText);
        }
      });
    });
  });
  