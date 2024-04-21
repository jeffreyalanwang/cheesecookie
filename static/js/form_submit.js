$(document).ready(function($)
{
        $('#save_button').on('click', function(event)
        {
            event.preventDefault();

            // collect all form responses
            //var data = {'submit': true};
            var data = new FormData();

            $(':input', 'form').each(function(){
                if ($(this).attr('type') === "file") { // for image uploads
                    data.append($(this).attr('id'), $(this).prop('files')[0])
                } else {
                    data.append($(this).attr('id'), $(this).val());
                }
            });

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