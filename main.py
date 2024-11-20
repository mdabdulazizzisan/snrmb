import json
import os
import time
import requests
from rembg import remove
from PIL import Image
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('image_processor.log'),
        logging.StreamHandler()
    ]
)
