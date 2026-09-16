gsap.utils.toArray("section").forEach(section=>{

    gsap.from(section,{

        y:100,
        opacity:0,

        duration:1,

        scrollTrigger:{

            trigger:section,

            start:"top 80%",

            toggleActions:"play none none none"

        }

    });

});