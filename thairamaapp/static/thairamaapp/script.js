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


      function filterPath(string) {
      return string
        .replace(/^\//,'')
        .replace(/(index|default).[a-zA-Z]{3,4}$/,'')
        .replace(/\/$/,'');
      }
      var locationPath = filterPath(location.pathname);
      var scrollElem = scrollableElement('html', 'body');
     
      $('a[href*=#]').each(function() {
        var thisPath = filterPath(this.pathname) || locationPath;
        if (  locationPath == thisPath
        && (location.hostname == this.hostname || !this.hostname)
        && this.hash.replace(/#/,'') ) {
          var $target = $(this.hash), target = this.hash;
          if (target) {
            var targetOffset = $target.offset().top;
            $(this).click(function(event) {
              event.preventDefault();
              $(scrollElem).animate({scrollTop: targetOffset}, 400, function() {
                location.hash = target;
              });
            });
          }
        }
      });
     
      // use the first element that is "scrollable"
      function scrollableElement(els) {
        for (var i = 0, argLength = arguments.length; i <argLength; i++) {
          var el = arguments[i],
              $scrollElement = $(el);
          if ($scrollElement.scrollTop()> 0) {
            return el;
          } else {
            $scrollElement.scrollTop(1);
            var isScrollable = $scrollElement.scrollTop()> 0;
            $scrollElement.scrollTop(0);
            if (isScrollable) {
              return el;
            }
          }
        }
        return [];
      }

});


     


