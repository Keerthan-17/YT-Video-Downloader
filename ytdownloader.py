from pytube import YouTube
import sys

def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining 
    percentage_of_completion = bytes_downloaded / total_size * 100
    sys.stdout.write(f'\rDownloading: {percentage_of_completion:.2f}%')
    sys.stdout.flush()

def download_youtube_video(link):
    try:
        # Create a YouTube object with the video link
        yt = YouTube(link, on_progress_callback=progress_function)

        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()

        # Download the video
        print(f"Downloading: {yt.title}")
        stream.download()

        print("\nDownload completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_link = input("Enter the YouTube video link: ")
    download_youtube_video(video_link)
