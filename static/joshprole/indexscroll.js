        let currentsect = 1
        let maxsect = 1
        $(document).ready(function(){
          let i = 1;
          $(".section").each(function(){
            $(this).attr("id","section"+i)
            i++
          })
          maxsect = i-1
          console.log(maxsect)
          $('html, body').animate({
                    scrollTop: $("#section"+currentsect).offset().top
                }, 1000);
        })
       $('body').on('mousewheel DOMMouseScroll', function(e){
          if(typeof e.originalEvent.detail == 'number' && e.originalEvent.detail !== 0) {
            if(e.originalEvent.detail > 0) {
              if (currentsect<maxsect) {currentsect++
              $('html, body').animate({
                    scrollTop: $("#section"+currentsect).offset().top
                }, 1000);}
            } else if(e.originalEvent.detail < 0){
                if (currentsect>1) {currentsect--
              $('html, body').animate({
                    scrollTop: $("#section"+currentsect).offset().top
                }, 1000);
            }}
          } else if (typeof e.originalEvent.wheelDelta == 'number') {
            if(e.originalEvent.wheelDelta < 0) {
                if (currentsect<maxsect) {currentsect++
              $('html, body').animate({
                    scrollTop: $("#section"+currentsect).offset().top
                }, 1000);}
            } else if(e.originalEvent.wheelDelta > 0) {
                if (currentsect>1) {currentsect--
              $('html, body').animate({
                    scrollTop: $("#section"+currentsect).offset().top
                }, 1000);
            }}
          }
        });