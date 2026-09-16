const track = document.querySelector(".slider-track");
const slides = document.querySelectorAll(".slider-track img");

const next = document.querySelector(".next");
const prev = document.querySelector(".prev");

let index = 0;

function moveSlide(){

    track.style.transform = `translateX(-${index * 100}%)`;

}

next.addEventListener("click",()=>{

    index++;

    if(index >= slides.length){

        index = 0;

    }

    moveSlide();

});

prev.addEventListener("click",()=>{

    index--;

    if(index < 0){

        index = slides.length-1;

    }

    moveSlide();

});

/* AUTO SLIDE */

setInterval(()=>{

    index++;

    if(index >= slides.length){

        index = 0;

    }

    moveSlide();

},4000);