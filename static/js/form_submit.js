$(document).ready(function($)
{
    $('#save_button').on('click', function(event)
    {
        event.preventDefault();

        // collect all form responses
        var data = new FormData();

        // collect data from input and textarea elements
        $(':input[form="main-form"]', 'form[id="main-form"]').each(function(){
            if ($(this).attr('type') === "file") { // for image uploads
                data.append($(this).attr('id'), $(this).prop('files')[0])
            } else {
                data.append($(this).attr('id'), $(this).val());
            }
        });

        // collect data from wysiwyg editor
        $('#editor').each(function(){
            data.append('html_content', $(this).html());
        });

        // collect data from chip-based inputs
        var course_ids = []; // when corresponds to page, this is a list of courses that this course requires
        $('.chip-name', '.course-chips').each(function(){
            course_ids.push($(this).attr("data-id"));
        });
        if ($('.course-chips').length ) {
            data.append("course_ids", course_ids);
        }
        var software_ids = [];
        $('.chip-name', '.software-chips').each(function(){
            software_ids.push($(this).attr("data-id"));
        });
        if ($('.software-chips').length ) {
            data.append("software_ids", software_ids);
        }
        var language_ids = [];
        $('.chip-name', '.language-chips').each(function(){
            language_ids.push($(this).attr("data-id"));
        });
        if ($('.language-chips').length ) {
            data.append("language_ids", language_ids);
        }

        console.log("Form data: ");
        for (var pair of data.entries()) {
            console.log(pair); 
        }

        $.ajax({
            url: '#',
            type: 'POST',
            data: data,
            contentType: false,
            cache: false,
            processData: false,
            success: function (result) {
                $('#save_button').attr("data-bs-original-title", "Saved!");
                $('.tooltip-inner').html("Saved!");

                setTimeout(function(){
                    $('#save_button').attr("data-bs-original-title", "Save changes");
                    $('.tooltip').fadeOut();
                }, 2000)
            }
        });
    })
});