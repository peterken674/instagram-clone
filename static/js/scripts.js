$(document).ready(function(){
    $('.post-content').click(function(){
        url = $(this).attr('data-url');
        username = $(this).attr('data-username');
        profilepic = $(this).attr('data-profilepic')

        $('#imageModal .img-container img').attr('src', url);
        $('#imageModal .post-header-profilepic img').attr('src', profilepic);
        $('#imageModal .post-header-username small strong').text(username);
    })
    
})