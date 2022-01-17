import cv2
import os
import time
import uuid


IMAGES_PATH = r'C:\Users\calvi\PycharmProjects\IKCOVI\collected_images'
labels = ['A', 'B', 'C', 'D', 'E','F','G']
number_imgs = 15

def create_directory():
    if os.path.exists(IMAGES_PATH):
        print('Using existing output folder')
    else:
        try:
            os.mkdir(IMAGES_PATH)
            print('creating output directory')
        except OSError as error:
            print(error)


def main():
    create_directory()

    for label in labels:
        os.mkdir(r'C:\Users\calvi\PycharmProjects\IKCOVI\collected_images\\'+label)
        cap = cv2.VideoCapture(0)
        print(r'verzamelen beeld materiaal voor ' + label)
        time.sleep(3)
        for imgnum in range(number_imgs):
            ret, frame = cap.read()
            image_name = os.path.join(IMAGES_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
            cv2.imwrite(image_name, frame)
            cv2.imshow('frame', frame)
            time.sleep(2)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release



if __name__ == '__main__':
    main()

