$("#image").change(function(e) {

    for (var i = 0; i < e.originalEvent.srcElement.files.length; i++) {
        
        var file = e.originalEvent.srcElement.files[i];
        
        var reader = new FileReader();
        reader.onloadend = function() {
            $("#icon_img").attr("src", reader.result);
        }
        reader.readAsDataURL(file);
    }
});