import os

# 1. Update HTML
with open('scroll-animation/index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Remove canvas from body top
html_content = html_content.replace('<canvas id="hero-lightpass"></canvas>\n', '')

# Modify hero section
hero_start = '<header id="home" class="hero">'
hero_new = '''<header id="home" class="hero scroll-hero">
        <div class="sticky-hero">
            <canvas id="hero-lightpass"></canvas>
            <div class="hero-bg" style="background-image: url('../images/hero_cake.png');"></div>
            <div class="hero-content">
                <h1 class="fade-in-up">Where Every Slice is a Royal Experience</h1>
                <p class="fade-in-up delay-1">Freshly baked, beautifully crafted cakes tailored for your special moments.</p>
                <div class="rating fade-in-up delay-2">
                    <span class="stars">★★★★½</span>
                    <span class="reviews">(142 Google Reviews)</span>
                </div>
                <a href="#menu" class="primary-btn fade-in-up delay-3">Explore Menu</a>
            </div>
        </div>
    </header>'''

# Replace the entire old hero section
import re
html_content = re.sub(r'<header id="home" class="hero">.*?</header>', hero_new, html_content, flags=re.DOTALL)

with open('scroll-animation/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

# 2. Update CSS
with open('scroll-animation/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Modify canvas CSS
css_content = css_content.replace('''canvas {
  position: fixed;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  max-width: 100vw;
  max-height: 100vh;
  object-fit: contain;
  z-index: -1;
}''', '''canvas {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  min-width: 100%;
  min-height: 100%;
  object-fit: cover;
  z-index: -1;
}
.scroll-hero {
    height: 300vh; /* Make hero scrollable */
    display: block; /* Override previous flex */
}
.sticky-hero {
    position: sticky;
    top: 0;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
}''')

with open('scroll-animation/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

# 3. Update JS
with open('scroll-animation/script.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# We need to change the scroll listener for the canvas
old_scroll_logic = '''window.addEventListener('scroll', () => {  
  const scrollTop = html.scrollTop;
  const maxScrollTop = html.scrollHeight - window.innerHeight;
  const scrollFraction = scrollTop / maxScrollTop;
  // Frame index is 0-based in our array
  const frameIndex = Math.min(
    frameCount - 1,
    Math.floor(scrollFraction * frameCount)
  );
  
  requestAnimationFrame(() => updateImage(frameIndex));
});'''

new_scroll_logic = '''window.addEventListener('scroll', () => {  
  const hero = document.querySelector('.scroll-hero');
  if (!hero) return;
  
  const rect = hero.getBoundingClientRect();
  const heroTop = rect.top + window.scrollY;
  const heroHeight = hero.offsetHeight;
  const stickyHeight = window.innerHeight;
  
  // How far we have scrolled within the hero section
  let scrollProgress = (window.scrollY - heroTop) / (heroHeight - stickyHeight);
  
  // Clamp between 0 and 1
  scrollProgress = Math.max(0, Math.min(1, scrollProgress));
  
  const frameIndex = Math.min(
    frameCount - 1,
    Math.floor(scrollProgress * frameCount)
  );
  
  requestAnimationFrame(() => updateImage(frameIndex));
});'''

js_content = js_content.replace(old_scroll_logic, new_scroll_logic)

with open('scroll-animation/script.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Update complete")
