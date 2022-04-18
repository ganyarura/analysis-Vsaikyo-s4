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

VIDEO_IDs = ['JPcmD51cK5E', 'NDNCHgChFXw', '7MQxPlmQhSE']

num_of_views = []

for video in VIDEO_IDs:
    details = youtube.videos().list(
        part="liveStreamingDetails",
        id=video
    ).execute()
    detailitems = details['items']
    dict = detailitems[0]
    dictdict = dict["liveStreamingDetails"]
    views = dictdict["concurrentViewers"]
    print(views)
    num_of_views.append(views)

print(num_of_views)
