$(document).ready(function () {
    // display speak message 
    eel.expose(DisplayMessage);
    function DisplayMessage(message) {
        $(".sirimessage li:first").text(message);
        $('.siri-message').textillate('start');
    }
    
});

