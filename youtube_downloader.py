"""
    Youtube downloader Utility Script to enter any number of valid youtube urls for the program 
    to download them in the format you want.

    Example of a valid link: https://www.youtube.com/watch?v=dQw4w9WgXcQ
    -----------------------------------------------------------
    Made by Massimo Sabba
"""

from youtube_dl import YoutubeDL
import validators

urls = []

def youtube_downloader():
    # Insert the urls for the program to validate them
    while True:
        url = input(
            "Insert any number of valid YouTube urls. When ready, simply press [ENTER]: ")

        if url == "":
            break
        elif validators.url(url):

            if url in urls:
                print("This link in already in the list!")
                continue

            else:
                urls.append(url)

        elif not validators.url(url):
            print("Invalid link! Please use another one.")
            continue

    # For every url in the list of given ones, it searches for it and downloads it.
    for url in urls:
        try:
            video_info = YoutubeDL().extract_info(url=url,download=False)
            file_name = f"{video_info['title']}.mp3".replace("\\", "").replace("/", "").replace(":", "").replace('"', "").replace("?", "").replace("<", "").replace(">", "").replace("|", "").replace("*", "")
            options={
                'format':'bestaudio/best',
                'keepvideo':False,
                'outtmpl':file_name,
            }
            with YoutubeDL(options) as ydl:
                ydl.download([video_info['webpage_url']])
        except:
            print("There was an error downloading this link! Try checking your connection. Going to the next one...")
            continue

if __name__ == "__main__":
    youtube_downloader()