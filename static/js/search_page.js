// advanced options expander
$(document).ready(function($)
{
    $('#open-close').click(() => {
        if ($('#query-options').attr('closed') != 'true') { // to close
            $('#query-options').attr('closed', true);
            $('i', '#open-close').text('chevron_left');
            $('#actual-options').slideUp();
        } else { // to open            
            $('#query-options').attr('closed', false);
            $('i', '#open-close').text('expand_more');
            $('#actual-options').slideDown();
        }
    });
});

function reloadQueryOptions () {
    $('#actual-options').children().hide();
    console.log('ho');
    if ($('#course_chk').prop('checked')) {
        console.log('hi');
        $('.for-course', '#actual-options').show();
    }
    if ($('#software_chk').prop('checked')) {
        $('.for-software', '#actual-options').show();
    }
    if ($('#language_chk').prop('checked')) {
        $('.for-language', '#actual-options').show();
    }
}

// show advanced options based on intro checkboxes
$(document).ready(function($)
{
    reloadQueryOptions();
    $('input[type="checkbox"]', '#intro').change(reloadQueryOptions);
});