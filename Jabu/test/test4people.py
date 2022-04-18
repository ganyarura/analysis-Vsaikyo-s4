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

SEARCH_TEXTs = ["卯月コウ", "イブラヒム【にじさんじ】", "Kuzuha Channel", "Uruca ch /うるか"]
CHANNEL_IDs = []
for text in SEARCH_TEXTs:
    a_response = youtube.search().list(q=text, part="id,snippet", maxResults=25).execute()
    for item in a_response.get("items", []):
        if item["id"]["kind"] != "youtube#channel":
            continue
        CHANNEL_IDs.append(item["snippet"]["channelId"])

print(CHANNEL_IDs)

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
