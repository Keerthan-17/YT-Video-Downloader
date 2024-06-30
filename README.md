YouTube Video Downloader
This Python script allows you to download YouTube videos by providing a video link. It uses the pytube library to fetch and download the highest resolution stream available for the video.

Prerequisites
Before running the script, ensure you have Python installed on your system. You'll also need to install the pytube library. You can install it using pip:pip install pytube
Usage
Clone the Repository:

Clone or download the repository to your local machine.

Navigate to the Directory:

Open a terminal or command prompt and navigate to the directory where the script download_youtube_video.py is located.

Run the Script:

Execute the script by running the following command:python download_youtube_video.py
Enter the YouTube Video Link:

When prompted, enter the full YouTube video link (e.g., https://www.youtube.com/watch?v=your_video_id).

Download Progress:

The script will display the title of the video being downloaded and show the progress until the download completes. The progress is not displayed in percentage in this version of the script.

Download Completion:

Once the download is complete, a message will be displayed indicating the successful download.

Error Handling:

If an error occurs during the download process (e.g., invalid link or network issues), an error message will be displayed.

Customization
Download Path: By default, the script saves the downloaded video in the current working directory. You can customize the script to specify a different download directory by modifying the download_youtube_video function.
Notes
This script downloads the video in the highest resolution available. If you need to download specific resolutions or formats, you can modify the script accordingly using pytube's stream methods.
The script uses the input() function to prompt for the YouTube video link. Ensure you enter a valid YouTube video link when prompted.
