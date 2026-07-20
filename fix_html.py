import os
import re

with open('scroll-animation/index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Fix the overzealous replace
# The only animation wrapper end should be after the about section.
# The about section is:
#     <section id="about" class="about section"> ... </section>
# And then the wrapper closes.
# But right now we have:
#     <section id="menu" ... </section></div> <!-- End animation-wrapper -->
#     <section id="reviews" ... </section></div> <!-- End animation-wrapper -->
#     <section id="contact" ... </section></div> <!-- End animation-wrapper -->

# We can just remove the string from everywhere except after about section.
# First, remove all of them.
html_content = html_content.replace('</div> <!-- End animation-wrapper -->\n', '')
html_content = html_content.replace('</div> <!-- End animation-wrapper -->', '')

# Now re-add it specifically after the about section.
about_end = '''        </div>
    </section>'''

# Find the index of about section
idx = html_content.find('<section id="about" class="about section">')
if idx != -1:
    end_idx = html_content.find(about_end, idx) + len(about_end)
    html_content = html_content[:end_idx] + '\n</div> <!-- End animation-wrapper -->\n' + html_content[end_idx:]

with open('scroll-animation/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML fixed")
