// We are here to power Website in Run time....
//alert("hello")
const slider = $(".slider-item");
slider.slick({
  autoplay: true,
  autoplaySpeed: 1500,
  dots: true
});
slider.on("wheel", function(e) {
  e.preventDefault();

  if (e.originalEvent.deltaY < 0) {
    $(this).slick("slickNext");
  } else {
    $(this).slick("slickPrev");
  }
});
