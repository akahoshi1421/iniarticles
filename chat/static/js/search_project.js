function search_js(event)
{
    let user = event.currentTarget.value;
    if(user != ""){
        $.ajax({
            url: window.location.origin + "/api/search/project",
            type: "POST",
            data: {"user": user},
            dataType:"json",
            success:function(data){
                let user_result = document.getElementById("user_result");
                user_result.innerHTML = "<span class='mintyo search-prediction'>検索予測</span><hr>";
                for(let user of data.result){
                    user_result.innerHTML += ('<li><a href="'+window.location.origin+"/"+user.id+'">' + user.name + "</a></li>")
                    user_result.innerHTML += "<div class='search-height'></div>"
                }
            }
        })
    }
    else{
        let user_result = document.getElementById("user_result");
        user_result.innerHTML = "";
    }
}

window.addEventListener('load', init);

function init()
{
    let user = document.getElementById("project_search");
    user.addEventListener("input", search_js);
}

$(window).on("click",function(){ 
    $(".suggest").each(function(){
        if(!$(this).hasClass("none")){
            $(this).addClass("none");
        }
    });
});

$(document).on("input", "#project_search", function(){
    $(".suggest").each(function(){
        if($(this).hasClass("none")){
            $(this).removeClass("none");
        }
    });
});