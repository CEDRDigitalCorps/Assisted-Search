$(function() {
    var url = $("#search-form").attr("action");
    $("#query").on("keyup", function() {
        $("#results").html('<div id="spinner"><i class="fa fa-spinner fa-spin fa-2x" aria-hidden="true"></i></div>');
        $.ajax({
            url: url,
            method: "POST",
            data: $("#search-form").serialize()
        }).done(function(data) {
            $("#results").html(data);
        });
    });
});
