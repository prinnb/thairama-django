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
            currentPagerPosition:'left',
            enableTouch:true,
            enableDrag: true,
            item:1,
            auto: true
      });



      $(function(){
     
        $('a[href*=#]').click(function() {
        if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'')
            && location.hostname == this.hostname) {
                var $target = $(this.hash);
                $target = $target.length && $target || $('[name=' + this.hash.slice(1) +']');
                if ($target.length) {
                    var targetOffset = $target.offset().top;
                    $('html,body').animate({scrollTop: targetOffset}, 1200); // change number for scroll speed, higher = slower
                    return false;
                }
            }
        });
    }); 

});


     


