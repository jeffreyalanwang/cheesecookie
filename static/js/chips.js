// taken from
// https://www.geeksforgeeks.org/how-to-create-a-chips-component-using-html-css-javascript

function addOption(id, dataList) {
    dataList.children("[data-id=" + id + "]").prop("disabled", false);
}

function removeOption(id, dataList) {
    dataList.children("[data-id=" + id + "]").prop("disabled", true);
}

// Function to create a new chip 
function createChip(name, id, containerClass) { 
    const dataList = $( "datalist", $(containerClass).parent() );

    $(containerClass)
        // add chip element
        // afterElement.before(newElement);
        .children(".chip-form").before($('<div></div>')
        .addClass("chip") 
            // add chip's name element
            .append($('<div></div>')
            .addClass("chip-name")
            .text(name)
            .attr("data-id", id)
            )
            // add chip's remove button
            .append($('<div></div>')
            .addClass("close-icon")
            .text("x")
            )
        .click(function () {
            addOption(id, dataList);
            $(this).remove();
        })
        );
    removeOption(id, dataList);
}

function chipId(name, dataList) {
    let id = -1;
    dataList.children('option').each(function () {
        if (this.value === name) {
            id = $(this).attr("data-id");
        }
    });
    return id;
}

function validChip(name, dataList) {
    let sentinel = false;
    dataList.children('option').each(function () {
        if (this.value === name) {
            sentinel = true;
        }
    });
    return sentinel;
}

function plusButtonColor(color, button, speed) {

    let inTrans, outTrans, waitTime;
    switch (speed) {
        case 1:
            inTrans = "0.25s ease";
            outTrans = "0.3s linear";
            waitTime = 800;
            break;
        case 2:
            inTrans = "0s ease";
            outTrans = "0.75s linear";
            waitTime = 200;
            break;
        default:
            console.log("issue 21439812734");
      }

    button.stop();
    button.css({"color": color, "transition":"color " + inTrans});
    setTimeout(function () {
        button.css({"color": "unset", "transition":"color " + outTrans});
    }, waitTime);
}
  
$(document).ready(function($)
{
    // Handle chips form submission 
    $("button", ".chip-form").click(function(){
        const nameInput = $(".chip-input", $(this).parent())
        const name = nameInput.val().trim();
        const dataList = $('dataList', $(this).parent())
        if (name !== "" && validChip(name, dataList)) { 
            plusButtonColor("#66FF00", $(this), 2);

            let containerClass = "";
            $(this).parent()[0].classList.values().forEach(element => {
                className = element;
                if (className == "chip-form") {
                    className = "chips-container";
                }
                containerClass += "." + className;
            });

            createChip(name, chipId(name, dataList), containerClass);

            nameInput.val(""); 
        } else { // invalid chip name input
            plusButtonColor("red", $(this), 1);
        }
    });
});