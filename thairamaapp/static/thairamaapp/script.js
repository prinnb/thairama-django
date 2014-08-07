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

      $('a[href^="#"]').on('click',function (e) {
          e.preventDefault();

          var target = this.hash,
          $target = $(target);

          $('html, body').stop().animate({
              'scrollTop': $target.offset().top
          }, 900, 'swing', function () {
              window.location.hash = target;
          });
      });
});
