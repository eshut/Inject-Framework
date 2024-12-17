"""Framework: https://github.com/eshut/Inject-Framework"""

import base64
import os
import random
from random import choice
from string import ascii_lowercase, ascii_uppercase
from string import digits

import cv2
import numpy as np
import pyautogui
from PIL import Image

from framework.Base.BaseElement import *

FILES = jsonGetter.GetJson.get_file(CONFIG, "Files")


class SysOperations:
    @staticmethod
    def upload(file):
        path = os.getcwd() + FILES + file
        pyautogui.write(path)
        pyautogui.press('enter')

    @staticmethod
    def download64_img(data, filepath):
        img_data = base64.b64decode(data)
        with open(filepath, 'wb') as f:
            f.write(img_data)

    @staticmethod
    def generate_string(x=10):
        string = [choice(ascii_uppercase + ascii_lowercase + ascii_lowercase + digits) for i in range(x)]
        random.shuffle(string)
        string = "".join(string)
        return string

    @staticmethod
    def compare_images(path_1, path_2):
        image1 = Image.open(path_1)
        size = image1.size
        image2 = Image.open(path_2)
        image2 = image2.convert("RGB")
        new_image2 = image2.resize(size)
        new_image2.save(path_2, quality=95)

        img1 = cv2.imread(path_1, 0)
        img2 = cv2.imread(path_2, 0)

        try:
            res = cv2.absdiff(img2, img1)
            percentage = (np.count_nonzero(res) * 100) / res.size
        except:
            percentage = 99999
        return percentage
