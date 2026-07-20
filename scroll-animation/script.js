const html = document.documentElement;
const canvas = document.getElementById("hero-lightpass");
const context = canvas.getContext("2d");

const frameCount = 270;
const currentFrame = index => (
  `../ezgif-4b2ecc7eb016d355-jpg/ezgif-frame-${index.toString().padStart(3, '0')}.jpg`
);

const images = [];
const preloadImages = () => {
  for (let i = 1; i <= frameCount; i++) {
    const img = new Image();
    img.src = currentFrame(i);
    images.push(img);
  }
};

preloadImages();

const initialImage = images[0];

const drawInitial = () => {
  canvas.width = initialImage.width || 1152;
  canvas.height = initialImage.height || 896;
  context.drawImage(initialImage, 0, 0);
};

if (initialImage.complete) {
  drawInitial();
} else {
  initialImage.onload = drawInitial;
}

const updateImage = index => {
  if (images[index] && images[index].complete) {
    context.drawImage(images[index], 0, 0);
  }
};

window.addEventListener('scroll', () => {  
  const wrapper = document.querySelector('.animation-wrapper');
  if (!wrapper) return;
  
  const rect = wrapper.getBoundingClientRect();
  const wrapperTop = rect.top + window.scrollY;
  const wrapperHeight = wrapper.offsetHeight;
  const stickyHeight = window.innerHeight;
  
  // How far we have scrolled within the wrapper
  let scrollProgress = (window.scrollY - wrapperTop) / (wrapperHeight - stickyHeight);
  
  // Clamp between 0 and 1
  scrollProgress = Math.max(0, Math.min(1, scrollProgress));
  
  const frameIndex = Math.min(
    frameCount - 1,
    Math.floor(scrollProgress * frameCount)
  );
  
  
  const heroBg = document.querySelector('.hero-bg');
  if (heroBg) {
     if (window.scrollY > 20) {
         heroBg.style.opacity = '0';
     } else {
         heroBg.style.opacity = '1';
     }
  }
  
  requestAnimationFrame(() => updateImage(frameIndex));

});


// Navbar Scrolled State
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Intersection Observer for Scroll Animations
const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.15
};

const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Select elements to animate
const animElements = document.querySelectorAll('.slide-up, .fade-in');
animElements.forEach(el => observer.observe(el));
