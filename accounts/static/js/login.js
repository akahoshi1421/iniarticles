$(window).on("resize", function(){
    let size = $(this).width();
    if(size <= 1000){
        $(".img").each(function(){
            $(this).removeClass("col-7");
            $(this).addClass("none");
        });
        $(".form-background").each(function(){
            $(this).removeClass("col-5");
        });
    }
    else{
        $(".img").each(function(){
            if(!$(this).hasClass("col-7")){
                $(this).addClass("col-7");
                $(this).removeClass("none");
            }
            $(".form-background").each(function(){
                $(this).addClass("col-5");
            });
        });
    }
});