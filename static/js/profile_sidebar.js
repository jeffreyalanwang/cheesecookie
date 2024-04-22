var jwtDecode;
import("https://unpkg.com/jwt-decode@4.0.0/build/esm/index.js").then((module) => {
    jwtDecode = module.jwtDecode;
});

// Google OAuth
function handleGToken(token) {
    let payload = jwtDecode(token["credential"]);
    const user_details = {};
    user_details["user_id"] = payload["sub"]
    user_details["email"] = payload["email"];
    user_details["picture_url"] = payload["picture"];
    user_details["name"] = payload["given_name"] + payload["family_name"];
    // send server to create user if needed
    // update cookie
    update_view();
}

// TODO
function update_user_cookie() {

}

// call once cookie state is changed
function update_view() {
    $(".signed-in").hide();
    // access cookie
    // update name in sidebar title and icon in navbar
    // change which elements display based on whether user logged in
}

// initial update_view based on cookie
$(document).ready(function($)
{
    update_view();
});

// sign out button functionality
$(document).ready(function($)
{
    $("#signOutButton").click(function()
    {
        // remove cookie

        update_view();
    })
});

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