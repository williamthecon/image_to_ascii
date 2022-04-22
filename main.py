from PIL import Image

ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))

    return resized_image

def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join(ascii_chars[pixel//25] for pixel in pixels)

    return characters

def main(new_width=150):
    path = input("Enter a valid path to an image: ")
    try:
        image = Image.open(path)

        new_image_data = pixels_to_ascii(grayify(resize_image(image, new_width)))
        pixel_count = len(new_image_data)
        ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

        print(ascii_image)
    except Exception as e:
        print(e)
        print(path, "is not a valid path to an image.")

    main()

main()
