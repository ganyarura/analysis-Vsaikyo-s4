L = [{'kind': 'youtube#video', 'etag': 'FrT8ys6bltl8OTNmrJynOe7wg9M', 'id': 'WfirmFpMMA8', 'liveStreamingDetails': {'actualStartTime': '2022-04-16T11:26:24Z', 'scheduledStartTime': '2022-04-16T11:10:37Z', 'concurrentViewers': '2842', 'activeLiveChatId': 'Cg0KC1dmaXJtRnBNTUE4KicKGFVDM2xORmVKaVRxNkwzVVdvejRnMWUtQRILV2Zpcm1GcE1NQTg'}}]
dict = L[0]
dictdict = dict["liveStreamingDetails"]
views = dictdict["concurrentViewers"]
print(views)