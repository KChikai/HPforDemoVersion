$(function () {
  var $setElem = $('.switch'),
      pcName = '_pc',
      spName = '_sp',
      replaceWidth = 768;

  $('.sb-toggle-submenu').off('click').on('click', function() {
    var $submenu;

    $submenu = $(this).parent().children('.sb-submenu');
    $(this).add($submenu).toggleClass('sb-submenu-active');

    if ($submenu.hasClass('sb-submenu-active')) {
      $submenu.slideDown(200);
    } else {
      $submenu.slideUp(200);
    }
  });

  // fade staff photo block when hover this.
  $('.default_box_link, .top_box_link, .requirements_button a').hover(function() {
    $(this).fadeTo('fast', .6);
  }, function() {
    $(this).fadeTo('fast', 1);
  });

  $setElem.each(function() {
    var $this = $(this);

    function imgSize(){
      var windowWidth = parseInt($(window).width());
      if (windowWidth >= replaceWidth) {
        $this.attr('src', $this.attr('src').replace(spName,pcName)).css({visibility:'visible'});
      } else if (windowWidth < replaceWidth) {
        $this.attr('src', $this.attr('src').replace(pcName,spName)).css({visibility:'visible'});
      }
    }
    $(window).resize(function() { imgSize(); });

    imgSize();
  });

  // dropdown `dropmenu` child when mouseover this
  $('#dropmenu > li').hover(
    function() {
      $(this).find('ul').stop().slideDown('fast');
    },
    function() {
      $(this).find('ul').stop().slideUp('fast');
    }
  );

  $('.question').on('click', function() {
    $(this).next().slideToggle();
  }).next().hide();

  $(document).ready(function() {
    if ($.slidebars != undefined) {
      $.slidebars();
    }
  });
});
