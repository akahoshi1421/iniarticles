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

$(window).on("load", function(){
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
});

$(function() {
    $('.slide').each(function() {
      // スライド（画像）の数を取得
      var $slides = $(this).find('img'),
          slideNum = $slides.length,
          currentIdx = 0; // 何番目か
    
      // 最初の画像をフェードイン
      $(".slide img").eq(currentIdx).fadeIn();
      setInterval(dispNextSlide, 6000);
    
      // 次のスライドを表示するメソッド
      function dispNextSlide() {
        var nextIdx = currentIdx + 1;
    
        // 最後のスライドの場合ははじめに戻る
        if (nextIdx > (slideNum - 1)) {
          nextIdx = 0
        }
    
        // 現在のスライドをフェードアウト
        $(".slide img").eq(currentIdx).fadeOut(2000);
    
        // 次のスライドをフェードイン
        $(".slide img").eq(nextIdx).fadeIn(2000);
    
        // インデックスを更新
        currentIdx = nextIdx;
      }
    });
   });