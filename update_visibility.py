import os

# 1. Update CSS
with open('scroll-animation/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Fix hero-bg visibility and canvas sizing
css_content = css_content.replace('''.hero-bg {
    display: none;
    position: absolute;''', '''.hero-bg {
    display: block;
    position: absolute;''')

css_content = css_content.replace('''    transition: transform 10s ease-out;
}''', '''    transition: opacity 0.5s ease-out, transform 10s ease-out;
    z-index: -1;
}''')

css_content = css_content.replace('''canvas {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  min-width: 100%;
  min-height: 100%;
  object-fit: cover;
  z-index: -1;
}''', '''canvas {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  min-width: 100%;
  min-height: 100%;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: -2;
}''')

with open('scroll-animation/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)


# 2. Update JS
with open('scroll-animation/script.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Fix initialImage load issue just in case
js_content = js_content.replace('''initialImage.onload = function() {
  canvas.width = initialImage.width;
  canvas.height = initialImage.height;
  context.drawImage(initialImage, 0, 0);
};''', '''const drawInitial = () => {
  canvas.width = initialImage.width || 1152;
  canvas.height = initialImage.height || 896;
  context.drawImage(initialImage, 0, 0);
};

if (initialImage.complete) {
  drawInitial();
} else {
  initialImage.onload = drawInitial;
}''')

# Add fade out logic to the scroll listener
new_logic = '''
  const heroBg = document.querySelector('.hero-bg');
  if (heroBg) {
     if (window.scrollY > 20) {
         heroBg.style.opacity = '0';
     } else {
         heroBg.style.opacity = '1';
     }
  }
  
  requestAnimationFrame(() => updateImage(frameIndex));
'''
js_content = js_content.replace('requestAnimationFrame(() => updateImage(frameIndex));', new_logic)

with open('scroll-animation/script.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Update visibility complete")
