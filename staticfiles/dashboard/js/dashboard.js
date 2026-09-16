const sidebar = document.querySelector(".sidebar");

const menu = document.querySelector(".menu-toggle");

if(menu){

menu.addEventListener("click",()=>{

    sidebar.classList.toggle("active");

});

}

document.addEventListener("click",(e)=>{

if(window.innerWidth<992){

if(!sidebar.contains(e.target) && !menu.contains(e.target)){

    sidebar.classList.remove("active");

}

}

});