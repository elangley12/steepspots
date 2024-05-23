function HomepageCarousel() {
    return (
      <div id="about-carousel" className="carousel slide" data-bs-ride="carousel">
        <div className="carousel-indicators">
          <button type="button" data-bs-target="#about-carousel" data-bs-slide-to="0" className="active" aria-current="true" aria-label="Slide 1"></button>
          <button type="button" data-bs-target="#about-carousel" data-bs-slide-to="1" aria-label="Slide 2"></button>
          <button type="button" data-bs-target="#about-carousel" data-bs-slide-to="2" aria-label="Slide 3"></button>
        </div>
        <div className="carousel-inner">
          <div className="carousel-item active">
            <img src="../static/images/tea-mug-cheers.jpg" className="d-block w-100 carousel-img" alt="..."/>
            <div className="carousel-caption d-none d-md-block">
              <h4>Explore</h4>
              <p>the world through your cup</p>
            </div>
          </div>
          <div className="carousel-item">
            <img src="../static/images/loose-leaf-teas.jpg" className="d-block w-100 carousel-img" alt="..."/>
            <div className="carousel-caption d-none d-md-block">
              <h4>Discover</h4>
              <p>flavors that inspire your curiosity</p>
            </div>
          </div>
          <div className="carousel-item">
            <img src="../static/images/tea-leaf-water-drops.jpg" className="d-block w-100 carousel-img" alt="..."/>
            <div className="carousel-caption d-none d-md-block">
              <h4>Unearth</h4>
              <p>your steeping favorites from anywhere</p>
            </div>
          </div>
        </div>
        <button className="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
          <span className="carousel-control-prev-icon" aria-hidden="true"></span>
          <span className="visually-hidden">Previous</span>
        </button>
        <button className="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
          <span className="carousel-control-next-icon" aria-hidden="true"></span>
          <span className="visually-hidden">Next</span>
        </button>
      </div>
    );
}

ReactDOM.render(<HomepageCarousel />, document.getElementById("homepage-carousel"));