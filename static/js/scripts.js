$(document).ready(function(){
    $('.post-content').click(function(){
        url = $(this).attr('data-url');
        $('#imageModal .img-container img').attr('src', url);
    })
    
})