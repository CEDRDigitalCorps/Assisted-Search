$(function() {
    var url = $("#search-form").attr("action");
    $("#query").on("keyup", function() {
        $.ajax({
            url: url,
            method: "POST",
            data: $("#search-form").serialize()
        }).done(function(data) {
            $("#results").html(data);
        });
    });
});
