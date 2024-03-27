from googleapiclient.discovery import build

api_key = "AIzaSyAf44ue23JB05gq_zl1kWWMg78NK0aHWPI"
video_id = "AhOo5w5wLn0"

resource = build('youtube','v3',developerKey=api_key)

request = resource. commentThreads().list(part="snippet",
                                          videoId=video_id,
                                          maxResults= 10,
                                          order="orderUnspecified")

response =request.execute()
items = response["items"][:3]
print("-----------------------------------------------------------------------------------")
for item in items:
    item_info = item["snippet"]

    topLevelComment = item_info["topLevelComment"]
    comment_info = topLevelComment["snippet"]

    print("Comment By:", comment_info["authorDisplayName"])
    print("Comment Text:",comment_info["textDisplay"])
    print("Likes on Comment:", comment_info["likeCount"])
    print("Comment Date:",comment_info["publishedAt"])
    print("======================================")