let menuBtn = document.querySelector('.menuBtn');
$(document).ready(function() {
  $('.menuBtn').click(function() {
    $('.header__menu').animate({
      width: ["toggle"],
      heigth: ["toggle"],
      opacity: ["toggle"],
    }, 1500, "linear")
  })
})