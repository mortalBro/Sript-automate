# import mutagen

# # Open the MP3 file
# mp3_file = mutagen.File("sangit_name.mp3")

# # Extract the metadata
# title = mp3_file.get("TIT2").text[0]
# artist = mp3_file.get("TPE1").text[0]
# # album = mp3_file.get("TALB").text[0]
# # year = mp3_file.get("TDRC").text[0][:4]  # Extract only the year from the full date

# # Print the extracted metadata
# print(f"Title: {title}")
# print(f"Artist: {artist}")
# # print(f"Album: {album}")
# # print(f"Year: {year}")




############################################################

import os
import mutagen

# Set the path to the folder containing the MP3 files
folder_path = "folder_hai"

# Get a list of all the files in the folder
files = os.listdir(folder_path)

# Loop over each file in the folder
song_not_mp3=[]
for file_name in files:
    # Check if the file is an MP3 file
    if file_name.endswith(".mp3"):
        song_name=file_name[:-4]
        print(file_name)
    else:
        song_not_mp3.append(file_name)

        # Construct the full path to the file
    #     file_path = os.path.join(folder_path, file_name)
        
    #     # Open the MP3 file
    #     mp3_file = mutagen.File(file_path)
        
    #     # Extract the metadata
    #     title = mp3_file.get("TIT2").text[0]
    #     artist = mp3_file.get("TPE1").text[0]
    #     # album = mp3_file.get("TALB").text[0]
    #     # year = mp3_file.get("TDRC").text[0][:4]  # Extract only the year from the full date
        
    #     # Print the extracted metadata
    #     print(f"Title: {title}")
    #     print(f"Artist: {artist}")
    # #     print(f"Album: {album}")
    # #     print(f"Year: {year}")
    # else:
    #     print("problem hai")
