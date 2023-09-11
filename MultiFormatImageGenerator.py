import os
import shutil
from jinja2 import Environment, FileSystemLoader


def scan_image_directory(directory):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    images = []

    for subdir, _, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in image_extensions):
                rel_dir = os.path.relpath(subdir, directory)
                images.append(os.path.join(rel_dir, file))

    return images


def create_pages(image_list, per_page=20):
    total_pages = -(-len(image_list) // per_page)  # Ceiling division
    for page_num in range(total_pages):
        start_index = page_num * per_page
        end_index = start_index + per_page
        yield image_list[start_index:end_index]


# Ensure output directory exists
if not os.path.exists('output'):
    os.mkdir('output')

# Setup Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

# Gallery template
gallery_template = env.get_template('gallery.html')

# Generate gallery pages
image_list = scan_image_directory('images')
pages = list(create_pages(image_list))

for idx, page_images in enumerate(pages):
    with open(f'output/gallery_page_{idx}.html', 'w') as f:
        f.write(gallery_template.render(images=page_images, current_page=idx, total_pages=len(pages)))

# About template
about_template = env.get_template('about.html')
with open('output/about.html', 'w') as f:
    f.write(about_template.render())

# Copy CSS to output directory
shutil.copy2('templates/style.css', 'output/style.css')
