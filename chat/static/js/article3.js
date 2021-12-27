var markdown_socket3;

window.addEventListener("load", init3);

function delete_article()
{
    let kakunin = confirm("本当に削除しますか？");
    if(kakunin){
        let room = document.getElementById("name");
        markdown_socket3.send(JSON.stringify({"room_name":room.textContent}));
    }
}

function init3()
{
    let room = document.getElementById("name");
    markdown_socket3 = new WebSocket(
        "ws://" + window.location.host + "/ws/markdown-delete/" + room.textContent + "/"
    );

    markdown_socket3.onmessage = function(e){
        let data = JSON.parse(e.data);
        if(data["delete"] == "true"){
            let prj_id = document.getElementById("prj_id");
            window.location = window.location.origin + "/" + prj_id.textContent;
        }

    }
}