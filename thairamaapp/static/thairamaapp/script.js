$(document).ready(function(){
      $(".flexnav").flexNav();

      $(".owl-carousel").owlCarousel({

      autoplay:true,
      items : 1,
      loop: true,
      smartSpeed: 800,
      // "singleItem:true" is a shortcut for:
      // items : 1, 
      // itemsDesktop : false,
      // itemsDesktopSmall : false,
      // itemsTablet: false,
      // itemsMobile : false

      });

      $(".lightGallery").lightGallery({
      });

      $('.imageGallery').lightSlider({
            gallery:true,
            minSlide:1,
            maxSlide:1,
            currentPagerPosition:'left'
      }); 


  $('a[href*=#]:not([href=#])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html,body').animate({
          scrollTop: target.offset().top
        }, 1000);
        return false;
      }
    }
  });


});
