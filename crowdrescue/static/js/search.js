$(function() {
    var Search = function(qs) {
        $.ajax({
            url: url,
            method: "POST",
            data: {
                "query": qs
            }
        }).done(function(data) {
            $("#results").html(data);
        });
    };

    var url = $("#search-form").attr("action");
    $("#query").on("keyup", function() {
        var qs = $(this).val();
        Search(qs);
    });
});
