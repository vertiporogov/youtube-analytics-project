import json

from googleapiclient.discovery import build
import os

api_key: str = os.getenv('API-KEY-YouTube')


class Video:

    # you_tube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id: str):
        self.__video_id = video_id
        channel = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails', id=video_id).execute()
        self.title = channel['items'][0]['snippet']['title']
        self.url = channel['items'][0]['snippet']['thumbnails']['default']['url']
        self.view_count = channel['items'][0]['statistics']['viewCount']
        self.like_count = channel['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.title

    @property
    def video_id(self):
        return self.__video_id

    @classmethod
    def get_service(cls):
        """Метод возвращающий объект для работы с YouTube API"""

        return build('youtube', 'v3', developerKey=api_key)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале ."""
        video_id = self.video_id
        channel = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails', id=video_id).execute()
        return print(json.dumps(channel, indent=2, ensure_ascii=False))