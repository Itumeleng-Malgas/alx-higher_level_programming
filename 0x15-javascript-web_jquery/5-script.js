$(function(){
  $('#add_item').on('click', function() {
    const newItem = $('<li>').text('Item');

    $('ul.my_list').append(newItem);
  });
});
