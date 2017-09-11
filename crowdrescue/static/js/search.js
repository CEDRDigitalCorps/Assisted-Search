$(function() {
    var url = $("#search-form").attr("action");
    var query_running = false;

    function reqListener() {
        $("#results").html(this.responseText);
        query_running = false;
    }

    function runQuery() {
        if (query_running === false) {
            query_running = true;
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
        }
    }

    $.fn.extend({
        donetyping: function(callback, timeout){
            timeout = timeout || 1e3; // 1 second default timeout
            var timeoutReference,
                doneTyping = function(el){
                    if (!timeoutReference) return;
                    timeoutReference = null;
                    callback.call(el);
                };
            return this.each(function(i,el){
                var $el = $(el);
                // Chrome Fix (Use keyup over keypress to detect backspace)
                // thank you @palerdot
                $el.is(':input') && $el.on('keyup keypress paste',function(e){
                    // This catches the backspace button in chrome, but also prevents
                    // the event from triggering too preemptively. Without this line,
                    // using tab/shift+tab will make the focused element fire the callback.
                    if (e.type=='keyup' && e.keyCode!=8) return;

                    // Check if timeout has been set. If it has, "reset" the clock and
                    // start over again.
                    if (timeoutReference) clearTimeout(timeoutReference);
                    timeoutReference = setTimeout(function(){
                        // if we made it here, our timeout has elapsed. Fire the
                        // callback
                        doneTyping(el);
                    }, timeout);
                }).on('blur',function(){
                    // If we can, fire the event since we're leaving the field
                    doneTyping(el);
                });
            });
        }
    });

    $("#query").donetyping(function() {
        runQuery();
    });
});
