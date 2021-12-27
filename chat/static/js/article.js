var markdown_socket;

window.addEventListener("load", init);

function hanei(event)
{
    let room = document.getElementById("name");
    let text_in = event.currentTarget.value;

    markdown_socket.send(JSON.stringify({"message":text_in, "room_name":room.textContent}));
}

function init()
{
    let room = document.getElementById("name");
    markdown_socket = new WebSocket(
        "ws://" + window.location.host + "/ws/markdown/" + room.textContent + "/"
    );

    markdown_socket.onmessage = function(e){
        let data = JSON.parse(e.data);
        let data_txt = data["message"]["message"];
        let text_result = document.getElementById("text");
        text_result.value = data_txt;

        let data_time = data["message"]["update_at"];
        let time_result = document.getElementById("time");
        time_result.textContent = data_time;

        let data_txt_markdown = data["message_markdown"];
        let md = document.getElementById("md");
        md.innerHTML = data_txt_markdown;
    }

    let text = document.getElementById("text");
    text.addEventListener("input", hanei);
}