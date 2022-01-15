import os
import time
import cv2
from matplotlib import pyplot as plt
from image import Image
from rotate_crop import rotate_neck_picture, crop_neck_picture, resize_image

output_directory = './output_chords'

def create_directory():
    if os.path.exists(output_directory):
        print('Using existing output folder')
    else:
        try:
            os.mkdir(output_directory)
            print('creating output directory')
        except OSError as error:
            print(error)

create_directory()
i = 1
plt.figure(1)
cropped_images = []
for filename in os.listdir("./pictures/"):
    print("File found: " + filename + " - Processing...")
    start_time = time.time()
    path = "./pictures/" + filename

    chord_image = Image(path=path)
    resized = resize_image(chord_image.image)
    new = Image(img=resized)
    new = Image(path=path)
    rotated_image = rotate_neck_picture(new)
    cropped_image = crop_neck_picture(rotated_image)

    plt.subplot(int("42" + str(i)))
    i += 1
    plt.imshow(cv2.cvtColor(chord_image.image, cv2.COLOR_BGR2RGB))
    #cv2.imwrite(output_directory + 'chord_image' + filename, chord_image.image)
    plt.subplot(int("42" + str(i)))
    i += 1
    plt.imshow(cv2.cvtColor(cropped_image.image, cv2.COLOR_BGR2RGB))
    cv2.imwrite('output_chords/'+'cropped_image_' + filename, cropped_image.image)
    print("Done - Time elapsed: %s seconds" % round(time.time() - start_time, 2))

plt.show()

