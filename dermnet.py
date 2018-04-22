'''
    Written in Python 2.7
'''

import requests
from PIL import Image
from bs4 import BeautifulSoup
from io import BytesIO
import os
import shutil

root = 'http://www.dermnet.com'