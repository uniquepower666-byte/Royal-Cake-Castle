import os

# Read files
with open('index.html', 'r', encoding='utf-8') as f:
    root_html = f.read()

with open('styles.css', 'r', encoding='utf-8') as f:
    root_css = f.read()

with open('script.js', 'r', encoding='utf-8') as f:
    root_js = f.read()

with open('scroll-animation/script.js', 'r', encoding='utf-8') as f:
    scroll_js = f.read()

# Process HTML
new_html = root_html.replace('<link rel="stylesheet" href="styles.css">', '<link rel="stylesheet" href="style.css">')
new_html = new_html.replace('<body>', '<body>\n    <canvas id="hero-lightpass"></canvas>')
new_html = new_html.replace('images/', '../images/')

# Process CSS
canvas_css = """
canvas {
  position: fixed;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  max-width: 100vw;
  max-height: 100vh;
  object-fit: contain;
  z-index: -1;
}
"""

new_css = root_css + canvas_css
new_css = new_css.replace('background-color: var(--light);', 'background-color: transparent;')
new_css = new_css.replace('background-color: var(--darker);', 'background-color: rgba(17, 17, 17, 0.8);')
new_css = new_css.replace('.hero-bg {\n    position: absolute;', '.hero-bg {\n    display: none;\n    position: absolute;')
new_css = new_css.replace('.section {\n    padding: 6rem 5%;\n}', '.section {\n    padding: 6rem 5%;\n    background-color: rgba(253, 251, 247, 0.5);\n}')

# Process JS
new_js = scroll_js + '\n\n' + root_js

# Write files
with open('scroll-animation/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

with open('scroll-animation/style.css', 'w', encoding='utf-8') as f:
    f.write(new_css)

with open('scroll-animation/script.js', 'w', encoding='utf-8') as f:
    f.write(new_js)

print("Merge complete")
