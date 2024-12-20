import os
from pytube import YouTube

def download_youtube_video(youtube_url, download_path="downloads"):
    try:
        # Create downloads folder if not exists
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        # Initialize YouTube object
        yt = YouTube(youtube_url)

        # Display video details
        print(f"Title: {yt.title}")
        print(f"Author: {yt.author}")
        print(f"Views: {yt.views:,}")
        print(f"Length: {yt.length} seconds")

        # Get highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        print("Downloading...")
        video_stream.download(output_path=download_path)
        print(f"Downloaded successfully to: {os.path.abspath(download_path)}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    youtube_url = input("Enter the YouTube video URL: ")
    download_youtube_video(youtube_url)
