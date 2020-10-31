
let navbarLight = document.getElementById("nav-bar-light");
let navbarDark = document.getElementById("nav-bar-dark");
let navItems = document.getElementsByClassName("nav-item");
let blogSearch = document.getElementById("blog-search-form");
let questionSearch = document.getElementById("faq-search-form");
let easyWayList = document.getElementById("easy-way-ol");
let siteUrl = "http://127.0.0.1:8000"

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

// Navbar active toggle

// for (let i = 0; i < navItems.length; i++) {
//   navItems[i].onclick = function (event) {
//     let hightlight = event.target;
//     for (let sibling of this.parentNode.children) {
//       sibling.classList.remove("active");
//     }
//     hightlight.classList.add("active")
//   }
// }

// Clickable list on homepage -- Easy Way to Use Dinee


if (easyWayList) {
  let listItems = easyWayList.getElementsByClassName("easy-way-li")
  for (let i = 0; i < listItems.length; i++) {
    listItems[i].onclick = function (event) {
      let highlight = event.target;
      for (let sibling of this.parentNode.children) {
        sibling.classList.remove("active");
      }
      highlight.classList.add("active")
    }
  }
}


// Search function event

document.addEventListener("keydown", function (event) {
  if (event.keyCode == 13) {
    if (questionSearch) {
      window.location.href = siteUrl + `/faq/${questionSearch.value}`;
    }
    else if (blogSearch) {
      window.location.href = siteUrl + `/blog/search/${blogSearch.value}`;
    }
    else {
      console.log("nothing to search...")
    }
  }
})

// questionSearch.addEventListener("keydown", function (event) {
//   console.log("faq search jalan");
//   if (event.keyCode == 13 && questionSearch) {
//     window.location.href = siteUrl + `/faq/${questionSearch.value}`;
//   }
//   else {
//     console.log('question form is null, aborting search...')
//   };
// })

// blogSearch.addEventListener("keydown", function (event) {
//   console.log("script search jalan");
//   if (event.keyCode == 13 && blogSearch) {
//     window.location.href = siteUrl + `/blog/search/${blogSearch.value}`;
//   }
//   else {
//     console.log('blog form is null, aborting search...')
//   };
// })

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
