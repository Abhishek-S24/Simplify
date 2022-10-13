$(document).ready(function() {

    $('.has_ul').click(function(){
        if($(this).hasClass('active')){
            $(this).removeClass('active');
        }
        else{
            $('.has_ul').removeClass('active');
            $(this).addClass('active');
        }
    });

    $('.accord li a').click(function(){
        $('.accord li a').removeClass('current');
        if(!$(this).hasClass('has_ul')){
            $(this).addClass('current');
        }
    });


    $('.nav_icon').click(function(){
        if($('.sidebar-left').is(':visible')){
            $('.sidebar-left').removeClass('d-lg-block mob');
        }
        else{
            $('.sidebar-left').addClass('d-lg-block mob');
        }
    });    


});
