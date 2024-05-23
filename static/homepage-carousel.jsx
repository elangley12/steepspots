function HomepageCarousel() {
    return (
      <div id="about-carousel" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-indicators">
          <button type="button" data-bs-target="#about-carousel" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
          <button type="button" data-bs-target="#about-carousel" data-bs-slide-to="1" aria-label="Slide 2"></button>
          <button type="button" data-bs-target="#about-carousel" data-bs-slide-to="2" aria-label="Slide 3"></button>
        </div>
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img src="../static/images/tea-mug-cheers.jpg" class="d-block w-100 carousel-img" alt="...">
            <div class="carousel-caption d-none d-md-block">
              <h4>Explore</h4>
              <p>the world through your cup</p>
            </div>
          </div>
          <div class="carousel-item">
            <img src="../static/images/loose-leaf-teas.jpg" class="d-block w-100 carousel-img" alt="...">
            <div class="carousel-caption d-none d-md-block">
              <h4>Discover</h4>
              <p>flavors that inspire your curiosity</p>
            </div>
          </div>
          <div class="carousel-item">
            <img src="../static/images/tea-leaf-water-drops.jpg" class="d-block w-100 carousel-img" alt="...">
            <div class="carousel-caption d-none d-md-block">
              <h4>Unearth</h4>
              <p>your steeping favorites from anywhere</p>
            </div>
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    );
}