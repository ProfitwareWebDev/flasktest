$(function () {
  $("h1").click(function () {
    $(this).hide();
  });

  var counter = 0;

  $("form").submit(function () {

    $.post("/counter", {"counter": counter}, function (data) {
      counter = data.counter;
      $("span.counter").text(counter);
    });

    return false;
  });

});
