// Setup: jQuery 3.3.1
(function ($) {
    "use strict";

    // Document ready
    $(document).ready(function () {
        var isLocked = false; // Flag to track if paths are locked

        // Add event listener to the confirm button
        $('#confirm-button').on('click', function () {
            isLocked = true;
            console.log('Paths are locked');
        });

        // Loop through each path
        $("path[id^=\"basic_\"]").each(function (i, e) {
            addEvent($(e).attr('id'));
        });

        // Add event listener
        function addEvent(id, relationId) {
            // Change opacity
            var _obj = $('#' + id);
            $('#basic-wrapper').css({ 'opacity': '1' });
            _obj.attr({ 'fill': 'rgba(228, 115, 7, 0)', 'stroke': 'rgba(250, 250, 250, 1)', 'cursor': 'default' });

            // Change cursor
            if (basic_config[id]['active'] === true) {
                _obj.attr({ 'cursor': 'pointer' });

                var initialColor = 'rgba(228, 115, 7, 0)'; // Initial fill color
                var isClicked = false; // Flag to track if element is clicked

                // Handle Hover event
                _obj.on('mouseenter', function () {
                    if (!isClicked && !isLocked) {
                        $('#tip-basic').show().html(basic_config[id]['hover']);
                        _obj.css({ 'fill': 'rgba(228, 115, 7, 0.3)' });
                    }
                }).on('mouseleave', function () {
                    if (!isClicked && !isLocked) {
                        $('#tip-basic').hide();
                        _obj.css({ 'fill': initialColor });
                    }
                });

                // Move tooltip
                _obj.on('mousemove', function (e) {
                    if (!isClicked && !isLocked) {
                        let x = e.pageX + 10, y = e.pageY + 15;
                        let $abasic = $('#tip-basic');
                        $abasic.css({ 'left': x, 'top': y });
                    }
                });

                // Handle Click event
                _obj.on('click', function () {
                    if (!isLocked) {
                        console.log('Clicked on ' + id);
                        var fillColor = _obj.css('fill');

                        if (fillColor === 'rgba(228, 115, 7, 0.3)') {
                            _obj.css('fill', 'rgba(228, 115, 7, 0.9)');
                            initialColor = 'rgba(228, 115, 7, 0.9)'; // Update initial color
                        } else if (fillColor === 'rgba(228, 115, 7, 0.9)') {
                            _obj.css('fill', 'rgba(228, 115, 7, 0)');
                            initialColor = 'rgba(228, 115, 7, 0)'; // Update initial color
                        }

                        isClicked = !isClicked; // Set the flag to true or false after click
                    }
                });
            }
        }
    });
})(jQuery);
