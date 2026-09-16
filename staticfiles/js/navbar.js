const menuBtn = document.querySelector(".menu-btn");
const navLinks = document.querySelector(".nav-links");

menuBtn.addEventListener("click", () => {

    navLinks.classList.toggle("active");

    if(navLinks.classList.contains("active")){
        menuBtn.innerHTML = "✕";
    }else{
        menuBtn.innerHTML = "☰";
    }

});

document.querySelectorAll(".nav-links a").forEach(link => {

    link.addEventListener("click", () => {

        navLinks.classList.remove("active");

        menuBtn.innerHTML = "☰";

    });

});

const consultBtn = document.getElementById("mobileConsult");

if (consultBtn) {

    consultBtn.addEventListener("click", function(e){

        // First click -> expand only
        if(!consultBtn.classList.contains("open")){

            e.preventDefault();

            consultBtn.classList.add("open");

        }

    });

    // Click anywhere else -> close
    document.addEventListener("click", function(e){

        if(!consultBtn.contains(e.target)){

            consultBtn.classList.remove("open");

        }

    // Collapse consultation button when page scrolls
    window.addEventListener("scroll", () => {

    if (consultBtn && consultBtn.classList.contains("open")) {

        consultBtn.classList.remove("open");

    }

    });

    });

}