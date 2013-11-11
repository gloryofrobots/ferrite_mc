 $(document).ready(function() {
      $( ".categories_header" ).click(function() {
      $(this).parent().children( ".categories_list").toggle( 300 );
  });
});