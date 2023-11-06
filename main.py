import os
import openai  # pip install openai
import urllib.request
from datetime import datetime

OPENAI_API_KEY = "your openai api key HERE"
IMAGE_DESCRIPTION = "image description HERE"
NUMBER_OF_PICTURES = 1 # how many images to generate
IMAGE_SIZE = "1024x1024" # image size 256x256, 512x512 in px

openai.api_key=OPENAI_API_KEY

response = openai.Image.create(
    prompt=IMAGE_DESCRIPTION,
    n=NUMBER_OF_PICTURES, 
    size=IMAGE_SIZE 
)

image_url = response['data'][0]['url'] # [0] is for the first image, if you have multiple images [1],[2],...


image_name = f"img_{datetime.now().strftime('%H_%M_%S')}.png"
urllib.request.urlretrieve(image_url, image_name) # download image locally
