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

      $(function(){
03     
04        $('a[href*=#]').click(function() {
05        if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'')
06            && location.hostname == this.hostname) {
07                var $target = $(this.hash);
08                $target = $target.length && $target || $('[name=' + this.hash.slice(1) +']');
09                if ($target.length) {
10                    var targetOffset = $target.offset().top;
11                    $('html,body').animate({scrollTop: targetOffset}, 800); // change number for scroll speed, higher = slower
12                    return false;
13                }
14            }
15        });
16    });

});


     


