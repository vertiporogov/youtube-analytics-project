from googleapiclient.discovery import build
import json
import os

api_key: str = os.getenv('API-KEY-YouTube')
youtube = build('youtube', 'v3', developerKey=api_key)

class Channel:
    """Класс для ютуб-канала"""
    # api_key: str = os.getenv('API-KEY-YouTube')
    # youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id) -> str:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.title = self.print_info()['items'][0]['snippet']['title']
        self.description = self.print_info()['items'][0]['snippet']['description']
        self.url = self.print_info()['items'][0]['snippet']['thumbnails']['default']['url']
        self.subscriber_count = self.print_info()['items'][0]['statistics']['subscriberCount']
        self.video_count = self.print_info()['items'][0]['statistics']['videoCount']
        self.view_count = self.print_info()['items'][0]['statistics']['viewCount']




    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        id = self.channel_id
        channel = youtube.channels().list(id=id, part='snippet,statistics').execute()

        return channel

    @property
    def channel_id(self):

        return self.__channel_id

    @classmethod
    def get_service(cls):
        '''Метод возвращающий объект для работы с YouTube API'''
        youtube = build('youtube', 'v3', developerKey=api_key)

        return youtube

    def to_json(self, data_file):
        '''Метод сохраняющий в файл значения атрибутов экземпляра'''
        with open(data_file, "w", encoding='utf-8') as jsonfile:
            id = self.channel_id
            channel = youtube.channels().list(id=id, part='snippet,statistics').execute()

            return jsonfile.write(json.dumps(channel))











