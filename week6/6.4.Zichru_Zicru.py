from PIL import Image


def content_extraction(user_path):
    """
    The function extracts the encrypted content.
    :param user_path: Image's path.
    :return: The message that was encrypted
    """
    my_image = Image.open(user_path)
    my_image = my_image.convert('RGB')
    width, height = my_image.size
    pixels = my_image.load()
    text = ''
    for w in range(width):
        for h in range(height):
            if pixels[w, h] == (1, 1, 1):
                text += chr(h)
    return text


if __name__ == '__main__':
    image_path = input("Please enter image path: ")
    message_in_path = content_extraction(image_path)
    print(message_in_path)
