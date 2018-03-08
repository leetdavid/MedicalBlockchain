$('buttons.remove.doc').on('click', function() {
  console.log('WOW');
  var userID = $(this).attr('data-id');
  $.ajax({
    method: "POST",
    url: "/patientfunction/delete",
    data: {
      "durp": userID
    },
    success: function(result) {
      location.reload();
    }
  })
});

$('buttons.approve.doc').on('click', function() {
  var userID = $(this).attr('data-id');
  $.ajax({
    method: "POST",
    url: "/patientfunction/approve",
    data: {
      "durp": userID
    },
    success: function(result) {
      location.reload();
    }
  })
});