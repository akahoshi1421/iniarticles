function search_js(event)
{
    let user = event.currentTarget.value;
    $.ajax({
        url: window.location.origin + "/search/project",
        type: "POST",
        data: {"user": user},
        dataType:"json",
        success:function(data){
            let user_result = document.getElementById("user_result");
            user_result.innerHTML = "検索予測";
            for(let user of data.result){
                user_result.innerHTML += ('<li><a href="'+window.location.origin+"/"+user.id+'">' + user.name + "</a></li>")
            }
        }
    })
}

window.addEventListener('load', init);

function init()
{
    let user = document.getElementById("project_search");
    user.addEventListener("input", search_js);
}