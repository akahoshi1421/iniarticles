var markdown_socket2;

window.addEventListener("load", init2);

function hanei2(event)
{
    let room = document.getElementById("name");
    let title_in = event.currentTarget.value;

    markdown_socket2.send(JSON.stringify({"newtitle":title_in, "room_name":room.textContent}));
}

function init2()
{
    let room = document.getElementById("name");
    markdown_socket2 = new WebSocket(
        "ws://" + window.location.host + "/ws/markdown-title/" + room.textContent + "/"
    );

    markdown_socket2.onmessage = function(e){
        let data = JSON.parse(e.data);
        let data_txt = data["titles"]["newtitle"];
        let text_result = document.getElementById("title");
        text_result.value = data_txt;

        let data_time = data["titles"]["update_at"];
        let time_result = document.getElementById("time");
        time_result.textContent = data_time;
    }

    let title = document.getElementById("title");
    title.addEventListener("input", hanei2);
}