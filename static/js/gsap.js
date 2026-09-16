gsap.registerPlugin(ScrollTrigger);

const tl = gsap.timeline();

tl.from(".navbar",{
    y:-100,
    opacity:0,
    duration:0.8
})

.from(".hero-title",{
    y:100,
    opacity:0,
    duration:1
})

.from(".hero-subtitle",{
    y:60,
    opacity:0,
    duration:0.8
},"-=0.5")

.from(".hero-btn",{
    scale:0.8,
    opacity:0,
    duration:0.6
},"-=0.4")

.from(".hero-image",{
    x:120,
    opacity:0,
    duration:1
},"-=0.8");

gsap.from(".stat-box",{
    y:80,
    opacity:0,
    duration:1,
    stagger:0.2,
    ease:"power3.out",
    scrollTrigger:{
        trigger:".service-stats",
        start:"top 80%"
    }
});