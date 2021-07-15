$(document).ready(function(){
    $('.post-content').click(function(){
        url = $(this).attr('data-url');
        username = $(this).attr('data-username');
        profilepic = $(this).attr('data-profilepic')
        caption = $(this).attr('data-caption')

        $('#imageModal .img-container img').attr('src', url);
        $('#imageModal .post-header-profilepic img').attr('src', profilepic);
        $('#imageModal .post-header-username #caption').text(caption);
        $('#imageModal .post-header-username small strong').text(username);
        
    })
    $('#viewComments').click(function () {
        url = $(this).attr('data-url');
        username = $(this).attr('data-username');
        profilepic = $(this).attr('data-profilepic')
        caption = $(this).attr('data-caption')

        $('#imageModal .img-container img').attr('src', url);
        $('#imageModal .post-header-profilepic img').attr('src', profilepic);
        $('#imageModal .post-header-username #caption').text(caption);
        $('#imageModal .post-header-username small strong').text(username);
        
    })
    
})