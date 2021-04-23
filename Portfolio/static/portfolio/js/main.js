$(document).ready(function(){
  var btns=$('.project-area .button-group button');
  btns.click(function(e){
    $('.project-area .button-group button').removeClass('active');
    e.target.classList.add("active");

    var selector =$(e.target).attr('data-filter');
    $('.project-area .grid').isotope({
      filter:selector
    });
    return false;
  });

    $('.project-area .button-group #btn1').trigger('click');
    $('.project-area .grid .text-popup-link').magnificPopup({
      type:'image',
      showCloseBtn:true,
      removalDelay: 300,

  // Class that is added to popup wrapper and background
  // make it unique to apply your CSS animations just to this exact popup
  mainClass: 'mfp-fade',
  gallery:{
    enabled:true
  },
});
// sticky navmenu
var nav_offset_top=$('.header_area').height();
function navbarFixed()
{
  if($('.header_area').length)
  {
    $(window).scroll(function(){
      var scroll=$(window).scrollTop();
      if(scroll >= nav_offset_top)
      {
        $('.header_area .main-menu').addClass('navbar_fixed');
      }
      else{
        $('.header_area .main-menu').removeClass('navbar_fixed');
      }
    });
  }
}
navbarFixed();
 $(window).resize(function() {
  if ( $(window).width() < 766) {
       $('.subscribe-us-area .subscribe').removeClass('container');
      }
    else{
       $('.subscribe-us-area .subscribe').addClass('container');
    }
});

$("#modal").modal('show');

$('.owl-carousel').owlCarousel({
    loop:false,
    margin:10,
    nav:true,
    responsive:{
        0:{
            items:1,
            center:true,
        },
        600:{
            items:3
        },
    }
});
  $('.card').hover(function(){
    $('.read-more').addClass('d-block');
    $('.read-more').removeClass('d-none');
  },
  function(){
    $('.read-more').removeClass('d-block');
    $('.read-more').addClass('d-none');
  }
  );
  // ==== Magnific Popup =====
  // $('.first-img').magnificPopup({type:'image'});
});
