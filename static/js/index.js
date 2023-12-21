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

function updateURL(){
    // find url and set style
    var unique_url = `![](https://digest.gasinski.dev/svg/${user.value}?theme=${theme.value})`
    // set to new text, prevents text s
    url.innerHTML = unique_url
    url.href = unique_url
}

// update URL 
let button = document.getElementById("submit");
button.addEventListener("click", updateURL);

// update image on theme change
theme.addEventListener("change", function() {
    // get img and update it to theme
    document.getElementById("example_img").setAttribute("src", `/static/img/${themes[theme.value]}`)

})
