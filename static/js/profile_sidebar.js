import "https://cdn.jsdelivr.net/npm/js-cookie@3.0.5/dist/js.cookie.min.js";
var jwtDecode;
import("https://unpkg.com/jwt-decode@4.0.0/build/esm/index.js").then((module) => {
    jwtDecode = module.jwtDecode;
}); 

// Google OAuth
window.handleGToken = function (token) {
    const payload = jwtDecode(token["credential"]);
    const user_details = {};
    user_details["user_id"] = payload["sub"];
    user_details["email"] = payload["email"];
    user_details["picture_url"] = payload["picture"];
    user_details["name"] = payload["given_name"] + " " + payload["family_name"];
    // don't make the user impatient
    accountChangeFade();
    // send to server to create user if needed
    uploadUser(user_details, () => {
        // update cookie, update view
        signIn(user_details['user_id']);
    });
};

function accountChangeFade() {
    // don't want an ugly disappearing scrollbar
    const pageHeight = $('body').css('height');
    $('body').css('height', pageHeight);

    const target = $('body').children().not("#sidebar");
    target.fadeOut("fast", "linear");
}

function uploadUser(user_details, callback) {
    $.ajax({
        url: '/update_user',
        type: 'POST',
        data: user_details,
        complete: callback
    });
}

// Set the user cookie, refresh for updated page
function signIn(user_id) {
    Cookies.set('user', user_id);
    location.reload(false);
}
function signOut() {
    Cookies.remove('user');
    location.reload(false);
}

// call once cookie state is changed
function update_view() {
    if (Cookies.get('user') === undefined) {
        $(".signed-in").hide();
        $(".signed-out").show();
    } else {
        $(".signed-out").hide();
        $(".signed-in").show();
    }
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
        accountChangeFade();
        // remove cookie, refresh view
        signOut();
    })
});

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