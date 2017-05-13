$(document).ready(function(){
  $('.interview_list_box').hover(function() {
    var self = $(this);
    self.css({"background-image": "url("+self.data().enter+")"});
  }, function () {
    var self = $(this);
    self.css({"background-image": "url("+self.data().leave+")"});
  }).each(function(i,e) {//preload
    var self = $(e);
    var img = $("<img>");
    img.attr("src",self.data().enter);
  })
  
  $(".type_search").on("click", function() {
      if($(window).width() <= 768){
        $(this).nextAll("ul").slideToggle();
      　 $(this).toggleClass("remove");
      }
  });
  
});
$(window).resize(function() {
  if($(window).width() >= 768){
    $('.searchCategory ul').show();
  }
});

$(document).ready(function(){
  var topbnr_box = $("#topbnr_box");
  if(topbnr_box) {
    $.each([1, 2, 3, 4, 5, 6, 7, 8],function(i,e) {
      var id_name = "a#staff_target_" + e;
      var box = topbnr_box.find(id_name);
      if(box) {
        if(typeof random_interviews != "undefined") {
          var interview = random_interviews.shift();
          box.attr("href",interview.link);
          box.find("img.topbnr").attr("src", i%2==0 ? interview.image_s : interview.image_l);
          box.find(".interview_comment").text(interview.title);
          box.find(".interview_name").text(interview.name);
        }
      }
    });
  }
});

$(document).ready(function(){
    $("a").click(function(e) {
        if(!$(this).hasClass("noscroll") && !$(this).data("toggle") && this.hash && this.host == window.location.host && this.pathname == window.location.pathname) {
            var target = $(this.hash);
            if (target.length > 0) {
                $("html,body").animate({
                    scrollTop: target.offset().top
                }, 300);
                return false;
            }
        }
    });
});
