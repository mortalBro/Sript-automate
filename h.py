# import requests
# from bs4 import BeautifulSoup
# import os

# url = "https://www.google.com/search?q=image&oq=image+&aqs=chrome..69i57j0i131i433i512l3j0i512j0i433i512l2j0i512j0i131i433i512l2.9705j0j15&sourceid=chrome&ie=UTF-8" # replace with the URL of the website you want to download images from
# output_folder = "/home/tspl/Documents/aaa" # replace with the name of the folder where you want to save the images
# print("llll")

# # create the output folder if it doesn't exist
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

# # send a request to the website and parse the HTML response
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# # find all image tags in the HTML
# img_tags = soup.find_all("img")

# # iterate through each image tag and download the image
# for img in img_tags:
#     img_url = img.get("src")
#     if img_url.startswith("http"):
#         filename = os.path.join(output_folder, img_url.split("/")[-1])
#         # with open(filename, "wb") as f:
#         #     f.write(requests.get(img_url).content)
#         # print(f"Downloaded {filename}")

#         try:
#             with open(filename, "wb") as f:
#                 f.write(requests.get(img_url).content)
#                 print(f"Downloaded {filename}")
#         except Exception as e:
#             print(f"Error downloading {img_url}: {e}")
        









# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True  # Divisible by 400, so it's a leap year
#             else:
#                 return False  # Divisible by 100 but not by 400, so it's not a leap year
#         else:
#             return True  # Divisible by 4 but not by 100, so it's a leap year
#     else:
#         return False  # Not divisible by 4, so it's not a leap year

# # Example usage
# year = 2024
# if is_leap_year(year):
#     print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")
# arr=[7,3,2,1,8,4,6,5]
# n=len(arr)
# i=0
# while(i<n):
#     perfect_postion=arr[i]-1
#     perfect_value=arr[i]
#     if(arr[perfect_postion]!=perfect_value):
#         temp=arr[perfect_postion]
#         arr[perfect_postion]  = perfect_value
#         arr[i]=temp
#     else:
#         i+=1
# print(arr)
