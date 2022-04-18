import json
from urllib import response
from apiclient.discovery import build

API_KEY = ""
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
SEARCH_TEXT = "卯月コウ"
CHANNEL_ID = "UC3lNFeJiTq6L3UWoz4g1e-A"

youtube = build(
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    developerKey=API_KEY
)

# チャンネル名でチャンネルを指定する場合
#response = youtube.search().list(q=SEARCH_TEXT, part="id,snippet", maxResults=25).execute()

# チャンネルIDでチャンネルを指定する場合
"""response = youtube.channels().list(
    part = 'snippet,statistics',
    id = CHANNEL_ID
    ).execute()
"""

# チャンネルIDでチャンネルを指定して最新の動画の情報を取得する
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
    print("*" * 10)
