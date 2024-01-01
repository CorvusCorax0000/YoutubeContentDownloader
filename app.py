from math import ceil
from pytube import YouTube
from googleapiclient.discovery import build

api_key = 'YOUR_API_KEY'  # replace with your YouTube Data API

youtube = build('youtube', 'v3', developerKey=api_key)

playlist_id = 'PL06diOotXAJJHjvUm7FNNG5a7XUA2_C27'  # Just the ID, not the full URL

# Request the playlist items
playlist_items = youtube.playlistItems().list(
    part='contentDetails',
    playlistId=playlist_id,
    maxResults=50  # Adjust this number to the number of videos you want to retrieve per request
).execute()

video_ids = [item['contentDetails']['videoId']
             for item in playlist_items['items']]

video_links = [
    f'https://www.youtube.com/watch?v={video_id}' for video_id in video_ids]

for link in video_links:
    yt = YouTube(link)
    # video = yt.streams.get_highest_resolution() # replace with this when you want to download videos instead of audios
    audio = yt.streams.filter(only_audio=True).first()
    file_size = audio.filesize_approx
    file_size_MB = round(file_size / (1024 * 1024), 2) if file_size else 0.0
    print(f"Downloading: {yt.title} ({file_size_MB} Mb)")
    audio.download("D:\musicLib") # replace directory with
