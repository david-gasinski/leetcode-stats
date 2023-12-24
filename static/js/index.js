const themes = {
    "nord" : "nord.png",
    "dracula" : "dracula.png",
    "gruvbox" : "gruvbox.png",
    "one_dark" : "one_dark.png",
    "monokai" : "monokai.png",
    "solarized_dark" : "solarized_dark.png",
    "solarized_light" : "solarized_light.png",
    "tokyo" : "tokyo.png",
    "terminal" : "terminal.png"  
}

const url = document.getElementById("url")
const theme = document.getElementById("theme");
const user = document.getElementById("username"); 
const realtime_example = document.getElementById("realtime")
let button = document.getElementById("submit");


function updateURL(){
    // find url and set style
    var unique_url = `![](https://leetcode.gasinski.dev/svg/${user.value}?theme=${theme.value})`
    // set to new text, prevents text s
    url.innerHTML = unique_url
    url.href = unique_url
}

function updatePreview(){
    // either update image with inputted username or default example
    let username = "david-gasinski" 
    
    if (user.value) {
        username = user.value
    }

    getImagePreview(username).then((data) => {
        realtime_example.innerHTML = data;
    })
}

async function getImagePreview(user) {
    const res = await fetch(`/svg/${user}?theme=${theme.value}`, {
        method: "GET",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
    });
    return res.text();
}

// add listeners
button.addEventListener("click", updateURL);
theme.addEventListener("change", updatePreview)

// run on page load
updatePreview()