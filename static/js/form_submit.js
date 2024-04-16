$(document).ready(function($)
{
        $('#save_button').on('click', function(event)
        {
            event.preventDefault();

            // collect all form responses
            var data = {'submit': true};

            $(':input','form').each(function(){
                data[$(this).attr('id')] = $(this).val();
            });

            console.log("Form data: ");
            console.log(data);

            $.ajax({
                url: '#',
                type: 'POST',
                data: data,
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