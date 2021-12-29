function search_js(event)
{
    let user = event.currentTarget.value;
    $.ajax({
        url: window.location.origin + "/api/name",
        type: "POST",
        data: {"user": user},
        dataType:"json",
        success:function(data){
            let user_result = document.getElementById("user_result");
            user_result.innerHTML = "検索予測";
            for(let user of data.users){
                user_result.innerHTML += ("<li>" + user + "</li>")
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