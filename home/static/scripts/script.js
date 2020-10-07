
let navbarLight = document.getElementById("nav-bar-light");
let navbarDark = document.getElementById("nav-bar-dark")

// Change navbar on scroll

let offset = navbarLight.offsetTop;

// Is the page still at the top?

let scrolled = false;

function scrollFunction () {
  if(window.pageYOffset > offset) {
    // fadeOut(navbarLight)
    navbarLight.style.display = "none"
    // fadeIn(navbarDark)
    navbarDark.style.display = "inline"
  }
  else {
    // fadeOut(navbarDark)
    navbarDark.style.display = "none"
    // fadeIn(navbarLight)
    scrolled = false;
    navbarLight.style.display = "inline"
  }
}

// Call the function on window scroll

document.addEventListener("DOMContentLoaded", function() {
  navbarDark.style.display = "none"
})

window.onscroll = function() { 
  scrollFunction()
  scrolled = true;
}

// Fade-in / Fade-out animation

function fadeIn (element) {
  let op = 0.1 //Initial opacity
  element.style.display = "block";
  let timer = setInterval(function () {
    // if(op >= 1) {
    //   clearInterval(timer);
    // }
    element.style.opacity = op

    op += op * 0.1;
  }, 20)
}

function fadeOut (element) {
  let op = 1 //Initial opacity
  element.style.display = "block";
  let timer = setInterval(function () {
    // if(op <= 0) {
    //   clearInterval(timer);
    // }
    element.style.opacity = op

    op -= op * 0.1
  }, 20)


}
