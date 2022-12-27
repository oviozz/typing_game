
import random
import time
import sys
import os

class Paragraph:
    @staticmethod
    def file_open():
        with open('paragraphs.txt') as paragraph:
            paragraphs = paragraph.readlines()
        return paragraphs[random.randint(0,len(paragraphs)-2)].strip()






