// slide 
document.addEventListener("DOMContentLoaded", function () {
    var carousel = new bootstrap.Carousel(document.getElementById("carouselExample"), {
      interval: 3000, // Set the interval (in milliseconds) for autoplay
      ride: "carousel", // Enable the carousel to start automatically
    });
  });