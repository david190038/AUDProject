import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
import requests
from PIL import Image
from io import BytesIO

# Maximum 20 Bilder, da mehr gesperrt sind

GOOGLE_IMAGE = \
    "https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&"


def main():
    global SAVE_FOLDER
    global _inp
    global RESIZED_FOLDER
    global _newimage
    global _filename

    SAVE_FOLDER = str(input('Please specify a path for the original images: '))
    RESIZED_FOLDER = str(input('Please specify a path for the resized images: '))

    if not os.path.exists(SAVE_FOLDER):
        os.mkdir(SAVE_FOLDER)
    if not os.path.exists(RESIZED_FOLDER):
        os.mkdir(RESIZED_FOLDER)

    _inp = input('What are you looking for?')
    _filename = str(input('How should the file be named? '))
    n_images = int(input('How many images do you want? '))

    searchurl = GOOGLE_IMAGE + "q=" + _inp
    data = getdata(searchurl)
    download_images(data, n_images)


def download_images(data, n_images: int):
    soup = BeautifulSoup(data, 'html.parser')
    imageAttributes = soup.find_all('img')
    imageAttributes = imageAttributes[0:n_images + 1]

    for item in imageAttributes:
        print(item['src'])

    imagelinks = []
    for imageAttribute in imageAttributes:
        imagelinks.append(imageAttribute['src'])  # filtering urls from the ResultSet.

    imagelinks.pop(0)  # First Entry does not include a valid URL! Deleting it with the method Pop

    for i, imagelink in enumerate(imagelinks):
        # open image link and save as file
        response = requests.get(imagelink)

        imagename = SAVE_FOLDER + '/' + _filename + str(i + 1) + '.jpg'
        with open(imagename, 'wb') as file:
            file.write(response.content)
        with Image.open(imagename) as image:
            width, height = image.size
            if height == width or (height <= width / 2 or width <= height / 2):
                newsize = (500, 500)
                _newimage = image.resize(newsize)
                _newimage.save(RESIZED_FOLDER + '/' + _filename + str(i + 1) + '.jpg', quality=100, optimize=True)



def getdata(url):
    r = requests.get(url)
    return r.text


main()
