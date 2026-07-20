import os
import re

# 1. Update HTML
with open('scroll-animation/index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# We want to wrap the hero and about section in an animation wrapper
# and move the canvas to stick behind both.

old_hero_start = '''<header id="home" class="hero scroll-hero">
        <div class="sticky-hero">
            <canvas id="hero-lightpass"></canvas>
            <div class="hero-bg" style="background-image: url('../images/hero_cake.png');"></div>
            <div class="hero-content">'''

new_hero_start = '''<div class="animation-wrapper">
        <div class="sticky-canvas">
            <canvas id="hero-lightpass"></canvas>
            <div class="hero-bg" style="background-image: url('../images/hero_cake.png');"></div>
        </div>
        
    <header id="home" class="hero content-section">
            <div class="hero-content">'''

html_content = html_content.replace(old_hero_start, new_hero_start)

# The end of hero was:
#             </div>
#         </div>
#     </header>
# We replace it:
old_hero_end = '''            </div>
        </div>
    </header>'''
new_hero_end = '''            </div>
    </header>'''
html_content = html_content.replace(old_hero_end, new_hero_end)

# The end of about section is:
#         </div>
#     </section>
old_about_end = '''        </div>
    </section>'''
new_about_end = '''        </div>
    </section>
</div> <!-- End animation-wrapper -->'''
html_content = html_content.replace(old_about_end, new_about_end)

with open('scroll-animation/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

# 2. Update CSS
with open('scroll-animation/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace sticky-hero and scroll-hero with new animation-wrapper styles
old_css_part = '''.scroll-hero {
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
}'''

new_css_part = '''.animation-wrapper {
    position: relative;
    /* We add height to the wrapper by letting the sections dictate it,
       or we make the sections tall so they scroll */
}
.sticky-canvas {
    position: sticky;
    top: 0;
    height: 100vh;
    width: 100%;
    overflow: hidden;
    z-index: -2;
}
.content-section {
    height: 150vh; /* make it scrollable */
    position: relative;
    z-index: 1;
}
.hero.content-section {
    margin-top: -100vh; /* pull it up over the sticky canvas */
}
.about.section {
    min-height: 150vh;
    display: flex;
    align-items: center;
    background-color: transparent; /* make it transparent so we see canvas */
}
'''
css_content = css_content.replace(old_css_part, new_css_part)

with open('scroll-animation/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

# 3. Update JS
with open('scroll-animation/script.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

old_js_part = '''const hero = document.querySelector('.scroll-hero');
  if (!hero) return;
  
  const rect = hero.getBoundingClientRect();
  const heroTop = rect.top + window.scrollY;
  const heroHeight = hero.offsetHeight;
  const stickyHeight = window.innerHeight;
  
  // How far we have scrolled within the hero section
  let scrollProgress = (window.scrollY - heroTop) / (heroHeight - stickyHeight);'''

new_js_part = '''const wrapper = document.querySelector('.animation-wrapper');
  if (!wrapper) return;
  
  const rect = wrapper.getBoundingClientRect();
  const wrapperTop = rect.top + window.scrollY;
  const wrapperHeight = wrapper.offsetHeight;
  const stickyHeight = window.innerHeight;
  
  // How far we have scrolled within the wrapper
  let scrollProgress = (window.scrollY - wrapperTop) / (wrapperHeight - stickyHeight);'''

js_content = js_content.replace(old_js_part, new_js_part)

with open('scroll-animation/script.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Combined animation logic applied")
