$(function() {
    var url = $("#search-form").attr("action");

    function reqListener() {
        $("#results").html(this.responseText);
    }

    $("#query").on("keyup", function() {
        $("#results").html('<div id="spinner"><i class="fa fa-spinner fa-spin fa-2x" aria-hidden="true"></i></div>');
        var req = new XMLHttpRequest();
        req.addEventListener("load", reqListener);
        req.open("POST", url);
        req.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        req.setRequestHeader(
            'Content-Type',
            'application/x-www-form-urlencoded'
        );
        req.send($("#search-form").serialize());
    });
});
