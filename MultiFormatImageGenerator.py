from PIL import Image, ImageDraw, ImageFont
import os
import random


def random_color():
    """Generate a random RGB color."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def random_resolution(min_width=100, max_width=1000, min_height=100, max_height=1000):
    """Generate a random resolution within given bounds."""
    return (random.randint(min_width, max_width), random.randint(min_height, max_height))


def create_test_image(file_name):
    # Get a random resolution
    width, height = random_resolution()

    # Create a new image with a random background color and random resolution
    bg_color = random_color()
    img = Image.new('RGB', (width, height), color=bg_color)

    d = ImageDraw.Draw(img)
    # Use a basic font that comes with PIL
    fnt = ImageFont.load_default()
    # Ensure text color is different from the background
    while True:
        text_color = random_color()
        if text_color != bg_color:
            break
    d.text((width // 4, height // 4), "Test Image", font=fnt, fill=text_color)

    img.save(file_name)


formats = ['jpg', 'jpeg', 'png', 'gif', 'bmp']


def main():
    total_images = int(input("How many images should be created for each format? "))

    if not os.path.exists('output_images'):
        os.mkdir('output_images')

    for fmt in formats:
        for i in range(total_images):
            file_name = f'output_images/test_image_{i + 1}.{fmt.lower()}'
            create_test_image(file_name)
            print(f"{file_name} created.")


if __name__ == '__main__':
    main()
