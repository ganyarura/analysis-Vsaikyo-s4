import json
from urllib import response
from apiclient.discovery import build

API_KEY = ""
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
CHANNEL_ID = "UC3lNFeJiTq6L3UWoz4g1e-A"

youtube = build(
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    developerKey=API_KEY
)
"""
response = youtube.search().list(
    part = "snippet",
    channelId = CHANNEL_ID,
    maxResults = 1,
    order = "date"
).execute()

for item in response.get("items", []):
    if item["id"]["kind"] != "youtube#video":
        continue
    print("*" * 10)
    print(json.dumps(item, indent=2, ensure_ascii=False))
    print("*" * 10)"""

VIDEO_ID = "WfirmFpMMA8"
details = youtube.videos().list(
    part="liveStreamingDetails",
    id=VIDEO_ID
).execute()

detailitems = details['items']
print(detailitems)

