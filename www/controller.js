// This file help us in connecting backend with front end like whenever we want to display any message on the frontend page that is the python will call some functions of js and vice versa


$(document).ready(function () {
    // Display Speak Message
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {
        $(".siri-message li:first").text(message);
        $('.siri-message').textillate('start');

    }

    // Display hood
    eel.expose(ShowHood)
    function ShowHood() {
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
    }
});