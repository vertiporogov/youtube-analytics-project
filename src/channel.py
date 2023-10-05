from googleapiclient.discovery import build
import json
import os

api_key: str = os.getenv('API-KEY-YouTube')
# youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('API-KEY-YouTube')
    # youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.title = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()['items'][0]['snippet']['title']
        self.description = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()['items'][0]['snippet']['description']
        self.url = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()['items'][0]['snippet']['thumbnails']['default']['url']
        self.subscriber_count = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()['items'][0]['statistics']['subscriberCount']
        self.video_count = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()['items'][0]['statistics']['videoCount']
        self.view_count = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        id_ = self.channel_id
        channel = self.get_service().channels().list(id=id_, part='snippet,statistics').execute()
        return print(json.dumps(channel, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):

        return self.__channel_id

    @classmethod
    def get_service(cls):
        """Метод возвращающий объект для работы с YouTube API"""
        youtube_ = build('youtube', 'v3', developerKey=api_key)

        return youtube_

    def to_json(self, data_file):
        """Метод сохраняющий в файл значения атрибутов экземпляра"""
        fff = []
        with open(data_file, "w", encoding='utf-8') as jsonfile:
            # id_ = self.channel_id
            # fff.append(self.channel_id)
            fff.append(self.title)
            fff.append(self.description)
            fff.append(self.url)
            fff.append(self.subscriber_count)
            fff.append(self.video_count)
            fff.append(self.view_count)
            # channel = youtube.channels().list(id=id_, part='snippet,statistics').execute()

            return jsonfile.write(json.dumps(fff))

