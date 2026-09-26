import sys

from PIL import Image, ImageDraw, ImageFont
from path import Path
import click

# get input
def handleInput(filepath, filedestination, width, height):
    # get filepath, filedestination, width and height. Path has to be Path object width and height are ints
    try:
        filepath, filedestination = Path(filepath), Path(filedestination)
    except Exception:
        print(f"Not a valid path: {filepath} or {filedestination}")
        sys.exit(10)

    if (not (isinstance(width, int) and isinstance(height, int))):
        print(f"Width and Height are not integers: {width} or {height}")
        sys.exit(11)
    return filepath, filedestination, width, height


# open image

def getImage(filepath: Path) -> Image:
    try:
        img = Image.open(filepath)
        print(f"Image loaded from {filepath}")
        return img
    except FileNotFoundError:
        print(f"File not found: {filepath}")

# resize image

def resizeImage(img: Image, width: int, height: int) -> Image:
    width, height = width, height
    try:
        img_resize = img.resize((width, height))
        return img_resize
    except Exception as e:
        print(f"Image couldn't be resized to {width}x{height}\nError: {e}")
        sys.exit(12)

# save new resized image under original-name_resized_sizeX_sizeY

def saveImage(img: Image, filedestination: Path) -> None:
    try:
        img.save(filedestination)
        return print(f"Image saved to {filedestination}")
    except Exception as e:
        print(f"Image could not be saved to {filedestination}\nError: {e}")


@click.command()
@click.option('--filepath', prompt='Path to Image', help='Relative or absolute path of image file')
@click.option('--filedestination', prompt='Your name', help='Destination relative or absolute path for the resized image')
@click.option('--width', type=int, prompt='New image width', help='Width of the resized image')
@click.option('--height', type=int, prompt='New image height', help='Height of the resized image')
def main(filepath, filedestination, width, height):
    filepath, filedestination, width, height = handleInput(filepath, filedestination, width, height)
    img = getImage(filepath)
    resized = resizeImage(img, width, height)
    saveImage(resized, filedestination)
    return

if __name__ == "__main__":
    main()