/*=========================================
        COUNTER ANIMATION
=========================================*/

const counters = document.querySelectorAll(".counter");

const observer = new IntersectionObserver((entries) => {

    entries.forEach((entry) => {

        if (entry.isIntersecting) {

            const counter = entry.target;
            const target = parseInt(counter.dataset.target);

            let current = 0;
            const speed = 80;

            const updateCounter = () => {

                const increment = Math.ceil(target / speed);

                current += increment;

                if (current >= target) {

                    counter.innerHTML = target + "+";

                } else {

                    counter.innerHTML = current + "+";

                    requestAnimationFrame(updateCounter);

                }

            };

            updateCounter();

            observer.unobserve(counter);

        }

    });

}, {
    threshold: 0.5
});

counters.forEach((counter) => {

    observer.observe(counter);

});

/*=========================================
        SERVICE CAROUSEL
=========================================*/

const slider = document.querySelector(".service-slider");
const cards = document.querySelectorAll(".service-card");
const dotsContainer = document.querySelector(".carousel-dots");

if (slider && cards.length) {

    let current = 0;

    let visibleCards = window.innerWidth <= 768 ? 1 : 3;

    const totalPages = Math.ceil(cards.length / visibleCards);

    // Create dots
    for (let i = 0; i < totalPages; i++) {

        const dot = document.createElement("span");

        dot.className = "carousel-dot";

        if (i === 0) dot.classList.add("active");

        dot.addEventListener("click", () => {

            current = i;

            updateCarousel();

            resetAuto();

        });

        dotsContainer.appendChild(dot);

    }

    const dots = document.querySelectorAll(".carousel-dot");

    function updateCarousel() {

        const gap = 30;

        const cardWidth = cards[0].offsetWidth + gap;

        slider.style.transform =
            `translateX(-${current * cardWidth * visibleCards}px)`;

        dots.forEach(dot => dot.classList.remove("active"));

        dots[current].classList.add("active");

    }

    function nextSlide() {

        current++;

        if (current >= totalPages) current = 0;

        updateCarousel();

    }

    let auto = setInterval(nextSlide, 3500);

    function resetAuto() {

        clearInterval(auto);

        auto = setInterval(nextSlide, 3500);

    }

    window.addEventListener("resize", () => {

        visibleCards = window.innerWidth <= 768 ? 1 : 3;

        location.reload();

    });

}