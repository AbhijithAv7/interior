const projects = document.querySelectorAll(".project-card");

const observer = new IntersectionObserver((entries)=>{

entries.forEach((entry)=>{

if(entry.isIntersecting){

entry.target.classList.add("show");

}

});

},{
threshold:.2
});

projects.forEach(project=>observer.observe(project));