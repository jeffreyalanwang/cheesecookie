// change display based on logged in
$(document).ready(function($)
{
    $(".signed-in").hide();
    // if user cookie is present, show signed in
        // $(".signed-out").hide();
        // $(".signed-in").show();
});

// sign out button

// Google OAuth

// reminder to jeffrey to edit the home page so that my content shows all content instead if not signed in

// reminder to jeffrey to write in support for the three other pages

// handle sidebar open/close
$(document).ready(function($)
{
    const profileTooltip = $("#profile-button-div");
    const profileLink = $("a", profileTooltip);
    const profileIcon = $("i", profileTooltip);
    $("#profile_sidebar").on("show.bs.offcanvas", function() {
        
        // turn profile button into a close button

        // red background, black icon color
        profileLink.css({
            "background-color":"red",
            "color":"black"
        });
        // icon: "close"
        profileIcon.text("close");
        // title: "Close sidebar"
        profileTooltip.attr("data-bs-original-title", "Close sidebar");
        // close tooltip
        profileTooltip.tooltip('hide');

    });

    $("#profile_sidebar").on("hide.bs.offcanvas", function() {
        
        // reset profile

        // background: unset, icon color: unset
        profileLink.css({
            "background-color":"unset",
            "color":"var(--nav-link-color)"
        });
        // icon: "person"
        profileIcon.text("person");
        // title: "Profile"
        profileTooltip.attr("data-bs-original-title", "Profile");
        // close tooltip
        profileTooltip.tooltip('hide');
        profileTooltip.tooltip('disable');
        setTimeout(function(){
            profileTooltip.tooltip('enable');
        }, 100)

    });
});