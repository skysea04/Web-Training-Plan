const ham = document.querySelector(".hamburger");
const nav = document.querySelector(".nav-container");

function toggleNavBar(){
    nav.classList.toggle("nav-display");
}

ham.addEventListener("click", toggleNavBar)