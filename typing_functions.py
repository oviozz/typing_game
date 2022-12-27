
import random
import time
import sys
import os

class Paragraph:
    @staticmethod
    def file_open():
        with open(resource_path('paragraphs.txt')) as paragraph:
            paragraphs = paragraph.readlines()
        return paragraphs[random.randint(0,len(paragraphs)-2)].strip()


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



