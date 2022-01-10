window.addEventListener("load", account_init);

function account_init()
{
    const target = document.getElementById("target");
    target.addEventListener("mouseover", over);
    target.addEventListener("mouseleave", leave);
}

function over()
{
    let account = document.getElementById("user-info");
    account.classList.remove("d-none");
}

function leave()
{
    let account = document.getElementById("user-info");
    account.classList.add("d-none");
}

$(document).on("click", "#target",function(){
    let check = confirm("ログアウトしますか？");
    if(check){
        window.location = window.location.origin + "/accounts/logout";
    }
});

