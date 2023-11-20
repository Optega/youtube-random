# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import random

import googleapiclient.discovery


def get_random_video(username):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.getenv("YOUTUBE_API_KEY")

    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=DEVELOPER_KEY)

    # search symbol @ in username and remove all before it
    if "@" in username:
        username = username.split("@")[1]

    # search symbol / in username and remove all after it
    if "/" in username:
        username = username.split("/")[0]

    request = youtube.search().list(part="id,snippet", maxResults=1, q=username, type="channel")
    response = request.execute()

    if response["pageInfo"]["totalResults"] == 0:
        print("No channel found")
    else:
        print(f"Channel: {username}")
        channel_id = response["items"][0]["id"]["channelId"]

        request = youtube.playlists().list(part="contentDetails, id, localizations, player, snippet, status", channelId=channel_id, maxResults=50)
        response = request.execute()

        if response["pageInfo"]["totalResults"] == 0:
            print("No playlists found")
        else:
            print("Number of playlists: ", response["pageInfo"]["totalResults"])

            # get random nubmer from 0 to totalResults
            random_item = random.randrange(0, response["pageInfo"]["totalResults"])
            playlist_id = response["items"][random_item]["id"]

            print("Selected playlist: ", response["items"][random_item]["snippet"]["title"])

            request = youtube.playlistItems().list(part="contentDetails, id, snippet, status", maxResults=50, playlistId=playlist_id)
            response = request.execute()

            if response["pageInfo"]["totalResults"] == 0:
                print("No videos found")
            else:
                print("Number of videos: ", response["pageInfo"]["totalResults"])

                # get random nubmer from 0 to totalResults
                random_item = random.randrange(0, response["pageInfo"]["totalResults"])
                video_id = response["items"][random_item]["contentDetails"]["videoId"]

                print("Selected video: ", response["items"][random_item]["snippet"]["title"])
                print("Video URL: ", f"https://www.youtube.com/watch?v={video_id}")

                return f"https://www.youtube.com/watch?v={video_id}"
