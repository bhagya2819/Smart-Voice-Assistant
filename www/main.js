// $(document).ready(function() {
// 	$('.text').textillate({
//         loop: true,
//         sync: true,
//         in: {
//             effect: "bounceIn",
//         },
//         out: {
//             effect: "bounceOut",
//         },

//     });


//     var siriWave = new SiriWave({
//         container: document.getElementById("siri-container"),
//         width: 800,
//         height: 200,
//         style: "ios9",
//         amplitude: "1",
//         speed: "0.30",
//         autostart: true
//       });

//       $('.siri-message').textillate({
//         loop: true,
//         sync: true,
//         in: {
//             effect: "fadeInUp",
//             sync: true,
//         },
//         out: {
//             effect: "fadeOutUp",
//             sync: true,
//         },

//     });


    

//     $("#MicBtn").click(function() {
//         $("#Oval").attr("hidden", true);
//         $("#SiriWave").attr("hidden", false);
//         // eel.playClickSound();
//         eel.allCommands()();
//     });
// });


$(document).ready(function() {
    // Text animation and wave
    $('.text').textillate({
        loop: true,
        sync: true,
        in: { effect: "bounceIn" },
        out: { effect: "bounceOut" },
    });

    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true
    });

    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: { effect: "fadeInUp", sync: true },
        out: { effect: "fadeOutUp", sync: true },
    });

    // Prevent page reload
    $("#MicBtn").click(function(event) {
        event.preventDefault();  // Prevent page refresh
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands()();  // Run Eel function
    });
});

// eel.expose(displayNewsInFrontend);
// function displayNewsInFrontend(headlines) {
//     let newsBox = $("#news-headlines");
//     newsBox.empty(); // clear previous news

//     if (headlines.length > 0) {
//         headlines.forEach(headline => {
//             newsBox.append(`<p><i class="bi bi-dot"></i> ${headline}</p>`);
//         });
//     } else {
//         newsBox.append("<p>No news found.</p>");
//     }

//     // Show the news section if it was hidden
//     $("#news-box").show();

// }

eel.expose(displayNewsInFrontend);
function displayNewsInFrontend(news) {
    console.log(news);  // Log the news to see if it's correctly received
    $('#news-box').html(news);  // Update the content of the news box
    $('#news-box').show();  // Make sure the news box is visible
    $('#SiriWave').hide(); // Hide the previous section if needed
}
