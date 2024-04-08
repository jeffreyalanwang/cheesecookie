"use strict";



const courseCheck = document.querySelector('#course');
const languageCheck = document.querySelector('#language');
const softwareCheck = document.querySelector('#software');

const queryFieldContainer = document.querySelectorAll('#queryFields');

//queryFieldContainer.children.forEach(child => {
    //child.classList.toggle("hide");
    //console.log(child);
//});

$('#queryFields').children().attr("class","hide");

//queryFieldContainer.firstChild.attr('class','hide');

courseCheck.addEventListener('click', (event) => {
    if ( $('#course').is(':checked') )
    {
        $('#creditHours_block').removeAttr("class","hide");
        $('#prereq_block').removeAttr("class","hide");
        $('#req_block').removeAttr("class","hide");

        $('#compLang_block').removeAttr("class","hide");
        $('#compSoft_block').removeAttr("class","hide");
    }
    else 
    { 
        $('#creditHours_block').attr("class","hide");
        $('#prereq_block').attr("class","hide");
        $('#req_block').attr("class","hide"); 
        
        if ( ! ($('#language').is(':checked')) ) {
            $('#compSoft_block').attr("class","hide");
        }
        if ( ! ($('#software').is(':checked')) ) {
            $('#compLang_block').attr("class","hide");
        }
    }
});

languageCheck.addEventListener('click', (event) => {
    if ( $('#language').is(':checked') )
    {
        $('#compCourse_block').removeAttr("class","hide");
        $('#compSoft_block').removeAttr("class","hide");
    }
    else 
    {  
        if ( ! ($('#course').is(':checked')) ) {
            $('#compSoft_block').attr("class","hide");
        }
        if ( ! ($('#software').is(':checked')) ) {
            $('#compCourse_block').attr("class","hide");
        }
    }
});

softwareCheck.addEventListener('click', (event) => {
    if ( $('#software').is(':checked') )
    {
        $('#compCourse_block').removeAttr("class","hide");
        $('#compLang_block').removeAttr("class","hide");
    }
    else 
    {  
        if ( ! ($('#course').is(':checked')) ) {
            $('#compLang_block').attr("class","hide");
        }
        if ( ! ($('#language').is(':checked')) ) {
            $('#compCourse_block').attr("class","hide");
        }
    }
});