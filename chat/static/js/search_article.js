function search_js(event)
{
    let user = event.currentTarget.value;
    $.ajax({
        url: window.location.origin+window.location.pathname+ "api/search/article",
        type: "POST",
        data: {"user": user},
        dataType:"json",
        success:function(data){
            let user_result = document.getElementById("user_result");
            user_result.innerHTML = "検索予測";
            for(let user of data.result){
                user_result.innerHTML += ('<li><a href="'+window.location.origin+"/"+user.prj_id+"/"+user.id+'">' + user.title + "</a></li>")
            }
        }
    })
}

window.addEventListener('load', init);

function init()
{
    let user = document.getElementById("article_search");
    user.addEventListener("input", search_js);
}