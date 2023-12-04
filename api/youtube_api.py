# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import random

import googleapiclient.discovery

# TODO: check if url is video


# Disable OAuthlib's HTTPS verification when running locally.
# *DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
DEVELOPER_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, developerKey=DEVELOPER_KEY)


def get_random_video(url):
    useraname = url

    if "watch" in url:
        video_id = url.split("v=")[1]

        # search symbol & in video_id and remove all after it
        if "&" in video_id:
            video_id = video_id.split("&")[0]

        request = youtube.videos().list(part="id,snippet", id=video_id)
        response = request.execute()

        if response["pageInfo"]["totalResults"] == 0:
            print("No video found")
        else:
            print(f"Channel: {response['items'][0]['snippet']['channelTitle']}")
            channel_id = response["items"][0]["snippet"]["channelId"]
            return get_random_video_by_channel_id(channel_id)
    else:
        # search symbol @ in username and remove all before it
        if "@" in url:
            username = url.split("@")[1]
        # search symbol / in username and remove all after it
        if "/" in url:
            username = url.split("/")[0]
        # search symbol ? in username and remove all after it
        if "?" in url:
            username = url.split("?")[0]

        request = youtube.search().list(part="id,snippet", maxResults=1, q=username, type="channel")
        response = request.execute()

        if response["pageInfo"]["totalResults"] == 0:
            print("No channel found")
        else:
            print(f"Channel: {username}")
            channel_id = response["items"][0]["id"]["channelId"]
            return get_random_video_by_channel_id(channel_id)


def get_random_video_by_channel_id(channel_id):
    request = youtube.playlists().list(part="contentDetails, id, localizations, player, snippet, status", channelId=channel_id, maxResults=50)
    response = request.execute()

    if response["pageInfo"]["totalResults"] == 0:
        print("No playlists found")
    else:
        print("Number of playlists: ", response["pageInfo"]["totalResults"])

        # get random nubmer from 0 to totalResults
        random_item = random.randrange(0, 50 if response["pageInfo"]["totalResults"] > 50 else response["pageInfo"]["totalResults"] - 1)
        playlist_id = response["items"][random_item]["id"]

        print("Selected playlist: ", response["items"][random_item]["snippet"]["title"])

        request = youtube.playlistItems().list(part="contentDetails, id, snippet, status", maxResults=50, playlistId=playlist_id)
        response = request.execute()

        if response["pageInfo"]["totalResults"] == 0:
            print("No videos found")
        else:
            print("Number of videos: ", response["pageInfo"]["totalResults"])

            # get random nubmer from 0 to totalResults
            random_item = random.randrange(0, 50 if response["pageInfo"]["totalResults"] > 50 else response["pageInfo"]["totalResults"] - 1)
            video_id = response["items"][random_item]["contentDetails"]["videoId"]

            print("Selected video: ", response["items"][random_item]["snippet"]["title"])
            print("Video URL: ", f"https://www.youtube.com/watch?v={video_id}")

            return f"https://www.youtube.com/watch?v={video_id}"
