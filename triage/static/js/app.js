// Setup: jQuery 3.3.1
(function ($) {
    "use strict";

    // Document ready
    $(document).ready(function () {
        var isLocked = false; // Flag to track if paths are locked

        // Loop through each path
        $("path[id^=\"basic_\"]").each(function (i, e) {
            addEvent($(e).attr('id'));
        });

        // Add event listener
        function addEvent(id, relationId) {
            // Change opacity
            var _obj = $('#' + id);
            $('#basic-wrapper').css({ 'opacity': '1' });

            // Get selected paths from local storage
            var selectedPaths = JSON.parse(localStorage.getItem('selectedPaths'));

            // Check if the current path is selected
            if (selectedPaths && selectedPaths.includes(id)) {
                _obj.attr({ 'fill': 'rgba(223,52,98, 1)', 'stroke': 'rgba(250, 250, 250, 1)', 'cursor': 'default' });
            } else {
                _obj.attr({ 'fill': 'rgba(223,52,98, 0)', 'stroke': 'rgba(250, 250, 250, 1)', 'cursor': 'default' });
            }
        }

    });
})(jQuery);