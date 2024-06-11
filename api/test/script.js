$(document).ready(function() {
  $("#solveBtn").click(function() {
      var a = $("#a").val();
      var b = $("#b").val();
      var c = $("#c").val();

      $.ajax({
          url: "/solve",
          type: "POST",
          contentType: "application/json",
          data: JSON.stringify({ a: a, b: b, c: c }),
          success: function(response) {
              $("#result").text(response.result);
          },
          error: function(xhr, status, error) {
              console.error("Error:", error);
          }
      });
  });
});
