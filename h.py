import requests
from bs4 import BeautifulSoup
import os

url = "https://www.google.com/search?q=image&oq=image+&aqs=chrome..69i57j0i131i433i512l3j0i512j0i433i512l2j0i512j0i131i433i512l2.9705j0j15&sourceid=chrome&ie=UTF-8" # replace with the URL of the website you want to download images from
output_folder = "/home/tspl/Documents/aaa" # replace with the name of the folder where you want to save the images
print("llll")

# create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# send a request to the website and parse the HTML response
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# find all image tags in the HTML
img_tags = soup.find_all("img")

# iterate through each image tag and download the image
for img in img_tags:
    img_url = img.get("src")
    if img_url.startswith("http"):
        filename = os.path.join(output_folder, img_url.split("/")[-1])
        # with open(filename, "wb") as f:
        #     f.write(requests.get(img_url).content)
        # print(f"Downloaded {filename}")

        try:
            with open(filename, "wb") as f:
                f.write(requests.get(img_url).content)
                print(f"Downloaded {filename}")
        except Exception as e:
            print(f"Error downloading {img_url}: {e}")
        
