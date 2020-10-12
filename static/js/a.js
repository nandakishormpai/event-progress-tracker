
$(document).ready(function(){
    // nav toggle
    $(".nav-toggle").click(function (){
        $(".header .nav").slideToggle();
    })
    $(".header .nav a").click(function (){
        if($(window).width() < 768){
            $(".header .nav").slideToggle();
        }
    })


    // fixed header
    $(window).scroll(function (){
        if($(this).scrollTop() > 100){
            $(".header").addClass("fixed");
        }
        else {
            $(".header").removeClass("fixed");
        }
    })

});

// average progress 
CSS.registerProperty({
    name: '--p',
    syntax: '<integer>',
    initialValue: 0,
    inherits: true });


// preloader
window.addEventListener("load", function(){
    document.querySelector(".preloader").classList.add("opacity-0")
    
    setTimeout(function(){
        document.querySelector(".preloader").style.display="none"
    }, 1000)
})
    