import json
from urllib import response
from apiclient.discovery import build

API_KEY = ""
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    developerKey=API_KEY
)

CHANNEL_IDs = ['UC3lNFeJiTq6L3UWoz4g1e-A', 'UCmZ1Rbthn-6Jm_qOGjYsh5A', 'UCSFCh5NL4qXrAy9u-u2lX3g', 'UChrTMfNcD1eN2ENGWBD7lUQ']
VIDEO_IDs = []

for channel in CHANNEL_IDs:
    b_response = youtube.search().list(
        part = "snippet",
        channelId = channel,
        maxResults = 1,
        order = "date"
    ).execute()
    for item in b_response.get("items", []):
        if item["id"]["kind"] != "youtube#video":
            continue
        VIDEO_IDs.append(item["id"]["videoId"])

print(VIDEO_IDs)
